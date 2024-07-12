import requests
import pandas as pd



url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"abc","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"x-rapidapi-key": "00c35e2c67msh00838e000dadc55p1e4578jsn56ca8d17f9bc",
	"x-rapidapi-host": "spotify23.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
  

data = response.json()

# df = pd.DataFrame.from_dict(data,orient='columns')
print(data)
df = pd.json_normalize(data['albums']['items'], max_level=100)
df.to_csv("data.csv")
