from __future__ import annotations

import sqlite3
from pathlib import Path

import stratz
from stratz.lang import code_English

api = stratz.Api(
    lang=code_English, token=open(
        'stratztoken.env',
    ).read().splitlines()[0],
)
path = Path('dota.db')
path.touch()
con = sqlite3.connect(path)
