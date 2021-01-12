import openreview
import os

username = os.environ["OPENREVIEW_USERNAME"]
password = os.environ["OPENREVIEW_PASSWORD"]


client = openreview.Client(
    baseurl="https://api.openreview.net", username=username, password=password
)

if client.baseurl == 'https://api.openreview.net':
    print("Success!")
