import streamlit as st
import json
import os
import pandas as pd

# Fungsi untuk membaca data dari file JSON
def baca_data_dari_file(nama_file):
    if os.path.exists(nama_file):
        with open(nama_file, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data.get('datapkl', {})
            except json.JSONDecodeError:
                st.error(f"Format data dalam file '{nama_file}' tidak valid.")
                return None
    else:
        st.error(f"File '{nama_file}' tidak ditemukan.")
        return None

# Fungsi untuk menyimpan data ke file JSON
def simpan_data_ke_file(data, nama_file):
    try:
        with open(nama_file, 'w', encoding='utf-8') as file:
            json.dump({"datapkl": data}, file, ensure_ascii=False, indent=4)
    except IOError as e:
        st.error(f"Terjadi kesalahan saat menyimpan data: {e}")

# Fungsi untuk login
def login(username, password):
    if username == "admin" and password == "admin123":
        return "admin"
    elif username == "user" and password == "user123":
        return "user"
    else:
        return None

# Fungsi untuk menambah buku
def tambah_buku(data, kategori, buku_baru):
    if kategori in data:
        data[kategori].append(buku_baru)
    else:
        data[kategori] = [buku_baru]
    return data

# Fungsi untuk menghapus buku
def hapus_buku(data, kategori, judul_buku):
    if kategori in data:
        data[kategori] = [buku for buku in data[kategori] if buku['judul_laporan_pkl'] != judul_buku]
    return data

# Nama file JSON (tanpa path lokal)
nama_file = "jsonadde.json"  # File berada dalam folder yang sama dengan skrip

# Membaca data dari file JSON
data_perpustakaan = baca_data_dari_file(nama_file)

# Pengaturan tampilan aplikasi
st.set_page_config(page_title="Pencarian Data Buku PKL", page_icon="📚", layout="wide")

# Halaman login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

if not st.session_state.logged_in:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        role = login(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.success(f"Login berhasil sebagai {role}")
        else:
            st.error("Username atau password salah")
else:
    # Menu setelah login
    if st.session_state.role == "admin":
        st.subheader("Selamat datang, Admin!")

        # Menampilkan pilihan fitur
        st.write("### Pilih Fitur yang Ingin Digunakan:")
        pilihan_fitur = st.radio("Fitur Admin", ["Pilih Kategori Buku", "Tambah Buku", "Hapus Buku"])

        if pilihan_fitur == "Pilih Kategori Buku":
            kategori_baru = st.selectbox("Pilih Kategori Buku", list(data_perpustakaan.keys()))
            if kategori_baru:
                buku_ditemukan = data_perpustakaan.get(kategori_baru, [])
                if buku_ditemukan:
                    # Menampilkan data dalam bentuk DataFrame
                    df = pd.DataFrame(buku_ditemukan)
                    df['No'] = range(1, len(df) + 1)  # Menambah kolom No
                    df = df.rename(columns={
                        'letak_buku_pkl': 'Letak Buku PKL',
                        'arsip_laporan_pkl': 'Arsip Laporan PKL',
                        'tahun_pelaksanaan': 'Tahun Pelaksanaan',
                        'nim': 'NIM',
                        'nama_mahasiswa': 'Nama Mahasiswa',
                        'judul_laporan_pkl': 'Judul Laporan PKL',
                        'nama_dosen_pembimbing': 'Nama Dosen Pembimbing',
                        'nama_tempat_pelaksanaan': 'Nama Tempat Pelaksanaan',
                        'kabupaten_kota': 'Kabupaten/Kota'
                    })
                    # Menampilkan kolom yang sudah diatur
                    df = df[['No', 'Letak Buku PKL', 'Arsip Laporan PKL', 'Tahun Pelaksanaan', 'NIM',
                             'Nama Mahasiswa', 'Judul Laporan PKL', 'Nama Dosen Pembimbing', 'Nama Tempat Pelaksanaan', 'Kabupaten/Kota']]
                    st.write("**Daftar Buku PKL:**")
                    st.write(df.to_html(index=False), unsafe_allow_html=True)
                else:
                    st.warning("Tidak ada buku yang ditemukan.")
        
        elif pilihan_fitur == "Tambah Buku":
            kategori_baru = st.selectbox("Pilih Kategori Buku untuk Ditambahkan", list(data_perpustakaan.keys()))
            if kategori_baru:
                with st.form("Tambah Buku"):
                    judul = st.text_input("Judul Laporan PKL")
                    letak = st.text_input("Letak Buku PKL")
                    arsip = st.text_input("Arsip Laporan PKL")
                    tahun = st.number_input("Tahun Pelaksanaan", min_value=2000, max_value=2100)
                    nim = st.text_input("NIM")
                    nama_mahasiswa = st.text_input("Nama Mahasiswa")
                    dosen = st.text_input("Nama Dosen Pembimbing")
                    tempat = st.text_input("Nama Tempat Pelaksanaan")
                    kota = st.text_input("Kabupaten/Kota")
                    submit_button = st.form_submit_button("Tambah Buku")

                    if submit_button:
                        buku_baru = {
                            "letak_buku_pkl": letak,
                            "arsip_laporan_pkl": arsip,
                            "tahun_pelaksanaan": tahun,
                            "nim": nim,
                            "nama_mahasiswa": nama_mahasiswa,
                            "judul_laporan_pkl": judul,
                            "nama_dosen_pembimbing": dosen,
                            "nama_tempat_pelaksanaan": tempat,
                            "kabupaten_kota": kota
                        }
                        # Update data
                        data_perpustakaan = tambah_buku(data_perpustakaan, kategori_baru, buku_baru)
                        # Simpan data yang telah diperbarui ke file JSON
                        simpan_data_ke_file(data_perpustakaan, nama_file)
                        st.success("Buku berhasil ditambahkan")

        elif pilihan_fitur == "Hapus Buku":
            kategori_baru = st.selectbox("Pilih Kategori Buku untuk Dihapus", list(data_perpustakaan.keys()))
            if kategori_baru:
                buku_yang_dihapus = st.text_input("Judul Buku untuk Dihapus")
                if st.button("Hapus Buku"):
                    data_perpustakaan = hapus_buku(data_perpustakaan, kategori_baru, buku_yang_dihapus)
                    # Simpan data yang telah diperbarui ke file JSON
                    simpan_data_ke_file(data_perpustakaan, nama_file)
                    st.success(f"Buku '{buku_yang_dihapus}' berhasil dihapus")
        
    elif st.session_state.role == "user":
        st.subheader("Selamat datang, User!")
        kategori_yang_dicari = st.selectbox("Pilih Kategori Buku", list(data_perpustakaan.keys()))
        
        if kategori_yang_dicari:
            buku_ditemukan = data_perpustakaan.get(kategori_yang_dicari, [])
            if buku_ditemukan:
                # Menampilkan data dalam bentuk DataFrame
                df = pd.DataFrame(buku_ditemukan)
                df['No'] = range(1, len(df) + 1)  # Menambah kolom No
                df = df.rename(columns={
                    'letak_buku_pkl': 'Letak Buku PKL',
                    'arsip_laporan_pkl': 'Arsip Laporan PKL',
                    'tahun_pelaksanaan': 'Tahun Pelaksanaan',
                    'nim': 'NIM',
                    'nama_mahasiswa': 'Nama Mahasiswa',
                    'judul_laporan_pkl': 'Judul Laporan PKL',
                    'nama_dosen_pembimbing': 'Nama Dosen Pembimbing',
                    'nama_tempat_pelaksanaan': 'Nama Tempat Pelaksanaan',
                    'kabupaten_kota': 'Kabupaten/Kota'
                })
                # Menampilkan kolom yang sudah diatur
                df = df[['No', 'Letak Buku PKL', 'Arsip Laporan PKL', 'Tahun Pelaksanaan', 'NIM',
                         'Nama Mahasiswa', 'Judul Laporan PKL', 'Nama Dosen Pembimbing', 'Nama Tempat Pelaksanaan', 'Kabupaten/Kota']]
                st.write("**Daftar Buku PKL:**")
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                st.warning("Tidak ada buku yang ditemukan.")
    
    # Tombol logout
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.success("Logout berhasil")
