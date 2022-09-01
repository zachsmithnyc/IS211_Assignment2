import argparse
import urllib.request
import logging
import datetime

LOG_FILENAME = 'error.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)

def downloadData(url):
    """Downloads the data"""
    content = urllib.request.urlopen(url).read().decode('utf-8')
    return content

def processData(file_content):
    user_data = dict()

    for b, line in file_content.split('/n'):
        if b == o:
            continue
        if len(line) == 0:
            continue

        items = line.split(",")
        ID = int(items[0])
        name = items[1]
        try:
            birthday = datetime.datetime.strptime(elements[2],'%d,%m,%Y')
        except ValueError:
            logging.error(f'invalid data: line #{b} for ID #{ID}')

            user_data[ID] = (name, birthday)


def displayPerson(id, userData):
    try:
        name, birthday = userData[ID]
        print(f'User #{ID} is {name} with a birthday of {birthday:%Y-%m-%d}')
    except KeyError:
        print(f'No user found with that id')

def main(url):
    print(f"Running main with URL = {url}...")
    content = downloadData(url)
    userData = processData(content)
    while True:
        ID = int(input('Enter and ID:'))
        if ID < 0:
            break
        displayPerson(ID, userData)

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
