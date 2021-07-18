import urllib.request

import requests
from bs4 import BeautifulSoup

# url constants
WIKI_BASE_URL = "https://newgirl.fandom.com/wiki"
CHARACTERS_ENDPOINT = "/Category:Characters"
CHARACTER_TEMPLATE = "/{}"


def fetch_characters():
    print("fetch all characters")
    characters = set()
    character_page_source = requests.get(WIKI_BASE_URL + CHARACTERS_ENDPOINT)
    characters_soup = BeautifulSoup(character_page_source.content, "html.parser")
    characters_tags = characters_soup.find_all("img", class_="category-page__member-thumbnail")
    for characters_tag in characters_tags:
        characters.add(characters_tag["alt"])
    return characters


def fetch_character_image(character):
    print("fetch source for  "+ character)
    character_source = requests.get(WIKI_BASE_URL + '/' + character)
    if character_source.status_code != 200:
        return
    soup = BeautifulSoup(character_source.content, "html.parser")
    results = soup.find_all("img", class_="pi-image-thumbnail")
    print(results)
    if results.__len__() > 0:
        print("Downloading image for " + character)
        urllib.request.urlretrieve(results[0]["src"], f"../character-images/{character}.jpg")


def main():
    characters = fetch_characters()
    for character in characters:
        fetch_character_image(character)


if __name__ == "__main__":
    main()
