from poster import posterize
import requests
from random import choice

header = posterize("Dad Jokes", "cyan")
print(header)

query = input("Let me tell you a joke!! Give me a word: ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": query}
)

data = response.json()["results"]

if len(data):
    print(f"I have {len(data)} jokes on {query}, Here is one of those:")
    joke = choice(data)["joke"]
    print(joke)
else:
    print(f"Sorry!!! I donot have any jokes on {query}. Try Again.")


