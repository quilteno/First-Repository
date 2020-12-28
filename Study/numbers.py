#  input what and output what
prompt = "I will repeat what you tell me:"
prompt += "\n type quit to exit."
while True:
    messege = input(prompt)
    if messege == 'quit':
        break
    else:
        print(messege)

