with open("sample.txt") as f:
    content = f.read()

with open("poem.txt", "w") as f:
    f.write(content)