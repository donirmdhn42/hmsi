from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/visi')
def visi():
    return render_template('visi.html')

@app.route('/kegiatan')
def kegiatan():
    return render_template('kegiatan.html')

@app.route('/publikasi')
def publikasi():
    return render_template('publikasi.html')

@app.route('/dokumentasi')
def dokumentasi():
    return render_template('dokumentasi.html')

if __name__ == '__main__':
    app.run(debug=True)
