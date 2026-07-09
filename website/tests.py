def Validation():
    while True:
        try:
            text = input("please enter text: ").strip()
            
            if not text:
                raise ValueError("input is empty")
            
            if not text.isalpha():
                raise ValueError("Only letters are allowed.")
            
            print(text)
            break
            
        except ValueError as e:
            print(f"ValueError: {e}")

Validation()