import requests
import csv
import login

search_url = "https://ekilimo.kilimo.go.tz/gateway/ikmis-crop-management-service/api/v1/advisory-inquiry?pageSize=10"

token = login.login("kigoshomusic@gmail.com", "@00n4ceynRaD")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def save_to_csv(data, filename='tz_farmers.csv'):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(['q_id'])
            # Write data
            for item in data:
                writer.writerow([
                    item.get('uuid', '')
                ])
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

try:
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()
    data = response.json().get("data", {}).get("itemList", [])
    print(len(data))
    
    if not data:
        print("No data found in the response")
    else:
        save_to_csv(data)
        
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except ValueError as e:
    print(f"Error parsing JSON response: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print("Raw response:", response.text)
