import subprocess

commands = [
    "isort --check-only --diff .",
    "flake8 --max-line-length=1000 .",
    "pycodestyle --ignore=E501,W504 ."
]

for command in commands:
    subprocess.run(command)
