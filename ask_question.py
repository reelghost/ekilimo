import cloudscraper
import random
import csv
import login


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
    
def ask_question(swali):
    ques_url = "https://ekilimo.kilimo.go.tz/gateway/ikmis-crop-management-service/api/v1/advisory-inquiry"
    payload = {
        "region":random.randint(0,20),
        "district":random.randint(0,20),
        "wardId":random.randint(0,207),
        "villageId":random.randint(1,890),
        "advisoryGroupEnum":"ADVICE",
        "description":f"{swali}😪",
    }
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-request-source": "web"
    }

    resp = scraper.post(ques_url, json=payload, headers=headers)
    return resp.json().get("description")

if __name__ == "__main__":
    scraper = cloudscraper.create_scraper()
    
    swali = "Tutapata lini mtaji?"
    print(ask_question(swali))