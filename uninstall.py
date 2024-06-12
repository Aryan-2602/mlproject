import subprocess

packages = [
    "contourpy==1.2.1",
    "cycler==0.12.1",
    "fonttools==4.53.0",
    "kiwisolver==1.4.5",
    "matplotlib==3.9.0",
    "nltk==3.8.1",
    "numpy==1.26.4",
    "packaging==24.1",
    "pandas==2.2.2",
    "pillow==10.3.0",
    "pyparsing==3.1.2",
    "python-dateutil==2.9.0.post0",
    "pytz==2024.1",
    "regex==2022.10.31",
    "seaborn==0.13.2",
    "setuptools==69.5.1",
    "six==1.16.0",
    "tzdata==2024.1",
    "wheel==0.43.0"
]

for package in packages:
    subprocess.run(["pip", "install", "-y", package])