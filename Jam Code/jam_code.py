import hashlib

hash_data_string = '021&20160512063343&48142&7461&00824023&4745-****-****-3452&01&10&'
security_key = 'abcdefghijklmnop'
trailing = ''
final_string = (hash_data_string +
                security_key + trailing).encode(encoding='UTF-16', errors='ignore')

digest = hashlib.md5()
digest.update(final_string)
print(digest.hexdigest())


digest = hashlib.sha1()
digest.update(final_string)
print(digest.hexdigest())

digest = hashlib.sha256()
digest.update(final_string)
print(digest.hexdigest())

digest = hashlib.sha512()
digest.update(final_string)
print(digest.hexdigest())

digest = hashlib.sha224()
digest.update(final_string)
print(digest.hexdigest())

digest = hashlib.sha384()
digest.update(final_string)
print(digest.hexdigest())
