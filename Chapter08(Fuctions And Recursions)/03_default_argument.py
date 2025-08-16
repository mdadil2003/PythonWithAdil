# Default Argument
def goodDay(name, ending = "Thank you for your time!"):
    print("Good Day, " + name)
    print(ending)
    return "ok"
a = goodDay("Adil")
print(a)