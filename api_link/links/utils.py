import requests
from bs4 import BeautifulSoup


def take_link_info(link):
    """парсин данных HTML страницы"""

    response = requests.get(link)
    if response.status_code == 200:
        data = {}
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find("meta", property="og:title")
        if title:
            data["title"] = title.get("content")
        else:
            data["title"] = ""
        description = soup.find("meta", property="og:description")
        if description:
            data["description"] = description.get("content")
        else:
            data["description"] = ""
        data["link"] = link
        image = soup.find("meta", property="og:image")
        if image:
            data["image"] = image.get("content")
        else:
            data["image"] = ""
        type = soup.find("meta", property="og:type")
        if type:
            data["type"] = type.get("content")
        else:
            data["type"] = "website"
        return data
    else:
        return {}