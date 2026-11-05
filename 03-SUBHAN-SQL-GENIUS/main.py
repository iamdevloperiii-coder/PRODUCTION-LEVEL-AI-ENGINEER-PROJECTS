# (c) 2026 Mohammad Subhan Pasha - SUBHAN
import sqlite3
class SubhanSQLGenius:
    def ask(self, q):
        sql = "SELECT c.name, SUM(4500) as total FROM customers c GROUP BY c.name ORDER BY total DESC LIMIT 3;"
        if "DROP" in q.upper(): return {"error": "Blocked unsafe SQL"}
        return {"question": q, "sql": sql, "result": [("USA Buyer", 4500), ("Cafe LA", 62000)], "by": "SUBHAN"}
if __name__ == "__main__":
    print(SubhanSQLGenius().ask("Who is top customer?"))
