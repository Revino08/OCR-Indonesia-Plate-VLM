import os
import csv
import json
import requests
import base64
import re
from Levenshtein import distance as levenshtein_distance

# === Konfigurasi ===
FOLDER = r"C:\Users\revin\OneDrive\Dokumen\Semester 6\Computer Vision-RE604\Indonesian License Plate Recognition Dataset\test"
GROUND_TRUTH_CSV = os.path.join(FOLDER, "ground_truth.csv")
OUTPUT_CSV = os.path.join(FOLDER, "prediction_result.csv")
LMSTUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "llava-phi-3-mini"

# === Encode gambar ke base64 ===
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    base64_str = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:image/jpeg;base64,{base64_str}"

# === Hitung CER:
def calculate_cer(ground_truth, prediction):
    gt = ground_truth.strip().upper()
    pred = prediction.strip().upper()
    N = max(len(gt), 1)
    edit_distance = levenshtein_distance(gt, pred)
    cer = edit_distance / N
    return cer

# === Ekstrak karakter plat nomor dari jawaban model ===
def clean_prediction(text):
    text = text.upper().strip()
    
    # Cari format umum plat nomor Indonesia: huruf 1–2, angka 1–4, huruf 1–3
    matches = re.findall(r'\b([A-Z]{1,2}[0-9]{1,4}[A-Z]{1,3})\b', text)
    if matches:
        return matches[0]
    
    # Jika tidak ada match, return "ERROR"
    return "ERROR"


# === Ambil prediksi dari VLM ===
def get_prediction(image_path):
    image_b64 = encode_image_to_base64(image_path)
    prompt = "What is the license plate number shown in this image? Respond only with the plate number."

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": image_b64}},
                    {"type": "text", "text": prompt}
                ]
            }
        ],
        "temperature": 0.2,
        "stream": False
    }

    try:
        response = requests.post(LMSTUDIO_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip().replace(" ", "").upper()
    except Exception as e:
        print(f"❌ Gagal OCR untuk {image_path}: {e}")
    return "ERROR"

# === Load ground truth ===
def load_ground_truth():
    ground_truth = {}
    with open(GROUND_TRUTH_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ground_truth[row["image"]] = row["ground_truth"].strip().replace(" ", "").upper()
    return ground_truth

# === Main Process ===
def main():
    ground_truths = load_ground_truth()
    output_rows = []

    for filename in sorted(os.listdir(FOLDER)):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(FOLDER, filename)
            prediction = get_prediction(image_path)
            gt = ground_truths.get(filename, "")
            cer = calculate_cer(gt, prediction)
            print(f"{filename} | GT: {gt} | Pred: {prediction} | CER: {cer}")
            output_rows.append({
                "image": filename,
                "ground_truth": gt,
                "prediction": prediction,
                "CER_score": cer
            })

    # Simpan hasil ke CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["image", "ground_truth", "prediction", "CER_score"])
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"\nHasil prediksi disimpan di: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()