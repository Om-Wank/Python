text = "   I am learning Python for AI   "
text =text.strip()
text =text.replace("Python","Python Programming")
text = text.split()
print(len(text))
word ="_".join(text)
print(word.startswith("I"))
print(word.endswith("AI"))