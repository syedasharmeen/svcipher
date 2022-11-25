
vowel_A="abcd"
letter_to_index_groupA=dict(zip(vowel_A,range(len(vowel_A))))
index_to_letter_group_A=dict(zip(range(len(vowel_A)),vowel_A))


vowel_E="efgh"
letter_to_index_groupE=dict(zip(vowel_E,range(len(vowel_E))))
index_to_letter_group_E=dict(zip(range(len(vowel_E)),vowel_E))


vowel_I="ijklmn"
letter_to_index_groupI=dict(zip(vowel_I,range(len(vowel_I))))
index_to_letter_group_I=dict(zip(range(len(vowel_I)),vowel_I))


vowel_O="opqrst"
letter_to_index_groupO=dict(zip(vowel_O,range(len(vowel_O))))
index_to_letter_group_O=dict(zip(range(len(vowel_O)),vowel_O))


vowel_U="uvwxyz"
letter_to_index_groupU=dict(zip(vowel_U,range(len(vowel_U))))
index_to_letter_group_U=dict(zip(range(len(vowel_U)),vowel_U))

# vowel_sp=" &*$#@.%"
# letter_to_index_groupsp=dict(zip(vowel_sp,range(len(vowel_sp))))
# index_to_letter_group_sp=dict(zip(range(len(vowel_sp)),vowel_sp))

def encrypt(message,shift=-3):
    cipher=""
      

    for letter in message:
        if(letter in vowel_A):
            letter_to_index=letter_to_index_groupA
            index_to_letter=index_to_letter_group_A
        elif(letter in vowel_E):
            letter_to_index=letter_to_index_groupE
            index_to_letter=index_to_letter_group_E
        elif(letter in vowel_I):
            letter_to_index=letter_to_index_groupI
            index_to_letter=index_to_letter_group_I
        elif(letter in vowel_O):
            letter_to_index=letter_to_index_groupO
            index_to_letter=index_to_letter_group_O
        # elif(letter in vowel_sp):
        #     letter_to_index=letter_to_index_groupsp
        #     index_to_letter=index_to_letter_group_sp
        else:
            letter_to_index=letter_to_index_groupU
            index_to_letter=index_to_letter_group_U
        number=(letter_to_index[letter] + shift) % len(letter_to_index)
        letter=index_to_letter[number]
        cipher+=letter
    
    return cipher


def decrypt(cipher,shift=-3):
    decrypted=""
      

    for letter in cipher:
        if(letter in vowel_A):
            letter_to_index=letter_to_index_groupA
            index_to_letter=index_to_letter_group_A
        elif(letter in vowel_E):
            letter_to_index=letter_to_index_groupE
            index_to_letter=index_to_letter_group_E
        elif(letter in vowel_I):
            letter_to_index=letter_to_index_groupI
            index_to_letter=index_to_letter_group_I
        elif(letter in vowel_O):
            letter_to_index=letter_to_index_groupO
            index_to_letter=index_to_letter_group_O
        # elif(letter in vowel_sp):
        #     letter_to_index=letter_to_index_groupsp
        #     index_to_letter=index_to_letter_group_sp
        else:
            letter_to_index=letter_to_index_groupU
            index_to_letter=index_to_letter_group_U
        number=(letter_to_index[letter] - shift) % len(letter_to_index)
        letter=index_to_letter[number]
        decrypted+=letter
    
    return decrypted




def main():

    message=input("Enter plain text: ")

    # fin=len(message)
    # shift=(random.randint(1,10)+fin)%34

    cipher=encrypt(message.lower(),shift=3)
    print("        ")

    print("Cipher Text: " , cipher)
    print("        ")
    
    plaintext=decrypt(cipher,shift=3)


    if(message==message.upper()):
        print("Decrypted Text: " ,plaintext.upper())
    else:

        print("Decrypted Text: " , plaintext)
     

main()
print(" ")

