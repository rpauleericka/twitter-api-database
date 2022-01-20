# config.py
# pylint: disable=missing-docstring

import os
from dotenv import load_dotenv

load_dotenv()
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # L'appel de replace() permet de s'assurer que l'URI commence par 'postgresql://' et non par 'postgres://' comme c'était le cas auparavant (il s'agit d'un hack de rétrocompatibilité).
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']