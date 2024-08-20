import caesar_cipher_art
print(caesar_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    encrypted_text=''
    for i in text:
        if i in alphabet:
            index=alphabet.index(i)+shift
            index%=len(alphabet)
            encrypted_text+=alphabet[index]
        else:
            encrypted_text+=i
    print(encrypted_text)
            
def decrypt(text,shift):
    decrypted_text=''
    for i in text:
        if i in alphabet:
            index=alphabet.index(i)-shift
            index=index%len(alphabet)
            decrypted_text+=alphabet[index]
        else:
            decrypted_text+=i
    print(decrypted_text)

def caesar(direction,text,shift):
    if direction=='encode':
        encrypt(text,shift)

    elif direction=='decode':
        decrypt(text,shift)

    else:
        print("INVALID DIRECTION !!!")

start_again='yes'
while start_again=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    start_again=input("Type 'yes' if you want to go again. Otherwise, type 'no':").lower()
    
        

        
    
    

    


                                
        
        
        
        
    
    

