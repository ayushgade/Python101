def translate(prase):
    translation = ""
    # here we are saying in 
    for letter in prase:
        if letter in "AEIOUaeiou":
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input("enter the prase : ")))