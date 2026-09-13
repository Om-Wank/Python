text = "   Python is powerful and Python is popular   "

text = text.strip()

text = text.replace("Python", "AI")

word = text.split()

print(len(word))

text = "-".join(word)

print(text.startswith("AI"))

print(text.endswith("popular"))