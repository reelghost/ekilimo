import cloudscraper
from faker import Faker
import csv




def register(email):
    
    reg_url = "https://auth.kilimo.go.tz/api/v1/portal/user"
    

    reg_payload = {
        "firstName":fake.first_name_female(),
        "middleName":fake.last_name_female(),
        "surname":"",
        "mobileNumber":"",
        "userType":"FARMER",
        "gender":"MALE",
        "email":email,
        "password":"matako@1998",
        "confirmPassword":"matako@1998",
        "enabled":True,
        "accountNonExpired":True,
        "credentialsNonExpired":True,
        "accountNonLocked":True,
        "name":"khulthum amin amina"
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-request-source": "web"
    }

    resp = scraper.post(reg_url, json=reg_payload, headers=headers)
    return resp.text

if __name__ == "__main__":
    scraper = cloudscraper.create_scraper()
    fake = Faker()
    
    email = f"samiasuluhu"
    print(email)
    with open("acc.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([email])  # email as a single-column row
    print(register(email))