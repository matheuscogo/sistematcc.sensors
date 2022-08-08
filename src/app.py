from ext import db
from ext.site import model
from ext.site import controller

if __name__ == "__main__":
    db.init_app()
    model.init_app()
    controller.init_app()
