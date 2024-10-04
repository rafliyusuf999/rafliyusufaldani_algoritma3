sa = int(input("sisi a: "))
sb = int(input("sisi b: "))
sc = int(input("sisi c: "))

if sa + sb > sc and sa + sc > sb and sb + sc > sa:
    if sa == sb == sc:
        print("Segitiga sama sisi")
    elif sa == sb or sa == sc or sb == sc:
        print("Segitiga sama kaki")
    elif sa**2 + sb**2 == sc**2 or sa**2 + sc**2 == sb**2 or sb**2 + sc**2 == sa**2:
        print("Segitiga siku-siku")
    else:
        print("Segitiga sembarang")
else:
    print("Segitiga tidak valid")
