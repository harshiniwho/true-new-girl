import urllib.request

import requests
from bs4 import BeautifulSoup

season_7_episodes = ["http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32808", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32809", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32810", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32811", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32812", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32813", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32814", "http://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=32511"]

def fetch_scripts():
    list_source = requests.get("https://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=7443")
    list_soup = BeautifulSoup(list_source.content, "html.parser")

    episode_links = list_soup.find_all("p")
    episodes = []
    for i in range(4, len(episode_links)-6):
        link = episode_links[i].find_all("a")
        if link:
            episodes.append(link[0]["href"])
    episodes.extend(season_7_episodes)
    print(len(episodes))
    return episodes


def fetch_episode_script():
    script_source = requests.get("https://transcripts.foreverdreaming.org/viewtopic.php?f=50&t=7445")
    script_soup = BeautifulSoup(script_source.content, "html.parser")
    dialogue_tags = script_soup.find_all("p")
    print(dialogue_tags)
    # print(dialogue_tags[2])

def main():
    fetch_scripts()
    # fetch_episode_script()

if __name__ == "__main__":
    main()