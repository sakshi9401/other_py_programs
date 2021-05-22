#with open('poem.txt') as f:
f = open("poem.txt")
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkl is not present")
f.close()