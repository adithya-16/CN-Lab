def xordiv(data : int, key : int) -> int:
    dividend = data
    divisor = key
    i = 1
    while len(bin(dividend)) >= len(bin(key)):
        divisor = key << (len(bin(dividend)) - len(bin(key)))
        print("  " * i + bin(dividend)[2:])
        print("  " * i + bin(divisor)[2:])
        print(("  " * i) + ("--" * (len(bin(dividend)) - 2)))
        dividend ^= divisor
        i += 1
    print("  " * i + bin(dividend)[2:])
    return dividend

def encode(data : int, key : int) -> int:
    n1 = len(bin(key)) - 3
    dividend = data << n1
    rem = xordiv(dividend, key)
    n2 = len(bin(rem)) - 2
    suffix = '0' * (n1 - n2) + bin(rem)[2:] if rem else '0' * n1
    return int(bin(data)[2:] + suffix, 2) 

def decode(data : int, key : int) -> None:
    rem = xordiv(data, key)
    print(
        "The received word is correct and has no errors." if rem == 0 \
            else f"The received word has an error with remainder {bin(rem)[2:]}"
    )

data = int(input("Enter data to encode: "), 2)
p = int(input("Enter key: "), 2)
print("Encoded data word: ", bin(encode(data, p))[2:])
print()
response = int(input("Enter received data word: "), 2)
decode(response, p)
