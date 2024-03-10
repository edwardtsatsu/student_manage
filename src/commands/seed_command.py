from flask.cli import AppGroup
from src.seeders import run_seed

seed_cli = AppGroup('seed')


@seed_cli.command('db')
def seed():
    run_seed()
