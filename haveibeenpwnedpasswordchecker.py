import hashlib
import requests

def getUserInputAndPrintResult():
    password_not_found = True
    word = input("Enter a password to check: ")
    word_sha1 = stringTosha1(word)
    result = contactPwnedAPI(word_sha1)
    password_hash_suffix = word_sha1[-35:].upper()
    hash_list = result.text.split()
    for line in hash_list:
        if line[:35]==password_hash_suffix:
            password_not_found = False
            print("password found: "+line[:-36] +" times in the database")
    if password_not_found:
        print("Password not found in database")
       
def contactPwnedAPI(password_hash):
 apiLink = "https://api.pwnedpasswords.com/range/"+password_hash[:5]
 return requests.get(apiLink)
    
def stringTosha1(m):
    hash = hashlib.sha1()
    hash.update(m.encode())
    return hash.hexdigest()
    
def main():
    getUserInputAndPrintResult()


if __name__ == '__main__': main()