import requests

def person_intelligence(response, necessary_person):
  for person in response.json():
    if person["name"] == necessary_person:
      return {person["name"] : person["powerstats"]["intelligence"]}

response = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')

necessary_persons = {}
necessary_persons.update(person_intelligence(response, 'Hulk'))
necessary_persons.update(person_intelligence(response, 'Captain America'))
necessary_persons.update(person_intelligence(response, 'Thanos'))

print(min(necessary_persons))
