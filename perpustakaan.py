import streamlit as st
import pandas as pd
import mysql.connector

# Fungsi untuk membaca data dari database MySQL berdasarkan nama tabel
def baca_data_dari_mysql(nama_tabel):
    try:
        # Koneksi ke MySQL
        conn = mysql.connector.connect(
            host="localhost",  # Ganti dengan host server Anda
            user="root",       # Ganti dengan username MySQL Anda
            password="",        # Ganti dengan password MySQL Anda
            database="dataPKL"  # Ganti dengan nama database Anda
        )
        cursor = conn.cursor(dictionary=True)
        # Mengambil data dari tabel berdasarkan pilihan
        query = f'''SELECT Letak_bukuPKL AS `Letak Buku PKL`,
                           arsip_laporan_pkl AS `Arsip Laporan PKL`,
                           tahun_pelaksanaan AS `Tahun Pelaksanaan`,
                           nim AS `NIM`,
                           nama_mahasiswa AS `Nama Mahasiswa`,
                           judul_laporan_pkl AS `Judul Laporan PKL`,
                           nama_dosen_pembimbing AS `Nama Dosen Pembimbing`,
                           nama_tempat_pelaksanaan AS `Nama Tempat Pelaksanaan`,
                           kabupaten_kota AS `Kabupaten/Kota`
                    FROM {nama_tabel}'''
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    except mysql.connector.Error as err:
        st.error(f"Terjadi kesalahan saat mengakses database: {err}")
        return None

# Set page config sebagai Streamlit command pertama
st.set_page_config(page_title="Pencarian Laporan PKL", layout="wide")

# Sidebar
st.sidebar.header("Pencarian Laporan PKL")
st.sidebar.markdown("""Gunakan aplikasi ini untuk mencari laporan PKL yang ada. Pilih tabel di bawah untuk melihat data.""")
st.title("📚 Pencarian Laporan PKL")

# Pilihan tabel
daftar_tabel = ["tb_informatika", "tb_elektronika", "tb_listrik"]  # Daftar tabel
nama_tabel = st.selectbox("Pilih Tabel Data PKL:", daftar_tabel)

# Tombol untuk mencari
if st.button("Cari"):
    # Membaca data dari tabel yang dipilih
    data_perpustakaan = baca_data_dari_mysql(nama_tabel)
    
    if data_perpustakaan:
        # Menampilkan tabel data laporan
        st.subheader(f"Data Laporan PKL dari Tabel '{nama_tabel}':")
        df = pd.DataFrame(data_perpustakaan)
        df = df[['Letak Buku PKL', 'Arsip Laporan PKL', 'Tahun Pelaksanaan', 'NIM', 'Nama Mahasiswa', 
                 'Judul Laporan PKL', 'Nama Dosen Pembimbing', 'Nama Tempat Pelaksanaan', 'Kabupaten/Kota']]
        st.write(df.to_html(index=False), unsafe_allow_html=True)  # Tampilkan tabel tanpa indeks
    else:
        st.warning(f"Tidak ada data ditemukan di tabel '{nama_tabel}'.")
