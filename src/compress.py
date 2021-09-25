import os

from PIL import Image

LOCATION = ""
BATCH_LOCATION = ""
BATCH = 100

def compress(file, batch):
    try:
        picutre = Image.open(LOCATION + "/" + file)
        new_file_name = file[:-4].replace(' ', '') + ".jpeg"
        picutre.convert('RGB').save(BATCH_LOCATION + str(batch) + "/" + new_file_name)
    except:
        print("Oops, not an image file...continuing")

def main():
    files = os.listdir(LOCATION)
    count = 1
    for file in files:
        compress(file, int(count/BATCH))
        if count%BATCH == 0:
            print("On batch " + str(count/BATCH))
        count = count + 1

if __name__ == "__main__":
    main()
