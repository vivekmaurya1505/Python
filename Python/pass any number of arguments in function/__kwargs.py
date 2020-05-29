def introduction(**data):
    print("\n Data type of arguments:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))
introduction(Firstname = "Vivek",Lastname = "Maurya",Age = 23, Phone = 1234567890)
