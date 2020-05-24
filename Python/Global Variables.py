x = 'Hi'
def read_x():
    print(x) # x is just referenced, therefore assumed global

read_x() # prints Hi


def read_y():
    y = 'Hey' # y appears in an assignment, therefore it's local
    print(y) # will find the local y
read_y() # prints Hey
def read_x_local_fail():
    if False:
        x = 'Hey' # x appears in an assignment, therefore it's local
        print(x) # will look for the _local_ z, which is not assigned, and will not be found
read_x_local_fail() # UnboundLocalError: local variable 'x' referenced before assignment


x = 5
print(x) # out: 5
del x
print(x) # NameError: name 'f' is not defined
