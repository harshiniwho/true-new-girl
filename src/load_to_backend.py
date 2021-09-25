import os
import requests

LOCATION = ""
INSERT_NEW_LINE_URL = "/api/subtitles"

def load_scripts(filename):
    season = filename[:2]
    episode = filename[3:]
    payload = {
        "filename": filename,
        "season": season,
        "episode": episode
    }
    print("Season " + season + " episode " + episode)
    with open(LOCATION + filename, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = str(line)
            clean_line = clean_line.replace("\n", "")
            if clean_line:
                payload['subtitle'] = clean_line
                result = requests.post(INSERT_NEW_LINE_URL, json=payload, verify=False)
                if result.status_code != 200:
                    print("Failed to insert subtitle " + str(line))


def main():
    files = os.listdir(LOCATION)
    for filename in files:
        load_scripts(filename)


if __name__ == "__main__":
    main()