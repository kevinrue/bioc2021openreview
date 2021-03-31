import openreview
import pandas
import os

import config

c = openreview.Client(
    baseurl="https://api.openreview.net", username=config.username, password=config.password
)

notes = c.get_notes(invitation=config.conference + "/-/Submission")

# Reformat content into single value fields

title = [note.content["title"] for note in notes]

authorids = [",".join(note.content["authorids"]) for note in notes]

authors = [",".join(note.content["authors"]) for note in notes]

keywords = [",".join(note.content["keywords"]) for note in notes]

abstract = [note.content["abstract"] for note in notes]

affiliation = [note.content["affiliation"] for note in notes]

contact_email = [note.content["contact_email"] for note in notes]

#gender = [note.content["gender"] for note in notes]

#bioconductor_package_maintenance = [note.content["bioconductor_package_maintenance"] for note in notes]

associated_packages = [note.content["associated_packages"] for note in notes]

short_talk = ["Short talk" in note.content["submission_type"] for note in notes]
package_demo = ["Package demo" in note.content["submission_type"] for note in notes]
birds_of_a_feather = ["Birds-of-a-Feather" in note.content["submission_type"] for note in notes]
long_workshop = ["Long workshop" in note.content["submission_type"] for note in notes]
poster = ["Poster" in note.content["submission_type"] for note in notes]

submission_is_not_registration = [note.content["submission_is_not_registration"] for note in notes]

code_of_conduct = [note.content["code_of_conduct"] for note in notes]

paperhash = [note.content["paperhash"] for note in notes]

submissions_table = pandas.DataFrame(data = {
    "title": title,
    "authorids": authorids,
    "authors": authors,
    "keywords": keywords,
    "abstract": abstract,
    "affiliation": affiliation,
    "contact_email": contact_email,
    #"gender": gender,
    #"bioconductor_package_maintenance": bioconductor_package_maintenance,
    "associated_packages": associated_packages,
    "short_talk": short_talk,
    "package_demo": package_demo,
    "birds_of_a_feather": birds_of_a_feather,
    "long_workshop": long_workshop,
    "poster": poster,
    "submission_is_not_registration": submission_is_not_registration,
    "code_of_conduct": code_of_conduct,
    "paperhash": paperhash,
})

submissions_table.to_csv(os.path.join(config.output_dir, "submissions.txt"),
    sep = "\t",
    index = False)
