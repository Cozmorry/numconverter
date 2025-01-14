from word2number import w2n
def wordstonumber (text):
    try: 
        return w2n.word_to_num(text)
    except ValueError as e:
        return f"Error: {e}"

input_in_words = input ("Enter a number in words: ")
print (f"{wordstonumber (input_in_words)}")