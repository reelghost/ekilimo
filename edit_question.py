import cloudscraper
import random
import base64
import csv
import login
import get_questions

def get_token():
    # get random username from csv file
    emails = []
    with open("acc.csv", "r", newline="") as f:
        reader = csv.reader(f)
        # Skip header if it exists
        next(reader, None)
        for row in reader:
            # Assuming email is the first column
            emails.append(row[0])
    token = login.login(random.choice(emails), "matako@1998")
    return token

def read_questions():
    with open("tz_farmers.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)

def get_random_question():
    with open("questions.txt", "r") as z:
        questions = z.readlines()
        return random.choice(questions)

def get_inspirobot_quote_image():

    # Step 1: Get image URL
    resp = scraper.get("https://dog.ceo/api/breeds/image/random").json()
    image_url = resp["message"]

    # Step 2: Download image
    img = scraper.get(image_url).content

    return base64.b64encode(img).decode("utf-8")


def edit_question(question_id):
    edit_url = f"https://ekilimo.kilimo.go.tz/gateway/ikmis-crop-management-service/api/v1/advisory-inquiry/id/{question_id}"

    # with open("test.png", "rb") as f:
    #     encoded = base64.b64encode(f.read()).decode("utf-8")

    edit_payload = {
        "region":random.randint(0,20),
        "district":random.randint(0,20),
        "wardId":random.randint(0,207),
        "villageId":random.randint(1,890),
        "advisoryGroupEnum":"ADVICE",
        # "description":get_random_question(),
        "photo": get_inspirobot_quote_image(),
        "name":"nyama choma",
    }
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-request-source": "web"
    }

    resp = scraper.put(edit_url, json=edit_payload, headers=headers)
    return resp.json().get("description")

if __name__ == "__main__":
    scraper = cloudscraper.create_scraper()
    get_questions.main()
    questions = read_questions()
    for question_id in questions:
        print(edit_question(question_id[0]))