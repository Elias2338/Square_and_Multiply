#An algorithm to calculate x^e mod n

import math

def sam(x:int, e:int, n:int):
    if n == 0:      #x^e mod 0 -> Error
        return f"Error: Cant calculate {x}^{e} mod 0\nn = 0 results in a division by zero error."
    if e == 0:      #x^0 mod n = 1 mod n
        return 1 % n
    print(f"\n*********SQUARE AND MULTIPLY*********" \
    f"\ninserted values: x = {x}, e = {e} and n = {n}\n" \
    f"representing {x}^{e} mod {n}\n")
    print("In order to start the algorithm we need to convert the exponent into binary notation")
    e_bin = int_to_binary(e)
    print(f"{e} converted to binary -> {e_bin}\n\n"\
          "Starting the algorithm\n")
    result = 1
    #starting point of the algorithm
    for index in e_bin:     #iterating through the exponent in binary notation
        if index == "1":        #if the current index = 1 we calculate (result^2 * x) and set it as the new result
            print(f"1: calculate {result} ^ 2 mod {n}")
            result = ((result ** 2) * x) % n
            print(f"    ->{result}")

        else:       #if the current index = 1 we calculate (result^2) and set it as the new result
            print(f"0: calculate {result} ^ 2 mod {n}")
            result = (result ** 2) % n
            print(f"    ->{result}")
    print("\nIterated through all bits of the exponent and therefore finished the algorithm.\n" \
    f"*********{x}^{e} ≡ {result} mod {n}*********\n")
    return result



def int_to_binary(n:int):
    binary = ""
    bit_length = int(math.log(n, 2))
    for i in range(bit_length, -1, -1):
        if 2**i <= n:
            binary += "1"
            n -= 2**i
        else:
            binary += "0"

    return binary

print("\nCalculate x^e mod n\n")
i1 = int(input("Please enter the base x: "))
i2 = int(input("Please enter the exponent e: "))
i3 = int(input("Please enter the divisor n: "))
sam(i1, i2, i3)
