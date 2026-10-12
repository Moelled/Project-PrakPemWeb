from flask import Flask

app = Flask(__name__)

@app.route('/profile')
def about():
    return ("Saya merupkan mahasiswa prodi informatika di Universitas Nahdlatul Ulama Yogyakarta. Memiliki ketertarikan dalam bidang cyeber security."
    "Saat ini saya sedang mengasah dan mengembangakan keterampilan di bidang tersebut.")
    

if __name__ == '__main__':
    app.run(debug=True)