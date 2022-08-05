from ext import db
from ext.site import model
from ext import schedule
from ext.site import controller
from ext.cli import cli

if __name__ == "__main__":
    db.init_app()
    model.init_app()
    controller.init_app()
    cli.init_app()
