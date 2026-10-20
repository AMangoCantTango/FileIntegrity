import hashlib

def get_hash(name):
    with open(name, "rb") as file:
        content = file.read()

    hash_file = hashlib.sha256(content).hexdigest()

    return hash_file


def main_menu():
     print("===== FILE INTEGRITY CHECKER =====")

     print("1. Save Original file hash")
     print("2. Check file integrity")
     print("3. Exit")

     choice = input("Enter your choice: ")
     return choice


while True:
    choice = main_menu()

    if choice == "1":
        print("Saving file hash...")
        original_hash = get_hash("important.txt")

        with open("hashes.txt", "w") as file:
            file.write(original_hash)

        print("File hash saved successfully!")

    elif choice == "2":
        print("Checking file integrity...")


        try:
            with open("hashes.txt", "r") as file:
                saved_hash = file.read()

        except FileNotFoundError:
            print("Error: A required file was not found!")
        else:

            try:  
                new_hash = get_hash("important.txt")
        
                if saved_hash != new_hash:
                    print("File has been modified!")
                else:
                    print("File has not been modified!")
            except FileNotFoundError:
                print("Error: important.txt cannot be found!")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid Choice!")
