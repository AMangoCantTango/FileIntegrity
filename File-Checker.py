import hashlib

def get_hash(name):
    with open(name, "rb") as file:
        content = file.read()

    hash_file = hashlib.sha256(content).hexdigest()

    return hash_file

original_hash = get_hash("important.txt")

with open("hashes.txt", "w") as file:
    file.write(original_hash)

new_hash = get_hash("important.txt")


if original_hash != new_hash:
    print("WARNING: File has been modified!")
else:
    print("File has not been modified.")