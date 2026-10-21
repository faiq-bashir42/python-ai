"""Task 1.6: Prompt Cleaner - cleans a messy question, measures it, builds an AI prompt."""

price_per_1k = 0.5  # example price in PKR per 1,000 tokens

name = input("Your name: ")
question = input("Your question: ")

# Why .strip().title(): removes extra spaces and fixes random capitals in the name.
name = name.strip().title()
question = question.strip().capitalize()

# Stretch: hide a bad word before the question goes anywhere near the AI.
question = question.replace("stupid", "***")

characters = len(question)
# Why divide by 4: roughly 4 characters make 1 token in English text.
tokens = round(characters / 4)
cost = tokens / 1000 * price_per_1k

# Why .lower(): turns the text lowercase so "Python" and "PYTHON" are all found.
mentions_python = "python" in question.lower()

line = "========================================"
print(line)
print(f"Cleaned question: {question}")
print(f"Characters: {characters}, about {tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated cost: {cost:.2f} PKR")
print(line)

# Why [:150]: slicing keeps very long questions from making the prompt too big.
prompt = f"""You are a friendly Python tutor.
Greet {name} by name and answer in 3 short lines.
Question: {question[:150]}"""
print(prompt)