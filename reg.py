import cloudscraper
from faker import Faker
import csv




def register(email):
    
    reg_url = "https://auth.kilimo.go.tz/api/v1/portal/user"
    ext_url = "https://ekilimo.kilimo.go.tz/gateway/ikmis-crop-management-service/api/v1/extensions"
    
    ext_payload = {"firstName":"BINTI","middleName":"MKUBWA","surname":"MALI","nida":"89536984378935676589","gender":"FEMALE","phoneNumber":"","email":"samiasuluhu@gmail.com","educationLevel":"BachelorDegree","extensionOfficerEnum":"PUBLIC","checkNumber":5678,"professionalismEnum":"CropExtensionOfficer","extensionOfficerServicesEnum":"AgriculturalInputSupply","workStationType":"REGION","designation":"RegionalAgriculturalExtensionOfficer(RAO)","regionId":19}
    
    reg_payload = {
        "firstName":fake.first_name_female(),
        "middleName":fake.last_name_female(),
        "surname":"",
        "mobileNumber":"",
        "userType":"FARMER",
        "gender":"",
        "email":email,
        "password":"matako@1998",
        "confirmPassword":"matako@1998",
        "enabled":True,
        "accountNonExpired":True,
        "credentialsNonExpired":True,
        "accountNonLocked":True,
        "name":""
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-request-source": "web"
    }

    resp = scraper.post(reg_url, json=reg_payload, headers=headers)
    # resp = scraper.post(ext_url, json=ext_payload, headers=headers)
    return resp.json().get("description")

if __name__ == "__main__":
    scraper = cloudscraper.create_scraper()
    fake = Faker()

    for i in range(10):
        email = fake.name().replace(" ", "").lower()
        reg_status = register(email)
        print(reg_status)
        if reg_status.lower == "completed successfully":
            with open("acc.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([email])  # email as a single-column row
        
