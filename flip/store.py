from __future__ import annotations
import json,sqlite3
from .block import Block
class ChainStore:
    """SQLite persistence; database is a local replica, not a consensus authority."""
    def __init__(self,path="flip-chain.sqlite3"):
        self.db=sqlite3.connect(path);self.db.execute("CREATE TABLE IF NOT EXISTS blocks(hash TEXT PRIMARY KEY,height INTEGER NOT NULL,previous_hash TEXT NOT NULL,header TEXT NOT NULL,transactions TEXT NOT NULL)");self.db.commit()
    def put(self,block:Block):
        h=block.header.hash(); self.db.execute("INSERT OR IGNORE INTO blocks VALUES(?,?,?,?,?)",(h,block.header.height,block.header.previous_hash,block.header.canonical().decode(),json.dumps(block.transactions)));self.db.commit()
    def get_by_height(self,height:int):
        row=self.db.execute("SELECT header,transactions FROM blocks WHERE height=? ORDER BY hash LIMIT 1",(height,)).fetchone()
        return row
    def heights(self): return [r[0] for r in self.db.execute("SELECT height FROM blocks ORDER BY height")]
    def close(self): self.db.close()
