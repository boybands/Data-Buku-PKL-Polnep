import streamlit as st
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data login admin hardcoded
admin_username = "admin"
admin_password = "admin123"  # Ganti dengan password yang sesuai

# Fungsi untuk membaca data dari file JSON (akun login)
def baca_data_login():
    if os.path.exists("akun_pengguna.json"):
        with open("akun_pengguna.json", 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data.get('pengguna', {})
            except json.JSONDecodeError:
                st.error(f"Format data dalam file 'akun_pengguna.json' tidak valid.")
                return {}
    else:
        st.error(f"File 'akun_pengguna.json' tidak ditemukan.")
        return {}

# Fungsi untuk menyimpan data login ke file JSON
def simpan_data_login(data_login):
    with open("akun_pengguna.json", 'w', encoding='utf-8') as file:
        json.dump({'pengguna': data_login}, file, ensure_ascii=False, indent=4)

# Fungsi untuk membaca data dari file JSON
def baca_data_dari_file(nama_file):
    if os.path.exists(nama_file):
        with open(nama_file, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data.get('datapkl', {})
            except json.JSONDecodeError:
                st.error(f"Format data dalam file '{nama_file}' tidak valid.")
                return {}
    else:
        st.error(f"File '{nama_file}' tidak ditemukan.")
        return {}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data_ke_file(nama_file, data):
    with open(nama_file, 'w', encoding='utf-8') as file:
        json.dump({'datapkl': data}, file, ensure_ascii=False, indent=4)

# Fungsi untuk login
def login(username, password, data_login):
    # Cek apakah login adalah admin atau user biasa
    if username == admin_username and password == admin_password:
        return "admin"
    elif username in data_login and data_login[username] == password:
        return "user"
    return None

# Fungsi untuk mendaftar pengguna baru
def daftar(username, password, data_login):
    if username not in data_login:
        data_login[username] = password
        simpan_data_login(data_login)
        return True
    return False

# Fungsi untuk menambah buku
def Tambah_Buku(data_perpustakaan, kategori, buku_baru):
    if kategori in data_perpustakaan:
        data_perpustakaan[kategori].append(buku_baru)
    else:
        data_perpustakaan[kategori] = [buku_baru]
    return data_perpustakaan

# Fungsi untuk menghapus buku
def Hapus_Buku(data_perpustakaan, kategori, judul_buku):
    if kategori in data_perpustakaan:
        data_perpustakaan[kategori] = [
            buku for buku in data_perpustakaan[kategori] if buku['judul_laporan_pkl'] != judul_buku
        ]
    return data_perpustakaan

# Fungsi untuk mengedit buku
def edit_buku(data_perpustakaan, kategori, judul_lama, data_baru):
    if kategori in data_perpustakaan:
        for i, buku in enumerate(data_perpustakaan[kategori]):
            if buku['judul_laporan_pkl'] == judul_lama:
                data_perpustakaan[kategori][i] = data_baru
                break
    return data_perpustakaan

# Nama file JSON untuk data buku
nama_file = "jsonadde.json"

# Membaca data dari file JSON untuk buku
data_perpustakaan = baca_data_dari_file(nama_file)

# Data Buku Laporan PKL per Tahun (contoh data)
years = [2020, 2021, 2022, 2023, 2024]
books_reported = [10, 15, 25, 35, 40]  # Jumlah buku per tahun

# Pengaturan tampilan aplikasi
st.set_page_config(page_title="Pencarian Data Buku PKL", page_icon="📚", layout="wide")

# Halaman login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

# Membaca data login dari file JSON
data_login = baca_data_login()

# Jika pengguna belum login, tampilkan halaman login
if not st.session_state.logged_in:
    st.subheader("Login")
    
    # Pilih antara Login atau Daftar
    menu = st.radio("Pilih Menu", ("Login", "Daftar"))
    
    if menu == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            role = login(username, password, data_login)
            if role == "admin":
                st.session_state.logged_in = True
                st.session_state.role = "admin"
                st.success(f"Login berhasil sebagai {username}!")
            elif role == "user":
                st.session_state.logged_in = True
                st.session_state.role = "user"
                st.success(f"Login berhasil sebagai {username}!")
            else:
                st.error("Username atau password salah")
    
    elif menu == "Daftar":
        st.subheader("Pendaftaran Akun Baru")
        username_daftar = st.text_input("Username Baru")
        password_daftar = st.text_input("Password Baru", type="password")
        
        if st.button("Daftar"):
            if username_daftar and password_daftar:
                if daftar(username_daftar, password_daftar, data_login):
                    st.success("Akun berhasil dibuat! Silakan login.")
                else:
                    st.error("Username sudah terdaftar!")
            else:
                st.error("Harap isi semua kolom.")

else:
    # Menu setelah login, tampilkan menu berdasarkan role
    if st.session_state.role == "admin":
        pilihan_fitur = st.sidebar.selectbox("Pilih Fitur", ["Dashboard", "Pilih Kategori Buku", "Tambah Buku", "Hapus Buku", "Edit Buku", "Logout"])
    elif st.session_state.role == "user":
        pilihan_fitur = st.sidebar.selectbox("Pilih Fitur", ["Dashboard", "Pilih Kategori Buku", "Logout"])

    if pilihan_fitur == "Dashboard":
        st.subheader("Dashboard Buku PKL")

        # Menampilkan grafik data PKL (Area Chart)
        st.subheader("Area Chart - Jumlah Buku Laporan PKL per Tahun")
        fig, ax = plt.subplots(figsize=(8, 4))  # Ukuran gambar diperkecil
        ax.fill_between(years, books_reported, color="skyblue", alpha=0.5)
        ax.set_title("Jumlah Buku Laporan PKL per Tahun (Area Chart)")
        ax.set_xlabel("Tahun")
        ax.set_ylabel("Jumlah Buku Laporan PKL")
        ax.set_xticks(years)  # Mengatur sumbu x dengan nilai tahun sebagai integer
        st.pyplot(fig)

        # Menampilkan grafik data PKL (Bar Chart)
        st.subheader("Bar Chart - Jumlah Buku Laporan PKL per Tahun")
        fig, ax = plt.subplots(figsize=(8, 4))  # Ukuran gambar diperkecil
        ax.bar(years, books_reported, color='orange')
        ax.set_title("Jumlah Buku Laporan PKL per Tahun (Bar Chart)")
        ax.set_xlabel("Tahun")
        ax.set_ylabel("Jumlah Buku Laporan PKL")
        st.pyplot(fig)

    if pilihan_fitur == "Pilih Kategori Buku":
        st.subheader("Daftar Buku")
        kategori_yang_dicari = st.selectbox("Pilih Kategori Buku", list(data_perpustakaan.keys()))
        
        if kategori_yang_dicari:
            tahun_pelaksanaan = st.selectbox(
                "Pilih Tahun Pelaksanaan", 
                sorted(set(b['tahun_pelaksanaan'] for b in data_perpustakaan[kategori_yang_dicari]))
            )
            
            buku_ditemukan = [
                b for b in data_perpustakaan[kategori_yang_dicari] 
                if b['tahun_pelaksanaan'] == tahun_pelaksanaan
            ]
            
            if buku_ditemukan:
                df = pd.DataFrame(buku_ditemukan)
                df['No'] = range(1, len(df) + 1)
                df = df.rename(columns={  
                    'letak_buku_pkl': 'Letak Buku PKL',
                    'arsip_laporan_pkl': 'Arsip Laporan PKL', 
                    'tahun_pelaksanaan': 'Tahun Pelaksanaan', 
                    'nim': 'NIM', 
                    'nama_mahasiswa': 'Nama Mahasiswa', 
                    'judul_laporan_pkl': 'Judul Laporan PKL', 
                    'nama_dosen_pembimbing': 'Nama Dosen Pembimbing',  
                    'kabupaten_kota': 'Kabupaten/Kota' 
                })
                
                # Pastikan semua kolom yang ingin diakses ada
                required_columns = ['No', 'Arsip Laporan PKL', 'Tahun Pelaksanaan', 'NIM', 'Nama Mahasiswa', 'Judul Laporan PKL', 'Nama Dosen Pembimbing', 'Kabupaten/Kota']
                missing_columns = [col for col in required_columns if col not in df.columns]
                
                if missing_columns:
                    st.error(f"Kolom berikut tidak ditemukan: {', '.join(missing_columns)}")
                else:
                    df = df[required_columns]
                    st.write("*Daftar Buku PKL:*")
                    st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                st.warning("Tidak ada buku yang ditemukan untuk kategori dan tahun tersebut.")
            
    elif pilihan_fitur == "Tambah Buku" and st.session_state.role == "admin":
        
        # Hanya admin yang dapat menambah buku
        kategori_baru = st.selectbox("Pilih Kategori Buku", list(data_perpustakaan.keys()))
        
        # Validasi input dengan real-time feedback
        with st.form("Tambah Buku", clear_on_submit=True):
            judul = st.text_input("Judul Laporan PKL", help="Masukkan judul laporan PKL (hanya huruf dan angka)")
            letak = st.text_input("Letak Buku PKL", help="Lokasi buku di perpustakaan")
            arsip = st.text_input("Arsip Laporan PKL", help="Kode atau nomor arsip laporan")
            tahun = st.number_input("Tahun Pelaksanaan", min_value=2000, max_value=2100, value=2024, help="Masukkan tahun pelaksanaan PKL (misalnya: 2024)")
            nim = st.text_input("NIM", help="Nomor Induk Mahasiswa (harus berupa angka)")
            nama_mahasiswa = st.text_input("Nama Mahasiswa", help="Masukkan nama mahasiswa (hanya huruf dan spasi)")
            dosen_pembimbing = st.text_input("Nama Dosen Pembimbing", help="Masukkan nama dosen pembimbing")
            tempat_pelaksanaan = st.text_input("Nama Tempat Pelaksanaan", help="Nama tempat pelaksanaan PKL")
            kabupaten_kota = st.text_input("Kabupaten/Kota", help="Nama kabupaten atau kota tempat PKL")
            
            if st.form_submit_button("Tambah Buku"):
            # Validasi data
                errors = []
                if not judul.strip():
                    errors.append("Judul laporan PKL tidak boleh kosong.")
                if not arsip.strip():
                    errors.append("Arsip laporan PKL tidak boleh kosong.")
                if not nim.isdigit():
                    errors.append("NIM harus berupa angka.")
                if not nama_mahasiswa.replace(" ", "").isalpha():
                    errors.append("Nama Mahasiswa hanya boleh terdiri dari huruf dan spasi.")
                if not dosen_pembimbing.replace(" ", "").isalpha():
                    errors.append("Nama Dosen Pembimbing hanya boleh terdiri dari huruf dan spasi.")
                if not kabupaten_kota.strip():
                    errors.append("Kabupaten/Kota tidak boleh kosong.")

                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    # Data valid, simpan buku baru
                    buku_baru = {
                        'letak_buku_pkl': letak.strip(),
                        'arsip_laporan_pkl': arsip.strip(),
                        'tahun_pelaksanaan': tahun,
                        'nim': nim.strip(),
                        'nama_mahasiswa': nama_mahasiswa.strip(),
                        'judul_laporan_pkl': judul.strip(),
                        'nama_dosen_pembimbing': dosen_pembimbing.strip(),
                        'kabupaten_kota': kabupaten_kota.strip()
                    }
                    data_perpustakaan = Tambah_Buku(data_perpustakaan, kategori_baru, buku_baru)
                    simpan_data_ke_file(nama_file, data_perpustakaan)
                    st.success(f"Buku '{judul}' berhasil ditambahkan!")
    
    elif pilihan_fitur == "Hapus Buku" and st.session_state.role == "admin":
        st.subheader("Hapus Buku")
        kategori_hapus = st.selectbox("Pilih Kategori Buku", list(data_perpustakaan.keys()))
        
        # Pilih buku yang ingin dihapus
        judul_buku_hapus = st.selectbox("Pilih Judul Buku yang ingin dihapus", 
                                        [buku['judul_laporan_pkl'] for buku in data_perpustakaan.get(kategori_hapus, [])])
        
        if st.button("Hapus Buku"):
            if judul_buku_hapus:
                data_perpustakaan = Hapus_Buku(data_perpustakaan, kategori_hapus, judul_buku_hapus)
                simpan_data_ke_file(nama_file, data_perpustakaan)
                st.success(f"Buku '{judul_buku_hapus}' berhasil dihapus!")
    
    elif pilihan_fitur == "Edit Buku" and st.session_state.role == "admin":
        st.subheader("Edit Buku")
        kategori_edit = st.selectbox("Pilih Kategori Buku", list(data_perpustakaan.keys()))
        
        # Pilih buku yang ingin diedit
        judul_buku_edit = st.selectbox("Pilih Judul Buku yang ingin diedit", 
                                       [buku['judul_laporan_pkl'] for buku in data_perpustakaan.get(kategori_edit, [])])
        
        # Form edit buku
        if judul_buku_edit:
            buku_yang_diedit = next(buku for buku in data_perpustakaan[kategori_edit] if buku['judul_laporan_pkl'] == judul_buku_edit)
            st.write(f"Editing Buku: {judul_buku_edit}")
            
            # Buat form untuk edit buku
            with st.form("Edit Buku"):
                judul_edit = st.text_input("Judul Laporan PKL", value=buku_yang_diedit['judul_laporan_pkl'])
                letak_edit = st.text_input("Letak Buku PKL", value=buku_yang_diedit['letak_buku_pkl'])
                arsip_edit = st.text_input("Arsip Laporan PKL", value=buku_yang_diedit['arsip_laporan_pkl'])
                tahun_edit = st.number_input("Tahun Pelaksanaan", min_value=2000, max_value=2100, value=buku_yang_diedit['tahun_pelaksanaan'])
                nim_edit = st.text_input("NIM", value=buku_yang_diedit['nim'])
                nama_mahasiswa_edit = st.text_input("Nama Mahasiswa", value=buku_yang_diedit['nama_mahasiswa'])
                dosen_pembimbing_edit = st.text_input("Nama Dosen Pembimbing", value=buku_yang_diedit['nama_dosen_pembimbing'])
                tempat_pelaksanaan_edit = st.text_input("Nama Tempat Pelaksanaan", value=buku_yang_diedit['nama_tempat_pelaksanaan'])
                kabupaten_kota_edit = st.text_input("Kabupaten/Kota", value=buku_yang_diedit['kabupaten_kota'])

                # Tombol submit di dalam form
                submit_button = st.form_submit_button("Update Buku")

                if submit_button:
                    data_baru = {
                        'judul_laporan_pkl': judul_edit,
                        'letak_buku_pkl': letak_edit,
                        'arsip_laporan_pkl': arsip_edit,
                        'tahun_pelaksanaan': tahun_edit,
                        'nim': nim_edit,
                        'nama_mahasiswa': nama_mahasiswa_edit,
                        'nama_dosen_pembimbing': dosen_pembimbing_edit,
                        'nama_tempat_pelaksanaan': tempat_pelaksanaan_edit,
                        'kabupaten_kota': kabupaten_kota_edit
                    }
                    data_perpustakaan = edit_buku(data_perpustakaan, kategori_edit, judul_buku_edit, data_baru)
                    simpan_data_ke_file(nama_file, data_perpustakaan)
                    st.success(f"Buku '{judul_buku_edit}' berhasil diperbarui!")


    elif pilihan_fitur == "Logout":
        st.session_state.logged_in = False
        st.session_state.role = None
        st.success("Anda berhasil logout!")
        st.rerun()
