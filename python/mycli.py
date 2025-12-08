command = ""

while command != "quit":
    command = input("mycli> ")
    if command == "quit":
        print("== > got quit command, goodbye.")
    elif command != "":
        print(f"== > {command} is a nice command!")

