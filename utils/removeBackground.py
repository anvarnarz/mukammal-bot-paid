import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "background-removal.p.rapidapi.com",
    'x-rapidapi-key': "SIZNING_API_KALITINGIZ"
    }
# test payload
# payload = "image_url=https%3A%2F%2Fobjectcut.com%2Fassets%2Fimg%2Fraven.jpg"

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']