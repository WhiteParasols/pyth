import sqlite3

DB = 'mycrm.db'

def query_db(query, args=()):
    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row  # Enables dict-like rows
        cur = conn.cursor()
        cur.execute(query, args)
        rows = cur.fetchall()
        return [dict(row) for row in rows]

def query_db_paginated(query, page, limit, params=[]):
    offset = (page - 1) * limit
    paginated_query = f"{query} LIMIT {limit} OFFSET {offset}"

    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        # Total rows
        count_query = f"SELECT COUNT(*) FROM ({query})"
        total = cur.execute(count_query, params).fetchone()[0]

        # Data rows
        cur.execute(paginated_query, params)
        rows = cur.fetchall()
        data = [dict(row) for row in rows]

    return {
        "data": data,
        "pagination": {
            "page": page,
            "limit": limit,
            "total_rows": total,
            "total_pages": (total + limit - 1) // limit
        }
    }

def get_table_columns(table_name):
    with sqlite3.connect(DB) as conn:
        cur = conn.execute(f"PRAGMA table_info({table_name})")
        return [row[1] for row in cur.fetchall()]
