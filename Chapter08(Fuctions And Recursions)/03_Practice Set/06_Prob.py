# 6. Write a python function which converts inches to cms.

def inches_to_cms(inches):
    return inches * 2.54
n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inches_to_cms(n)}")


# def cms_to_inches(cms):
#     return cms / 2.54
