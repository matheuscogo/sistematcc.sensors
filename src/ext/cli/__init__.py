import click
from ..cli.cli import create_db, drop_db

def init_app(app):

    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))

    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate e listar pedidos
        click.echo("lista de pedidos")
