from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()
headers = {'User-Agent': ua.random}

def get_latest_matches():
    html = ""

    try:
        html = requests.get("https://www.fotmob.com/en/teams/9769/overview/gremio", headers=headers)
        html.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error Occured: {err}")
        return
    
    #with open("test_html.html", "w") as file:
    #    file.write(html.text)

    soup = BeautifulSoup(html.text, "lxml")

    #with open("test_html.html", "w") as file:
    #    file.write(soup.prettify())

    json_data_element = soup.find("script", id="__NEXT_DATA__")

    json_data = json.loads(json_data_element.text)
    
    json_formatted = json.dumps(json_data, indent=4)

    with open("test_json.json", "w") as file:
        file.write(json_formatted)

    #json_table = json_data["props"]["pageProps"]["fallback"]["team-9769"]["overview"]["table"][0]["data"]
    
    # gets recent matches
    recent_matches = json_data["props"]["pageProps"]["fallback"]["team-9769"]["overview"]["teamForm"]
    
    print(json.dumps(recent_matches, indent=4))


get_latest_matches()