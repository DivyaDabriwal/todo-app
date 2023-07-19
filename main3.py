while True:
    user_input = input("Please input the country you are from : ")
    match user_input:
        case "USA":
            print("Hello")

        case "India":
            print("Namaste")

        case "Germany":
            print("Hallo")

        case "Spanish":
            print("Hola")

        case default:
            break
