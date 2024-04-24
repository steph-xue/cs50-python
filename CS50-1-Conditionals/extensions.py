# The "extensions" program allows the user to input the name of the file and prints out the file's media type

def main():

    # Gets user to input the name of the file
    file = input("File name: ").strip().lower()

    # Prints out the file's media type
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
