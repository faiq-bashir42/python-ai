"""Task 1.5: AI Model Profile Card - shows a model's details and a cost estimate."""

model_name = "llama3.2"      # str
context_window = 128000      # int
price_per_1k = 0.5           # float (example price in PKR)
runs_locally = True          # bool

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k} PKR {type(price_per_1k)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# Why int(): input() returns text, and we can't do maths on text.
tokens = int(input("Tokens per chat: "))

# Why / 1000: the price is per 1,000 tokens, not per single token.
cost = round(tokens / 1000 * price_per_1k, 2)
print(f"Estimated cost: {cost} PKR")

# Stretch: monthly cost (30 days)
chats_per_day = int(input("Chats per day: "))
print(f"Estimated monthly cost: {round(cost * chats_per_day * 30, 2)} PKR")