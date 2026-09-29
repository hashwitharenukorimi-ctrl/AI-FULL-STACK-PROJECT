import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"Explain ai in 2-3 lines and three main types of ai in bullet points"
        }
    ]
)
print(response["message"]["content"])