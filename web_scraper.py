import requests
from bs4 import BeautifulSoup

# fetch webpage
def fetch_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    except Exception as e:
        print("Error:", e)
        return None

# extract data
def extract_data(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("title").text

    featured = soup.find(id="mp-tfa")

    links = soup.find_all("a")

    return title, featured, links

# display data
def display_data(title, featured, links):
    print("\nPage Title:")
    print(title)

    print("\nFeatured Article:")
    if featured:
        print(featured.text.strip())

    print("\nSome Links:")
    for link in links[:10]:   # print first 10 links
        print(link.get("href"))

# Main 
def main():
    url = "https://en.wikipedia.org/wiki/Main_Page"

    html = fetch_page(url)

    if html:
        title, featured, links = extract_data(html)
        display_data(title, featured, links)

# program
if __name__ == "__main__":
    main()