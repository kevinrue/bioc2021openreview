import openreview
import os

import config

c = openreview.Client(
    baseurl="https://api.openreview.net", username=config.username, password=config.password
)

notes = c.get_notes(invitation=config.conference + "/-/Submission")

# print(len(notes))
# print(notes[0])

contact_email = [note.content["contact_email"] for note in notes]

with open(os.path.join(config.output_dir, "contact_email.txt"), 'w') as f:
    for email in contact_email:
        f.write("%s\n" % email)
