import requests


def send_csv(file_name: str, csv: str) -> None:
    url = "https://httpbin.org/post"
    files = {"file": (file_name, csv)}
    requests.post(url, files=files)
