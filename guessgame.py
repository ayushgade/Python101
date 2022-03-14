secrt_word = "word"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guessess = False

while guess != secrt_word and not(out_of_guessess):
    if guess_count < guess_limit:
        guess = input("Enter the Secrt Word : ")
        guess_count += 1
    else:
        out_of_guessess = True 

if out_of_guessess:
    print("You Loss")
else:
    print("You Win")