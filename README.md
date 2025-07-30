## Nama : Revino Jantri Putra
## Nim : 4222201021
## Robotika A pagi Semester 6


# (Optical Character Recognition) OCR-Indonesia-Plate-VLM (USing Python +LMStudio)

Proyek ini dirancang untuk mengenali karakter pada plat nomor kendaraan dengan memanfaatkan **model Visual Language (VLM)** yang dijalankan melalui **LMStudio** dan terhubung dengan Python.

# 1. Membuat Folder
indonesian-license-plate-dataset/
│
├── test/
│   ├── test001_1.jpg
|   ├── test001_1.txt
│   ├── test002_1.jpg
│   └── test002_1.txt
│
├── Generate_ground_truth.csv/
│
├── prediction.py/
|
├── ground_truth.csv/
├── prediction_results.csv/

# 2. Persiapan dan Kebutuhan
* Install Python 3
* Install LMStudio (dijalankan lokal pada `http://127.0.0.1:1234`) pilih model "Llava-mini-3-phi-gguf" pastikan model tersebut sudah diinstall didalam LMStudio
* Download Dataset: [Indonesian License Plate Dataset](https://www.kaggle.com/datasets/juanthomaswijaya/indonesian-license-plate-dataset)
* Jalankan LMStudio pada Command Prompt 'cmd /c %USERPROFILE%/.lmstudio/bin/lms.exe bootstrap' lalu ketik lms server start. Apabila berhasil akan muncul pesan atau tulisan "Success! Server is now running on port 1234"

# 3. Jalankan Program
Jalankan generate_ground_truth_csv.py untuk membuat file ground_truth.csv kedalam file .txt. Hasil akan disimpan sebagai "ground_truth.csv", apstikan file yang dibuat masuk kedalam test.
Misal ground_truth.csv:

<img width="302" height="314" alt="image" src="https://github.com/user-attachments/assets/ab8f72af-8957-4c89-8b45-009ee40e68cb" />
