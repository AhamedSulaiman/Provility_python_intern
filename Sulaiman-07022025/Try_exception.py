x=10
try:
    print(x)
    try:
        print(y)
    except NameError:
        print("There is no variable y")
    except:
        print("Something went wrong")
    finally:
        print("Successfully executed")
except:
    print("Error")