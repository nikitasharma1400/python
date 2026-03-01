import random
import string

def gen_pass():
   
    length = int(input("how long do ya want the password? "))
    
    
    chars = string.ascii_letters + string.digits + string.punctuation
    
    
    password = "".join(random.choice(chars) for i in range(length))
    
    print(f"yer new password is: {password}")


gen_pass()