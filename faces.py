#return/replace emoticons with emojis. hello 🙂 goodbye 🙁
#userinp = input()
#if userinp == "Hello :)":
#    print("Hello 🙂")
#if userinp == "Goodbye :(":
#    print("Goodbye 🙁")
#if userinp == "Hello :) Goodbye :(":
#    print("Hello 🙂 Goodbye 🙁")


#less verbose

userinp = input()
print(userinp.replace(':)', '🙂').replace(':(', '🙁'))
