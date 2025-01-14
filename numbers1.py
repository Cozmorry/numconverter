def words2number (words):
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    teens = {
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, 
        "eighteen": 18, "nineteen": 19
    }
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    multiples = {
        "hundred": 100, "thousand": 1000
        }
    words = words.lower().split()
    results = 0
    temp = 0
    for word in words: 
        if word in units:
            temp += units[word]
        elif word in teens:
            temp += teens[word]
        elif word in tens:
            temp += tens[word]
        elif word == "hundred":
            temp*= multiples[word]
            results += temp
            temp = 0
        elif word == "thousand":
            results += temp* multiples[word]
            temp = 0

    results += temp
    return results

input_text = input("Enter a number in words: ")
print (f"numeric form: {words2number(input_text)}")