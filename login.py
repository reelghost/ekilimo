import cloudscraper
from urllib.parse import urlparse, parse_qs

def login(username, password):
    scraper = cloudscraper.create_scraper()

    # Step 1: Login credentials and URL
    login_url = "https://auth.kilimo.go.tz/login"
    login_payload = {
        "username": username,
        "password": password
    }

    # Step 2: POST login form
    resp = scraper.post(login_url, data=login_payload, allow_redirects=True)
    if resp.status_code != 200:
        print("Login failed:", resp.status_code)
        return None

    # Step 3: Go to authorize URL to get code
    authorize_url = (
        "https://auth.kilimo.go.tz/oauth2/authorize"
        "?response_type=code"
        "&state=dnc0W7fWVv"
        "&client_id=uaa-client"
        "&scope=read"
        "&redirect_uri=https://portal.kilimo.go.tz/login&continue"
    )

    # Follow redirects manually to capture 'code'
    url = authorize_url
    max_redirects = 5
    code = None

    for _ in range(max_redirects):
        resp = scraper.get(url, allow_redirects=False)
        if resp.status_code in (301, 302):
            url = resp.headers.get("Location")
            # Check if 'code' is in URL
            if url and "code=" in url:
                parsed = urlparse(url)
                qs = parse_qs(parsed.query)
                code = qs.get("code")[0]
                break
        else:
            # If no redirect, maybe final page
            break

    if not code:
        print("Authorization code not found.")
        return None

    # Step 4: Exchange code for access token
    token_url = "https://auth.kilimo.go.tz/oauth2/token"
    token_payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "https://portal.kilimo.go.tz/login",
        "state":"dnc0W7fWVv"
    }
    headers = {
        "Authorization": "Basic dWFhLWNsaWVudDoxMjM0NTY3OA==",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-request-source": "web"
    }

    token_resp = scraper.post(token_url, data=token_payload, headers=headers)
    if token_resp.status_code != 200:
        print("Token request failed:", token_resp.status_code)
        return None

    token_data = token_resp.json()
    access_token = token_data.get("access_token")

    return access_token

if __name__ == "__main__":
    token = login("admin", "matako@1998")
    if token:
        print("Logged in successfully! Token:", token)
