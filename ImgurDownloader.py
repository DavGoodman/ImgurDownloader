# downloads the first page of images from imgur based on the search
import os, requests, bs4

os.makedirs("imgurpics", exist_ok=True)

search = input("")
res = requests.get("https://imgur.com/search?q=" + search)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
image_elem = soup.select("a img")

for i in image_elem:
    src = i.get("src")
    image_url = "https:" + i.get("src")
    res = requests.get(image_url)
    res.raise_for_status()

    image_file = open(os.path.join("imgurpics", os.path.basename(image_url)), "wb")
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()