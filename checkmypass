import requests
import hashlib
import sys
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}, check the api and check again.')
    return res
def pwned_api_check(password):
    #check password if it exsist in the API response
    password = str(password)
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1password[0:5]
    tail = sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response ,tail)
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def main(args):
    for password in args:
        count = int(pwned_api_check(password))
        if count > 0 :
            print(f'{password} was found for {count} times.... You shall change it!')
        else:
            print(f'{password} was NOT found, Carry On!')
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
