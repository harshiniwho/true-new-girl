import datetime
import json
import os
import requests
import sys

SCRIPTS_LOCATION = ""
IMAGES_LOCATION = ""
INSERT_NEW_LINE_URL = "http://localhost:3900/api/subtitles"
INSERT_NEW_IMAGE_URL = "http://localhost:3900/api/images"

def load_scripts(filename):
    season = filename[:2]
    episode = filename[3:]
    payload = {
        "filename": filename,
        "season": season,
        "episode": episode
    }
    print("Season " + season + " episode " + episode)
    with open(SCRIPTS_LOCATION + filename, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = str(line)
            clean_line = clean_line.replace("\n", "")
            if clean_line:
                payload['subtitle'] = clean_line
                result = requests.post(INSERT_NEW_LINE_URL, json=payload, verify=False)
                if result.status_code != 200:
                    print("Failed to insert subtitle " + str(line))



def load_image_data(filename):
    print("Loading image data on file " + filename)
    with open(IMAGES_LOCATION + filename, 'r') as fp:
        data = json.load(fp)
        for d in data:
            response = requests.post(INSERT_NEW_IMAGE_URL, json=d, verify=False)
            if response.status_code != 200:
                print("error in loading details for filename " + d["filename"])
                print(response.content)

def main():
    files = os.listdir(SCRIPTS_LOCATION)
    for filename in files:
        load_scripts(filename)

    image_data_files = os.listdir(IMAGES_LOCATION)
    for filename in image_data_files:
        load_image_data(filename)


if __name__ == "__main__":
    main()
