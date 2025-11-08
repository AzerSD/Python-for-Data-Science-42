def all_thing_is_obj(object: any) -> int:
    # Print object type and return 42
    match object:
        case _ if isinstance(object, list):
            print(f"List : {type(object)}")
        case _ if isinstance(object, tuple):
            print(f"Tuple : {type(object)}")
        case _ if isinstance(object, set):
            print(f"Set : {type(object)}")
        case _ if isinstance(object, dict):
            print(f"Dict : {type(object)}")
        case _ if isinstance(object, str):
            print(f"{object} : {type(object)}")
        case _:
            print("Type not found")
    return 42
