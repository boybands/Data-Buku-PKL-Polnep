import streamlit as st
import qrcode
import pandas as pd
from PIL import Image
from io import BytesIO
import mysql.connector

# Fungsi untuk membuat QR code
def buat_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Fungsi untuk membaca data dari database MySQL
def baca_data_dari_mysql():
    try:
        # Koneksi ke MySQL
        conn = mysql.connector.connect(
            host="localhost",  # Ganti dengan host server Anda
            user="root",       # Ganti dengan username MySQL Anda
            password="",  # Ganti dengan password MySQL Anda
            database="dataPKL"  # Ganti dengan nama database Anda
        )
        cursor = conn.cursor(dictionary=True)
        # Mengambil data dari tabel yang benar
        cursor.execute('''SELECT Letak_bukuPKL AS `Letak Buku PKL`,
                                  arsip_laporan_pkl AS `Arsip Laporan PKL`,
                                  tahun_pelaksanaan AS `Tahun Pelaksanaan`,
                                  nim AS `NIM`,
                                  nama_mahasiswa AS `Nama Mahasiswa`,
                                  judul_laporan_pkl AS `Judul Laporan PKL`,
                                  nama_dosen_pembimbing AS `Nama Dosen Pembimbing`,
                                  nama_tempat_pelaksanaan AS `Nama Tempat Pelaksanaan`,
                                  kabupaten_kota AS `Kabupaten/Kota`
                           FROM tb_listrik''')  # Gunakan nama tabel yang benar
        data = cursor.fetchall()
        conn.close()
        return data
    except mysql.connector.Error as err:
        st.error(f"Terjadi kesalahan saat mengakses database: {err}")
        return None

# Fungsi untuk mencari laporan PKL berdasarkan judul
def cari_laporan(judul_dicari, data):
    for laporan in data:
        if 'Judul Laporan PKL' in laporan and laporan['Judul Laporan PKL'].lower() == judul_dicari.lower():
            return laporan
    return None

# Set page config sebagai Streamlit command pertama
st.set_page_config(page_title="Pencarian Laporan PKL", layout="wide")

# Menampilkan QR code untuk aplikasi di perangkat mobile
url_aplikasi = "https://pencarian-laporan-pkl.streamlit.app/"  # Ganti dengan URL aplikasi yang dihosting
qr_code = buat_qr_code(url_aplikasi)
qr_image = Image.open(qr_code)

# Menampilkan QR code di sidebar
st.sidebar.image(qr_image, caption="Scan QR untuk Akses Aplikasi di HP")

# Sidebar
st.sidebar.header("Pencarian Laporan PKL")
st.sidebar.markdown("""Gunakan aplikasi ini untuk mencari laporan PKL yang ada. Pilih judul laporan pada kolom di bawah dan tekan tombol 'Cari'.""")
st.title("📚 Pencarian Laporan PKL")

# Membaca data dari MySQL
data_perpustakaan = baca_data_dari_mysql()

# Jika data berhasil dibaca
if data_perpustakaan:
    # Ambil daftar judul laporan PKL dari data
    daftar_judul = ["Pilih Judul Laporan PKL"] + [laporan.get('Judul Laporan PKL', 'Judul Tidak Tersedia') for laporan in data_perpustakaan]

    # Input pengguna
    judul_yang_dicari = st.selectbox("Pilih Judul Laporan PKL:", daftar_judul)

    # Tombol untuk mencari
    if st.button("Cari"):
        if judul_yang_dicari != "Pilih Judul Laporan PKL":
            # Cari laporan PKL berdasarkan judul yang dipilih
            laporan_ditemukan = cari_laporan(judul_yang_dicari, data_perpustakaan)
            
            # Buat DataFrame untuk menampilkan hasil
            if laporan_ditemukan:
                df = pd.DataFrame([laporan_ditemukan])
                df = df[['Letak Buku PKL', 'Arsip Laporan PKL', 'Tahun Pelaksanaan', 'NIM', 'Nama Mahasiswa', 
                         'Judul Laporan PKL', 'Nama Dosen Pembimbing', 'Nama Tempat Pelaksanaan', 'Kabupaten/Kota']]
                st.subheader(f"Detail Laporan PKL '{judul_yang_dicari}':")
                st.write(df.to_html(index=False), unsafe_allow_html=True)  # Tampilkan tabel tanpa indeks
            else:
                st.warning("Laporan PKL tidak ditemukan.")
        else:
            st.warning("Silakan pilih judul laporan PKL.")
else:
    st.error("Data laporan PKL tidak tersedia.")
