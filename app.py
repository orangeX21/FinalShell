from flask import Flask, request, render_template
import hashlib
from Crypto.Hash import keccak

app = Flask(__name__)

def md5_hash(msg):
    md5 = hashlib.md5()
    md5.update(msg.encode('utf-8'))
    return md5.hexdigest()

def keccak384_hash(msg):
    keccak_hash = keccak.new(digest_bits=384)
    keccak_hash.update(msg.encode('utf-8'))
    return keccak_hash.hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        high_edition_md5 = md5_hash("61305" + code + "8552")[8:24]
        pro_edition_md5 = md5_hash("2356" + code + "13593")[8:24]
        high_edition_keccak = keccak384_hash(code + "hSf(78cvVlS5E")[12:28]
        pro_edition_keccak = keccak384_hash(code + "FF3Go(*Xvbb5s2")[12:28]

        return render_template('index.html', code=code,
                               high_edition_md5=high_edition_md5,
                               pro_edition_md5=pro_edition_md5,
                               high_edition_keccak=high_edition_keccak,
                               pro_edition_keccak=pro_edition_keccak)
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='::', port=5000, debug=True)