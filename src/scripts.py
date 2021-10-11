import urllib.request
import re
import requests
from bs4 import BeautifulSoup

SCRIPT_LOCATION = ""

leftout_season_6_episodes = ["http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32801", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32802", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32803", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32806", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32807"]
season_7_episodes = ["http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32808", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32809", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32810", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32811", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32812", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32813", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32814", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32511"]


def fetch_scripts():
    list_source = requests.get("https://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=7443", verify=False)
    list_soup = BeautifulSoup(list_source.content, "html.parser")

    episode_links = list_soup.find_all("p")
    episodes = []
    for i in range(4, len(episode_links)-6):
        link = episode_links[i].find_all("a")
        if link:
            episodes.append(link[0]["href"])
    episodes.extend(leftout_season_6_episodes)
    episodes.extend(season_7_episodes)
    print(len(episodes))
    return episodes


def remove_actions(tag):
    while("<em>" in tag):
        start = tag.find("<em>")
        end = tag.find("</em>")
        tag = tag[0: start:] + tag[end + 5::]
    return tag


def clean_script_line(tag):
    tag = tag[3:-4]
    clean_tag = remove_actions(tag)
    return clean_tag

# testing with: <p>NICK: <em>(With hands over his hears, shouting over Caroline)</em> I can't hear you, that means we're not breaking up! We can't break up if I can't hear you! No! La, la, la, la, la, la, la, la!</p>

def separate_character_dialogue(clean_tag):
    if (clean_tag.find(":")):
        colon = clean_tag.find(":")
        return clean_tag[:colon], clean_tag[colon+1:]

# <title>01x01 - Pilot - New Girl Transcripts - Forever Dreaming</title>
def extract_episode_season(episode_title):
    episode_title = episode_title[7:]
    season = episode_title[:2]
    episode_title = episode_title[3:]
    episode = episode_title[:2]
    return episode, season

def fetch_episode_script(script_link):
    # script_link = "https://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=7445"
    check_special_character = re.compile('[@#%^*<>/\|~:=]')
    script_source = requests.get(script_link, verify=False)
    script_soup = BeautifulSoup(script_source.content, "html.parser")
    episode_title = script_soup.find("title")
    episode, season = extract_episode_season(str(episode_title))
    print("Season " + season + " Episode " + episode)
    dialogue_tags = script_soup.find_all("p")
    with open(SCRIPT_LOCATION + season + "-" + episode, "w", encoding="utf-8") as f:
        for tag in dialogue_tags:
            clean_tag = clean_script_line(str(tag))
            f.write(clean_tag)
            f.write('\n')


def new_fetch_script():
    script_link = "https://subslikescript.com/series/New_Girl-1826940/season-2/episode-10-Bathtub"
    script_source = requests.get(script_link, verify=False)
    script_soup = BeautifulSoup(script_source.content, "html.parser")
    with open("test.csv", "w", encoding="utf-8") as f:
        f.write(str(script_soup))

def main():
    # new_fetch_script()
    episodes = fetch_scripts()
    for episode in episodes:
        try:
            fetch_episode_script(episode)
        except Exception as e:
            print(e)
            print("missing an episode here...")

if __name__ == "__main__":
    main()
