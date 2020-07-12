from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from util import Util

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    Util.print_banner()
    manager.run()
