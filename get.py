import requests

url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=20000&country=all&ssl=all&anonymity=all"
response = requests.get(url)
proxies = set(response.text.strip().splitlines())

with open("http.txt", "w") as f:
    f.write("\n".join(proxies))

print(f"New proxy total: {len(proxies)}")