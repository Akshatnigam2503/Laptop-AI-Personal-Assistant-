from openai import OpenAI
from config import apikey
client = OpenAI(api_key=apikey)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an email to my boss for resignation\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)


'''
Completion(id='cmpl-8wua8lLSu7ZdCTq4TfTXKjgLrl7Q9',

choices=
[CompletionChoice(
finish_reason='length',
index=0,
logprobs=None,
text="\nSubject: Notice of Resignation\n\nDear [Boss's Name],\n\nI am writing to tender my resignation from my current position at [Company Name]. After much consideration and deliberation, I have decided to move on and pursue other career opportunities. Therefore, I will be resigning from my position as [Position] effective [Date].\n\nI would like to take this opportunity to express my sincere gratitude for the support and guidance you have provided me during my time here at [Company Name]. It has been a pleasure working with such a dedicated and supportive team. I am grateful for the learning and growth opportunities that this role has offered me, and I appreciate the trust and confidence you have placed in me.\n\nI assure you that I will do everything in my power to ensure a smooth transition during my remaining time at the company. I am committed to completing all my current projects and tasks and will do my best to assist in finding and training a suitable replacement.\n\nKindly let me know if there is anything specific you would like me to do before my last day. I am more than happy to help in any way I can.\n\nI would like to take this opportunity to thank you for being a fantastic boss and for being supportive of my career development. I will always have the utmost respect")],

created=1709051216,
model='gpt-3.5-turbo-instruct',
object='text_completion', system_fingerprint=None,
usage=CompletionUsage(
completion_tokens=256,
prompt_tokens=9,
total_tokens=265)
)

'''