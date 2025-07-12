from ollama import Client

MODEL = "qwen3:0.6b"
MODEL = "deepseek-r1:1.5b"


client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'same-value'}
)

messages=[
    {
        'role': 'user',
        'content': 'Who are you?'
    }]


response = client.chat(model=MODEL, messages=messages,
    think=False,
    # temperature=0.7,
    # top_p=0.8,
    # top_k=20,
    # max_tokens=8192,
    # presence_penalty=1.5,
    # chat_template_kwargs={"enable_thinking": False
)

print(response['message']['content'])


# print('Thinking:\n========\n\n' + response.message.thinking)
# print('\nResponse:\n========\n\n' + response.message.content)
