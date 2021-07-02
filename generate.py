import secrets
import string

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))

token = secrets.token_urlsafe(16)

print(f" {password} \n {token}")