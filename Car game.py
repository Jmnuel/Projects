command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""
Start - To start the car
Stop - To stop the cara
quit - to quit 
""")
    elif command == "start":
        if started:
            print("The car already started!")
        else:
            started = True
            print("Engine starting...")
    elif command == "stop":
        if not started:
            print("The car already stopped!")
        else:
            started = False
            print("The car stop..")
    elif command == "quit":
        break
    else:
        print("Sorry, i don't understand..")

    
    