import openreview
import pandas
import os

import config

c = openreview.Client(
    baseurl="https://api.openreview.net", username=config.username, password=config.password
)

notes = c.get_notes(invitation=config.conference + "/Paper.*/-/Official_Review")

invitation = [note.invitation for note in notes]
invitation = [s.replace(config.conference + '/', '') for s in invitation]
paper = [s.replace('/-/Official_Review', '') for s in invitation]

reviewer = [note.signatures[0] for note in notes]
reviewer = [s.replace(config.conference, '').split('/') for s in reviewer]
reviewer = [a[-1] for a in reviewer]

comment = [note.content["review"] for note in notes]

rating = [note.content["rating"].split(':')[0] for note in notes]

sformat = [note.content["suggested_format"] for note in notes]

reviews_table = pandas.DataFrame(data = {
	"paper": paper,
    "reviewer": reviewer,
    "format": sformat,
    "rating": rating,
    "comment": comment
})

reviews_table.to_csv(os.path.join(config.output_dir, "reviews.txt"),
    sep = "\t",
    index = False)



