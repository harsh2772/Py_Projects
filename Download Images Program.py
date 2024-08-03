import requests

while True:

    URL = input("Enter The Url: ")

    if (URL == "quit"):
        break

    response = requests.get(URL)
    Image = input("Enter The Image name: ")
    open(f"{Image}.jpg", "wb").write(response.content)