encrypted_password = hashlub.md5(password.encode())
hexadecimal_password = encrypted_password.hexdigest()
get_passwrod = firebase.get('/', username)
if(get_password != None):