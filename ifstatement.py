is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("your are short")
elif not(is_male) and is_tall:
    print("your are short")
else:
    print("Your are nither")