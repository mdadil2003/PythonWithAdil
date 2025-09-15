a = "Contact me at test@example.com for details."

emails = []

for word in a.split():
    if "@" in word and "." in word:
        emails.append(word)

print(emails)