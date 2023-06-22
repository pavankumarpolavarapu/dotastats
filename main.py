from __future__ import annotations

import json
import logging

from globals import api
from globals import con


def main():
    logger = logging.getLogger(__name__)
#    match = api.get_match(7207632145)
#    json.dump(match, open("7207632145.json", "w", encoding="utf-8"))
    player_matches = api.get_player_matches(293437752, take=50)
    json.dump(
        player_matches, open(
            'player_293437752.json', 'w', encoding='utf-8',
        ),
    )

    cur = con.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS
                matches(id INT NOT NULL PRIMARY KEY, body TEXT)
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS
                match (id INT NOT NULL PRIMARY KEY, body TEXT)
                """)
    insert_matches = 'insert into matches(id, body) values(?, ?)'
    insert_match = 'insert into match(id, body) values(?, ?)'
    for match in player_matches:
        match_detail = ''
        match_detail = api.get_match(match['id'])
        try:
            con.execute(insert_match, (match['id'], json.dumps(match_detail)))
            con.execute(insert_matches, (match['id'], json.dumps(match)))
        except Exception as e:
            logger.error(f"Match ID: {match['id']}")
            logger.error(f"Sql error: {''.join(e.args)}")
            logger.error(f'Exception class: {e.__class__}')
            continue
    con.commit()


if __name__ == '__main__':
    main()
