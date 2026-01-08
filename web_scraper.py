from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()
headers = {'User-Agent': ua.random}

def get_gremio_data():
    html = ""

    try:
        html = requests.get("https://www.fotmob.com/en/teams/9769/overview/gremio", headers=headers)
        html.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error Occured: {err}")
        return

    soup = BeautifulSoup(html.text, "lxml")

    json_data_element = soup.find("script", id="__NEXT_DATA__")
    json_data = json.loads(json_data_element.text)
    #json_formatted = json.dumps(json_data, indent=4)
    #json_table = json_data["props"]["pageProps"]["fallback"]["team-9769"]["overview"]["table"][0]["data"]

    return json_data

def get_latest_matches():
    # gets recent matches
    recent_matches = get_gremio_data()["props"]["pageProps"]["fallback"]["team-9769"]["overview"]["teamForm"]
    
    return recent_matches

def format_match_results(recent_matches):
    for k in recent_matches:
        match k["resultString"]:
            case "W":
                print(f"venceu! ({k['tooltipText']['homeTeam']} {k['tooltipText']['homeScore']} x {k['tooltipText']['awayScore']} {k['tooltipText']['awayTeam']})")
            case "L":
                print(f"perdeu! ({k['tooltipText']['homeTeam']} {k['tooltipText']['homeScore']} x {k['tooltipText']['awayScore']} {k['tooltipText']['awayTeam']})")
        


#print(get_latest_matches())
format_match_results(get_latest_matches())