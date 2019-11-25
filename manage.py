from flask_script import Manager
# allows script commands to be run from command line
from flask_migrate import MigrateCommand, Migrate
# migrate allows db migration using alembic

from app import app
from models import db

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ = "__main__":
    manager.run()
