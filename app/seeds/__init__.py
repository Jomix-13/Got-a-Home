from flask.cli import AppGroup
from .users import seed_users, undo_users
from .homes import seed_homes, undo_homes
from .questions import seed_questions, undo_questions
from .images import seed_images, undo_images

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_homes()
    seed_questions()
    seed_images()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_questions()
    undo_homes()
    undo_images()
    # Add other undo functions here
