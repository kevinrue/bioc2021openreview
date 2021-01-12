# Set up

In your `.zshrc` or equivalent, add your OpenReview login details as environment variables, e.g.

```
OPENREVIEW_USERNAME="your_username"
OPENREVIEW_PASSWORD="your password"
```

Create a Conda environment and install dependencies.

```
conda create -n bioc2021 python=3.9
conda activate bioc2021
pip install -r requirements.txt
```

# Working environment

```
conda activate bioc2021
```

# Test

```
conda activate bioc2021
python test.py
```
