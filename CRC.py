def xor(a, b):
    """XOR two binary strings (skip first bit)."""
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))


def crc_divide(data, divisor):
    """Perform CRC division and return remainder."""
    pick = len(divisor)
    tmp = data[:pick]
    
    for i in range(pick, len(data)):
        tmp = (xor(divisor, tmp) if tmp[0] == '1' else xor('0' * pick, tmp)) + data[i]
    
    return xor(divisor, tmp) if tmp[0] == '1' else xor('0' * pick, tmp)


# Sender side
dataword = input("Enter dataword (binary): ")
generator = input("Enter generator (binary): ")

remainder = crc_divide(dataword + '0' * (len(generator) - 1), generator)
codeword = dataword + remainder

print(f"CRC bits: {remainder}")
print(f"Codeword: {codeword}")

# Receiver side
received = input("\nEnter received codeword: ")
check = crc_divide(received, generator)

print("Error detected!" if '1' in check else "No error. Valid codeword.")
