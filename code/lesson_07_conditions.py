"""Task 1.7: Smart Model Router - picks the right AI model and estimates the cost."""

# Why .strip().lower(): so " Code " and "CODE" both match "code" below.
task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

# Example prices in PKR per 1K tokens (not real prices).
if task == "code":
    model = "claude (cloud, strong at code)"
    price = 0.8
elif task == "private":
    model = "llama3.2 (local, Ollama)"
    # Why 0: a local model runs on our own computer, so there is no per-token fee.
    price = 0
else:
    model = "gemini-flash (cloud, cheap)"
    price = 0.2

cost = tokens / 1000 * price

if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")

# Stretch: free users can't send long requests.
paid = input("Is this a paid user? (yes/no): ").strip().lower()
if paid == "no" and tokens > 2000:
    print("Upgrade to send long requests.")