from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

print("AI Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    try:
        response = client.chat.completions.create(
            model="inclusionai/ling-3.2-flash:free",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        print("\nAI:", response.choices[0].message.content)
        print()

    except Exception as e:
        print("\nError:", e)
        print("Try again in a few minutes or switch models.\n")