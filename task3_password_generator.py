import string
import random 
def gen_password(length):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols="!@#$%^&*()_+"
    all=lowercase+uppercase+digits+symbols
    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    password+=random.choices(all,k=length-4)
    random.shuffle(password)
    return ''.join(password)
try:
    user_lenth=int(input("enter password lenth"))
    if user_lenth<4:
        print("lenth must be 4")
    else:
        final_password=gen_password(user_lenth)
        print("generated password:",final_password)    
except ValueError:
    print("enter valid number")



