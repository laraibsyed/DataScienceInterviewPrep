intput_str = "pythonisthebest"

def first_letter(str):
    temp_str = ""
    for letter in str:
        temp_str = temp_str + letter
        if temp_str.count(letter) > 1:
            return letter
    return None
    
print(first_letter(intput_str))    