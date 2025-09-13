a = "a very long string with emails"

email = []

import email


for word in a.split():
    if "@" in word:
        email.append(word)
        if "." in word:
            email.append(word)
            print(email)
            