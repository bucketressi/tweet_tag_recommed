import requests

data = {
  'grant_type': 'client_credentials'
}

response = requests.post('https://api.twitter.com/oauth2/token', data=data, auth=('c8G58hCAbUwpjzwZLmkqMHjSA', '5WoiG1ZnrX9NxUtdE2JhFXqFJYdF0JJiJZ5js10FR2R5CDYDF9'))
print(response)
print(response.json())