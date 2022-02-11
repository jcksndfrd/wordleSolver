def checkdataIsOneLetter(data):
    if len(data) == 1 and data.isalpha():
        return True
    return False

def checkArrayElementsAreEqual(data):
    for item in data:
        if item != data[0]:
            return False
    return True