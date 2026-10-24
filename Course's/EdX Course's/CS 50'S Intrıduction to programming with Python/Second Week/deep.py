get_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

get_input = get_input.strip().lower()

if get_input == "42" or get_input == "forty-two" or get_input == "forty two" or get_input == "FORTY TWO" or get_input == "Forty-Two":
    print("Yes")
else:
    print("No")