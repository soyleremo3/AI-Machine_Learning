def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    get_input = input("Enter a string: ")
    print(convert(get_input))

main()