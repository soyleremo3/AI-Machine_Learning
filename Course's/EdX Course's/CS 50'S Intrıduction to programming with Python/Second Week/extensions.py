get_input = input("Give me a file name: ")

get_input = get_input.strip().lower()

if get_input.endswith(".gif"):
    print("image/gif")
elif get_input.endswith(".jpg") or get_input.endswith(".jpeg"):
    print("image/jpeg")
elif get_input.endswith(".png"):
    print("image/png")
elif get_input.endswith(".pdf"):
    print("application/pdf")
elif get_input.endswith(".txt"):
    print("text/plain")
elif get_input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")