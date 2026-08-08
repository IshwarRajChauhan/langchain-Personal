with open("data/mediumblog1.txt", "r", encoding="utf-16") as f:
    content = f.read()
with open("data/mediumblog1.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("Done — file converted to UTF-8")