from flask import Flask, render_template

app = Flask(__name__)


# Data Pengurus
pengurus = [
    {"nama": "Basith Arrasyid", "jabatan": "Ketua Umum", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
    {"nama": "Firdaus Fadhilah", "jabatan": "Kepala Bidang", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
    {"nama": "Dena Agustin", "jabatan": "Sekretaris", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
    {"nama": "Nazla Khouerun Nisa", "jabatan": "Bendahara", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"}
]

# Data Divisi
divisi = [
    {
        "nama": "Divisi Jaringan Strategis & Dampak Sosial",
        "anggota": [
            {"nama": "Anggota 1", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
            {"nama": "Anggota 2", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
            {"nama": "Anggota 3", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
        ]
    },
    {
        "nama": "Divisi Inovasi & Pusat Keilmuan",
        "anggota": [
            {"nama": "Anggota 4", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
            {"nama": "Anggota 5", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
            {"nama": "Anggota 6", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
        ]
    },
    {
        "nama": "Divisi Sosial dan Masyarakat",
        "anggota": [
            {"nama": "Anggota 7", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
            {"nama": "Anggota 8", "foto": "https://cdn-icons-png.flaticon.com/512/3869/3869383.png"},
        ]
    }
]

# Data untuk Berita
berita_list = [
    {
        "judul": "Rektor ITM Raih Gelar Doktor",
        "deskripsi": "Rektor Institut Teknologi Al-Muhajirin, Dr. Eti Jumiati, S.E., M.M., berhasil menyelesaikan program doktoralnya dalam bidang Hukum Islam di UIN Sunan Gunung Djati Bandung.",
        "gambar": "https://almuhajirin.co.id/wp-content/uploads/2024/11/itm2-768x539.jpg",
        "link": "https://almuhajirin.co.id/selamat-rektor-institut-teknologi-al-muhajirin-itm-purwakarta-ibu-eti-jumiati-raih-gelar-doktor/"
    },
    {
        "judul": "ITM Gelar ITM Sport Cup 2023",
        "deskripsi": "Institut Teknologi Al-Muhajirin mengadakan ITM Sport Cup 2023 untuk mencari talenta muda berbakat dalam cabang olahraga bola voli.",
        "gambar": "https://almuhajirin.co.id/wp-content/uploads/2023/03/IMG_2880-scaled-1-768x512.jpg",
        "link": "https://almuhajirin.co.id/institut-teknologi-al-muhajirin-gelar-itm-sport-cup-2023/"
    },
    {
        "judul": "Seminar Nasional di ITM Bahas Pendidikan di Era Digital",
        "deskripsi": "Yayasan Al-Muhajirin bekerja sama dengan Universitas Langlangbuana menggelar Seminar Nasional bertema 'Perkembangan Pendidikan di Era Digital: Peluang dan Tantangan'.",
        "gambar": "https://almuhajirin.co.id/wp-content/uploads/2025/01/cnk-724x1024.jpg",
        "link": "https://almuhajirin.co.id/seminar-nasional-perkembangan-pendidikan-di-era-digital-peluang-dan-tantangan-siap-digelar-di-al-muhajirin-kampus-2-purwakarta/"
    },
    {
        "judul": "Beasiswa Kuliah Gratis di ITM",
        "deskripsi": "Institut Teknologi Al-Muhajirin meluncurkan program 'Beasiswa Untuk Negeri' yang menawarkan biaya kuliah gratis untuk program S1 di beberapa prodi.",
        "gambar": "https://almuhajirin.co.id/wp-content/uploads/2024/07/753fa832-36d5-4b68-b7ef-32c916d3d8ed-768x960.jpg",
        "link": "https://almuhajirin.co.id/kabar-gembira-ada-kuliah-gratis-di-institut-teknologi-al-muhajirin/"
    },
    {
        "judul": "Yayasan Al-Muhajirin Wakafkan Perguruan Tinggi Teknologi ke PWNU Jabar",
        "deskripsi": "Yayasan Al-Muhajirin mewakafkan Institut Teknologi Al-Muhajirin kepada PWNU Jawa Barat dalam rangka peringatan Maulid Nabi dan Hari Santri Nasional.",
        "gambar": "https://assets.jabarekspres.com/pasundan/2023/10/B-2-1200x675.webp",
        "link": "https://pasundan.jabarekspres.com/2023/10/27/yayasan-al-muhajirin-wakafkan-perguruan-tinggi-teknologi-ke-pwnu-jabar/"
    }
]


# Data untuk Kegiatan
kegiatan_list = [
    {"tanggal": "16-02-2025", "judul": "DPU Kampung Naga Garut", "deskripsi": "Kegiatan Dakwah Pengabdian Umat (DPU) di Kampung Naga Garut, bertujuan untuk memberikan pembinaan keagamaan, pendidikan, dan sosial kepada masyarakat setempat."},
    {"tanggal": "25-02-2025", "judul": "Workshop Web Development", "deskripsi": "Belajar membangun website modern dengan Laravel dan Tailwind."},
    {"tanggal": "10-03-2025", "judul": "Seminar AI dan Data Science", "deskripsi": "Membahas tren terbaru dalam kecerdasan buatan dan ilmu data bersama para pakar industri."},
    {"tanggal": "22-03-2025", "judul": "HMSI Hackathon 2025", "deskripsi": "Kompetisi coding 24 jam untuk menciptakan solusi inovatif di bidang teknologi."},
    {"tanggal": "05-04-2025", "judul": "Pelatihan UI/UX Design", "deskripsi": "Belajar dasar-dasar desain antarmuka dan pengalaman pengguna menggunakan Figma."},
    {"tanggal": "18-04-2025", "judul": "Company Visit ke Startup Teknologi", "deskripsi": "Kunjungan industri ke startup teknologi untuk memahami dunia kerja di bidang IT."},
    {"tanggal": "02-05-2025", "judul": "Pelatihan Cyber Security", "deskripsi": "Mempelajari dasar keamanan siber dan cara melindungi sistem dari serangan hacker."},
    {"tanggal": "20-05-2025", "judul": "Lomba CTF (Capture The Flag)", "deskripsi": "Kompetisi keamanan siber bagi mahasiswa untuk menguji keterampilan hacking etis."},
    {"tanggal": "07-06-2025", "judul": "Bootcamp Mobile App Development", "deskripsi": "Intensif pelatihan membangun aplikasi mobile dengan Flutter dan Firebase."},
    {"tanggal": "15-06-2025", "judul": "Pengabdian Masyarakat Digitalisasi UMKM", "deskripsi": "Membantu UMKM dalam transformasi digital dengan pembuatan website dan strategi online marketing."},
]

# Data untuk Publikasi
publikasi_data = [
    {"judul": "DPU di SMK Madka Iqlima II SI", "deskripsi": "Video DPU prodi SI 3", "gambar": "https://img.youtube.com/vi/wLWSGX6eKIM/hqdefault.jpg", "link": "https://youtu.be/wLWSGX6eKIM?si=xdT1U9ucZDOp_VUH"},
    {"judul": "Pelatihan Digital Desa Gandasoli", "deskripsi": "Rekaman workshop Machine Learning bersama pakar industri.", "gambar": "https://img.youtube.com/vi/Zt1mAjHJBXc/hqdefault.jpg", "link": "https://youtu.be/Zt1mAjHJBXc?si=yYTo-T7-J3KcCPWv"},
    {"judul": "ITM VISIT TO BOARDING SCHOOL", "deskripsi": "Dokumentasi kegiatan DPU IT Al-Muhajirin dalam mengabdi kepada masyarakat.", "gambar": "https://img.youtube.com/vi/sdYL3qur2JU/hqdefault.jpg", "link": "https://youtu.be/sdYL3qur2JU?si=ISJPglb3g6s32U9L"}
]


# Data untuk Dokumentasi
dokumentasi_data = [
    {"src": "doc1.jpg", "description": "Dokumentasi Kegiatan 1"},
    {"src": "doc2.jpg", "description": "Dokumentasi Kegiatan 2"},
    {"src": "doc3.jpg", "description": "Dokumentasi Kegiatan 3"},
    {"src": "doc4.jpg", "description": "Dokumentasi Kegiatan 4"},
    {"src": "doc5.jpg", "description": "Dokumentasi Kegiatan 5"},
    {"src": "doc6.jpg", "description": "Dokumentasi Kegiatan 6"},
    {"src": "doc7.jpg", "description": "Dokumentasi Kegiatan 7"},
    {"src": "doc8.jpg", "description": "Dokumentasi Kegiatan 8"},
    {"src": "doc9.jpg", "description": "Dokumentasi Kegiatan 9"},
    {"src": "doc10.jpg", "description": "Dokumentasi Kegiatan 10"},
    {"src": "doc11.jpg", "description": "Dokumentasi Kegiatan 11"},
    {"src": "doc12.jpg", "description": "Dokumentasi Kegiatan 12"},
]


@app.route('/')
def home():
    return render_template('index.html', berita=berita_list[:3], kegiatan=kegiatan_list[:3], publikasi=publikasi_data[:3], images=dokumentasi_data[:3])

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile')
def profile():
    return render_template('profile.html', pengurus=pengurus, divisi=divisi)

@app.route('/visi')
def visi():
    return render_template('visi.html')

@app.route('/berita')
def berita():
    return render_template('berita.html', berita=berita_list)

@app.route('/kegiatan')
def kegiatan():
    return render_template('kegiatan.html', kegiatan=kegiatan_list)

@app.route('/publikasi')
def publikasi():
    return render_template('publikasi.html', publikasi=publikasi_data)

@app.route('/dokumentasi')
def dokumentasi():
    return render_template('dokumentasi.html', images=dokumentasi_data)

if __name__ == '__main__':
    app.run(debug=True)
    