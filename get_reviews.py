import openreview

import config

client = openreview.Client(
    baseurl="https://api.openreview.net",
    username=config.username,
    password=config.password,
)

paper124_reviews = client.get_notes(
    invitation=config.conference + "/Paper124/-/Official_Review"
)

print(paper124_reviews)
print(paper124_reviews[0])
