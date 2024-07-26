def test(data,index):
    try:
        result = data[index]
        print("result: ",result)
    except IndexError:
        print("Error: Index out of range")


num = [1,2,3,4,5,6,7,8,9,10]

index = int(input("Enter the index: "))

test(num,index)