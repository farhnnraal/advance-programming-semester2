byteA = int(input("What is the first byte: "))
byteB = int(input("What is the second byte: "))

byteC = byteA & byteB
print(f"{byteA} & {byteB} = {byteC}")

byteC = byteA | byteB
print(f"{byteA} | {byteB} = {byteC}")


byteC = byteA ^ byteB
print(f"{byteA} ^ {byteB} = {byteC}")


byteC = ~byteA
print(f"~{byteA} = {byteC}")


byteC = byteA << byteB
print(f"{byteA} << {byteB} = {byteC}")


byteC = byteA >> byteB
print(f"{byteA} >> {byteB} = {byteC}")

