import os
import pathlib

basedir = pathlib.Path(__file__).parent.absolute()
print(os.environ.get("DATABASE_NAME"))


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}' + f'{os.environ.get('SQLITE_DATABASE_PATH')}' or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    print(SQLALCHEMY_DATABASE_URI)
