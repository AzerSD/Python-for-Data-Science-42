def NULL_not_found(object: any) -> int:
    try:
        match object:
            case None:
                print(f"Nothing: {object} {type(object)}")
            case _ if type(object) is float and object != object:
                print(f"Cheese: nan {type(object)}")
            case False:
                print(f"Fake: {object} {type(object)}")
            case 0:
                print(f"Zero: {object} {type(object)}")
            case "":
                print(f"Empty: {type(object)}")
            case _:
                print("Type not Found")
                return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    return 0
