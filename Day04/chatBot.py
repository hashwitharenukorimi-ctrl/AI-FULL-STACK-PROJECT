# import ollama
# msgs = []
# while True:
#     question = input("Ask question : ")
#     if question.lower() == "exit":
#         break
#     msgs.append(
#         {
#             "role" : "user",
#             "content" : question
#         }
#     )
#     response = ollama.chat(
#         model="llama3.2:3b",
#         messages=msgs
#     )
#     msgs.append(
#         {
#             "role" : "assistant",
#             "content":response["message"]["content"]
#         }
#     )
#     print("AI:",response["message"]["content"])




import ollama
msgs = [
    {
        "role" : "system",
        "content" : "Imagine you are human . give about this in 2 lines"
    }
]
while True:
    question = input("Ask question : ")
    if question.lower() == "exit":
        break
    msgs.append(
        {
            "role" : "user",
            "content" : question
        }
    )
    response = ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append(
        {
            "role" : "assistant",
            "content":response["message"]["content"]
        }
    )
    print("AI:",response["message"]["content"])
    print("-------Chat History---\n")
for msg in msgs:
    if msg["role"] == "system":
        break
    print(msg["role"], ":", msg["content"])
    