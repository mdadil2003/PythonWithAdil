def main():
    
    try: # Try block to test code for errors
        a = int(input("Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally: # Finally block runs regardless of exceptions
        print("This block always executes.")
        
main()
