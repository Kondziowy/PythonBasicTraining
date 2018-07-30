try:
    int("text")
except ValueError as e:
    print(str(e))
finally:
    print("Parsing completed")