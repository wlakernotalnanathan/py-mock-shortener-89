import hashlib
def shorten(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]