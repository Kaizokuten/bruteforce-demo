import time
import string

password = "demo"

charset = string.ascii_lowercase

def brute_force_visual(target):
    attempt = ""
    for i in range(len(target)):
        for char in charset:
            print(f"Essai pour la lettre {i+1} : {attempt + char}", end='\r')
            time.sleep(0.05)  
            if char == target[i]:
                attempt += char
                break
    print(f"\nMot de passe trouvé : {attempt}")

brute_force_visual(password)
