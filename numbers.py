from word2number import w2n
def words_to_number(text):
    try: 
        return w2n.word_to_num(text)
    except ValueError as e:
        return f"Error: {e}"

input_in_words = input("Enter a number in words: ")
print(f"Number: {words_to_number(input_in_words)}")