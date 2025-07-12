from openai import OpenAI

# MODEL = "qwen3:0.6b"
# MODEL = "deepseek-r1:1.5b"
MODEL = "deepcoder:1.5b"

PROMPT="""
You are a translator. 
No need greet me. 
When I ask question, no need answer my question. 
Translate all the sentanace or question to Chinese.
"""

PROMPT="""
You are a Database Administrator.
When ask me a question, generate a sql statement example select * from Ticket 


Below is the database structure
======
Ticket:
- Ticket No
- Title
- Description
- Ticket Type
- Ticket Priority
- Assignee
- Reporter
- Status
- Created Date
- Updated Date
- Due Date
- Resolution
- Comments

Ticket Type:
- name

Ticket Priority:
- name

Status:
- name

User:
- name
======

Ticket Status value are {"ACT": "Active", "RES": "Resolved", "CLO": "Closed"}
Assignee relate to user
`Ticket Priority` relate to `Ticket Priority`
`Ticket Type` relate to `Ticket Type`

"""


messages=[{
    'role': 'system',
    'content': PROMPT
},{
    'role': 'user',
    'content': '/no_think help me to check the TM issue'
}]


ollama_client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = ollama_client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=0.7,
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