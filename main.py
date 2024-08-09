import hashlib
from Crypto.Hash import keccak
import getpass


def md5_hash(msg):
    md5 = hashlib.md5()
    md5.update(msg.encode('utf-8'))
    return md5.hexdigest()


def keccak384_hash(msg):
    keccak_hash = keccak.new(digest_bits=384)
    keccak_hash.update(msg.encode('utf-8'))
    return keccak_hash.hexdigest()


def main():
    code = getpass.getpass("输入机器码: ")
    print("版本号 < 3.9.6 (旧版)")
    try:
        high_edition_md5 = md5_hash("61305" + code + "8552")[8:24]
        pro_edition_md5 = md5_hash("2356" + code + "13593")[8:24]
        print("高级版:", high_edition_md5)
        print("专业版:", pro_edition_md5)
    except Exception as e:
        print("Error generating MD5 hashes:", e)

    print("版本号 >= 3.9.6 (新版)")
    try:
        high_edition_keccak = keccak384_hash(code + "hSf(78cvVlS5E")[12:28]
        pro_edition_keccak = keccak384_hash(code + "FF3Go(*Xvbb5s2")[12:28]
        print("高级版:", high_edition_keccak)
        print("专业版:", pro_edition_keccak)
    except Exception as e:
        print("Error generating Keccak-384 hashes:", e)


if __name__ == "__main__":
    main()
