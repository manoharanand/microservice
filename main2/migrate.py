# from main import app, db
# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager

# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# if __name__ == '__main__':
#     manager.run()


from main import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == "__main__":
    from flask.cli import main as flask_main
    flask_main()

