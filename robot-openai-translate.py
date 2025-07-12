from openai import OpenAI

# MODEL = "qwen3:0.6b"
MODEL = "deepseek-r1:1.5b"
# MODEL = "deepcoder:1.5b"
# MODEL = "gemma3:1b"

PROMPT="""
From now on, you are a strict translation bot.
You must never answer, explain, or describe anything.
Only translate any English input I type into Simplified Chinese (简体中文).
❌ Do not answer questions.
❌ Do not explain.
❌ Do not reply in English.
✅ Only give me the direct Chinese translation.
✅ Only direct translate content to Chinese.

Example:

Input: Who are you? → Output: 您是谁？
Do not say who you are. Do not introduce yourself. Do not reply in any way except with the pure Chinese translation.
If I type "stop", go back to normal.
"""

messages=[{
    'role': 'system',
    'content': PROMPT
},{
    'role': 'user',
    'content': 'who are you?'
}]


ollama_client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = ollama_client.chat.completions.create(
    model=MODEL,
    messages=messages,
)

responseMessage = response.choices[0].message.content
# split the <think> and </think> to contentThink and content
contentThink = ""
content = ""
try:
    think_start_index = responseMessage.index('<think>') + len('<think>')
    think_end_index = responseMessage.index('</think>')
    contentThink = responseMessage[think_start_index:think_end_index].strip()
    content = responseMessage[think_end_index + len('</think>'):].strip()
except ValueError:
    content = responseMessage.strip()

# print the content
print("==== content =====")
print(content)
print("==== think =====")
print(contentThink)