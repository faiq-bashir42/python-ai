"""Task 1.8: City Care Bot - a chatbot for City Care Clinic that answers common questions,
hands complaints to a human, and counts the questions it could not answer."""

message_count = 0
unanswered = 0
complaints = 0

print("City Care Bot: Hi! Ask about timings, fees, location or appointments. Type 'bye' to exit.")

# Why ask here: the name is asked once before the loop, so it is not repeated every message.
name = input("City Care Bot: What is your name? ").strip().title()

# Why while True: we don't know how many messages the user will send,
# so the loop runs until we use break.
while True:
    # Why .strip().lower(): extra spaces and random capitals must not break our keyword checks.
    message = input(f"{name}: ").strip().lower()
    message_count += 1

    # Why first: an upset customer or a request for a human must never get a normal answer.
    if "human" in message or "agent" in message:
        print("City Care Bot: Connecting you to a human...")
        break
    elif "complain" in message or "problem" in message or "rude" in message or "is late" in message or "delay" in message:
        complaints += 1
        print("City Care Bot: Sorry about that. The clinic manager will call you today.")
    elif message == "bye":
        print(f"City Care Bot: Take care, {name}!")
        break
    # Why == and startswith: "hi" in "which" is True, so short words must not use "in".
    elif message == "hi" or message == "hello" or message.startswith("hey"):
        print(f"City Care Bot: Hello {name}! How can I help you?")
    elif "timing" in message or "open" in message or "hours" in message or "what time" in message:
        print("City Care Bot: We are open 10 am to 8 pm, Monday to Saturday.")
    elif "fee" in message or "price" in message or "cost" in message or "how much" in message:
        print("City Care Bot: Consultation fee is 2,000 PKR.")
    elif "where" in message or "location" in message or "address" in message:
        print("City Care Bot: We are on Main Boulevard, near City Mall.")
    elif "appointment" in message or "book" in message:
        print("City Care Bot: To book an appointment, please call our front desk.")
    elif "thank" in message:
        print(f"City Care Bot: You're welcome, {name}!")
    elif message == "":
        print("City Care Bot: Please type your question.")
    else:
        # Why count it: unanswered questions show the owner what to add next.
        unanswered += 1
        print(f"City Care Bot: I am not sure yet. In Module 2, an AI will answer: You are the friendly assistant of City Care Clinic. Answer in 2 lines: {message}")

print("========================================")
print(f"Chat summary: {message_count} messages, {unanswered} unanswered.")
print(f"Complaints received: {complaints}")