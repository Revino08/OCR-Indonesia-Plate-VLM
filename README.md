## Nama : Revino Jantri Putra
## Nim : 4222201021
## Robotika A pagi Semester 6


# (Optical Character Recognition) OCR-Indonesia-Plate-VLM (USing Python +LMStudio)

Proyek ini dirancang untuk mengenali karakter pada plat nomor kendaraan dengan memanfaatkan **model Visual Language (VLM)** yang dijalankan melalui **LMStudio** dan terhubung dengan Python.

# 1. Membuat Folder
indonesian-license-plate-dataset/
│

├── test/

|      ├── test001_1.jpg

|      ├── test001_1.txt

│      ├── test002_1.jpg

│      ├── test002_1.txt

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
Jalankan generate_ground_truth_csv.py untuk membuat file ground_truth.csv kedalam file .txt. Hasil akan disimpan sebagai "ground_truth.csv", pastikan file yang dibuat masuk kedalam test.
Sebagai contoh ground_truth.csv:


<img width="302" height="314" alt="image" src="https://github.com/user-attachments/assets/ab8f72af-8957-4c89-8b45-009ee40e68cb" />



Selanjutnya membuat program prediction dan beri label "predictions.py" lalu running program tersebut di cmd. Program akan melakukan encode gambar ke Base64, mengirim ke LM Studio dan menerima hasil prediksi sekaligus menghitung CER berdasarkan ground truth yang dibuat sebelumnya dan menyimpan ke "prediction_results.csv".
Sebagai contoh prediction.results.csv:


<img width="302" height="314" alt="image" src="https://github.com/user-attachments/assets/2716defd-46a8-4caf-b7c8-347d13b8813a" />



# 4. Prediksi pada LMStudio
Pilih power user pada kiri bawah dan masuk kedalam comment dan cobalah lakukan pengujian dari beberapa gambar plat yang telah di prediksi dan masukkan prompt "What is the license plate number shown in this image? Respond only with the plate number."

# Character Error Rate dihitung dengan rumus:
Rumus :
CER = (S + D + I) / N

- **S** = jumlah karakter salah (substitusi).
- **D** = jumlah karakter yang dihapus.
- **I** = jumlah karakter yang disisipkan.
- **N** = jumlah karakter pada ground truth.

# 5. Video Penjelasan 
https://youtu.be/zVXV-hsDY94

