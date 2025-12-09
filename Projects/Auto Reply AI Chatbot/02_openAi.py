from openai import OpenAI  # pip install openai 
from google import genai # pip install google-genai

client = OpenAI(
  api_key="YOUR_API_KEY",
)

command = ''''
Mujhe ek aisa python function likh ke do jo ki ek list of numbers ko input le aur usme se sirf prime numbers ko return kare.
'''
completion = client.chat.completions.create(
   model= "gpt-3.5-turbo",   
   messages=[
       {"role": "system", "content": "You are a person named Adil who speaks hindi as well as english. He is from India and is coder. You analyze chat history and respond like Adil"},
       {"role": "user", "content": command} # user prompt
   ]
)

print(completion.choices[0].message.content)
