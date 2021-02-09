import os
from os import path


username = os.environ["OPENREVIEW_USERNAME"]
password = os.environ["OPENREVIEW_PASSWORD"]

conference = "bioconductor.org/BioC/2021/Conference"

output_dir = "_out"
if not path.exists(output_dir):
    os.mkdir(output_dir)
