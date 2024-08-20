from textblob import TextBlob

def correct_grammar(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)

text = input("Enter yout Sentence: ")
corrected_text = correct_grammar(text)
print("Corrected text: ", corrected_text)