#Python Function to check whether the number lies in the range.

def test_range(n):
    if n in range(3,8):
        print(f"{n} is in the range")
    else:
        print(f"{n} is outside the range")


n = int(input("Enter the number: "))
test_range(n)

    