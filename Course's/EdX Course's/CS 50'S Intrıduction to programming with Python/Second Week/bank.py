get_input = input("Your Input: ")

get_input = get_input.lower().lstrip()

if get_input.startswith("hello"):
    print("$0")

elif get_input.startswith("h") and not get_input.startswith("hello"):
    print("$20")

else:
    print("$100")