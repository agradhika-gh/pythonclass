userRequest = int(input("Enter your Grade: "))

def mytable(table):
    for i in range(1,11,1):
        result = table * i
        print(f"{table} * {i} = {result}")


mytable(userRequest)
