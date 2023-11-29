import hashlib


PUBLIC_KEY = '0e2ba4544d8ecd347abfa21da4335ae9'
PRIVATE_KEY = 'e6c514d2e6deb2476201d889420d4bfe7d97f8a2'
TS = "1"
TO_HASH = TS + PRIVATE_KEY + PUBLIC_KEY
HASHED = hashlib.md5(TO_HASH.encode())

MARVEL_DICT = {
    "PUBLIC_KEY": PUBLIC_KEY,
    "PRIVATE_KEY": PRIVATE_KEY,
    "TS": TS,
    "TO_HASH": TO_HASH,
    "HASHED": hashlib.md5(TO_HASH.encode()),
    "URL": "http://gateway.marvel.com/v1/public/" + "comics",
}


def get_marvel_params():
    return {
        "ts": MARVEL_DICT['TS'],
        "apikey": MARVEL_DICT['PUBLIC_KEY'],
        "hash": MARVEL_DICT['HASHED'].hexdigest(),
        "limit": "50",
        "offset": "0"
    }
