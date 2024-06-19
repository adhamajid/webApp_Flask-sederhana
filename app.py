from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    if request.method == 'POST':
        bilangan1 = float(request.form['bilangan1'])
        bilangan2 = float(request.form['bilangan2'])
        operasi = request.form['operasi']

        if operasi == 'tambah':
            hasil = bilangan1 + bilangan2
        elif operasi == 'kurang':
            hasil = bilangan1 - bilangan2
        elif operasi == 'kali':
            hasil = bilangan1 * bilangan2
        elif operasi == 'bagi':
            hasil = bilangan1 / bilangan2
        else:
            hasil = 'Operasi tidak valid'

        return render_template('hasil.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
