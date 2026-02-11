text = "  Hello, World! Welcome to Python Programming.  "
cleaned_text = text.strip()
all_words = cleaned_text.split(" ")
print("The text with the leading and trailing spaces removed:", cleaned_text)
print("The number of words in the text is:", len(all_words))
new_text = ""
for c in all_words:
    capital = c.title()
    new_text += capital + " "
print("The text with each word capitalized is:", new_text)
print("The stripped string starts with 'Hello':", cleaned_text.startswith("Hello"))
print("The stripped string ends with 'ing':", cleaned_text.endswith("ing."))
print("The position (index) of the word 'Python' in the stripped string is:", cleaned_text.find("Python"))
print(" - ".join(all_words))

