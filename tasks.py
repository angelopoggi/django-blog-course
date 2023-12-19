"""Tasks for use with Invoke."""
from invoke import task


# ------------------------------------------------------------------------------
# TESTING
# ------------------------------------------------------------------------------
@task
def fmt(context):
    """Run python formatting."""
    commands = [
        "isort .",
        "black .",
        'find . -type f -name "*.py" | xargs dos2unix --safe 2>/dev/null',
    ]

    for command in commands:
        context.run(command)


@task
def lint(context):
    """Run Python Linting Suite"""
    commands = [
        "yamllint .",
        "isort ./ --check",
        "black --diff .",
        "bandit --recursive ./ --configfile .bandit.yml",
    ]

    for command in commands:
        context.run(command)


@task
def run(context):
    """Starts Django server"""
    commands = [
        "python3 /Users/angelo/PycharmProjects/feedback/feedback/manage.py runserver"
    ]
    for command in commands:
        context.run(command)


@task
def make(context):
    """Makes a Django DB"""
    commands = [
        "python3 /Users/angelo/PycharmProjects/feedback/feedback/manage.py makemigrations"
    ]
    for command in commands:
        context.run(command)


@task
def migrate(context):
    """Migrates a Django DB"""
    commands = [
        "python3 /Users/angelo/PycharmProjects/feedback/feedback/manage.py migrate"
    ]
    for command in commands:
        context.run(command)

@task
def shell(context):
    """Starts the Django Shell"""
    commands = [
        "python3 /Users/angelo/PycharmProjects/feedback/feedback/manage.py shell"
    ]
    for command in commands:
        context.run(command)

