import openreview
import os

username = os.environ["OPENREVIEW_USERNAME"]
password = os.environ["OPENREVIEW_PASSWORD"]


c = openreview.Client(
    baseurl="https://api.openreview.net", username=username, password=password
)

notes = c.get_notes(invitation="bioconductor.org/EuroBioC/2020/Conference/-/Submission")

len(notes)
notes[0]