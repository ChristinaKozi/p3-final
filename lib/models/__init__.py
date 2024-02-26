import sqlite3

CONN = sqlite3.connect('streaming.db')
CURSOR = CONN.cursor()
