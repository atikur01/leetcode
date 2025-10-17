import requests

url = "https://rakin-portfolio-backend.vercel.app/api/v1/contact/new"

headers = {
    "Host": "rakin-portfolio-backend.vercel.app",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua": '"Not=A?Brand";v="24", "Chromium";v="140"',
    "Content-Type": "application/json",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/140.0.0.0 Safari/537.36",
    "Origin": "https://rakin-al-mahin.vercel.app",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://rakin-al-mahin.vercel.app/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=4, i"
}

data = {
    "name": "rakinalmahin@gmail.com",
    "email": "rakinalmahin@gmail.com",
    "subject": "rakinalmahin@gmail.com",
    "message": "rakinalmahin@gmail.com"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
