import openreview

import config

c = openreview.Client(
    baseurl="https://api.openreview.net", username=config.username, password=config.password
)

notes = c.get_notes(invitation=config.conference + "/-/Submission")

print(len(notes))
print(notes[0])
