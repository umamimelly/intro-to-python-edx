#write the question asking for the answer of the life, universe, and everything

whatis = input("What is the answer to life, the universe, and everything? ")

if whatis.casefold() == "forty two":
    print("Yes")
elif whatis.casefold() == "forty-two":
    print("Yes")
elif whatis == "42":
    print("Yes")
else: print("No")
