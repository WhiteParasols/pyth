from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from utils.db import get_table_columns, query_db_paginated, query_db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

def get_paginated_result(table_name):
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    search = request.args.get('search', '')
    sort = request.args.get('sort', 'Id')
    order = request.args.get('order', 'asc').lower()

    base_query = f"SELECT * FROM {table_name}"

    valid_cols = get_table_columns(table_name)

    # Filter
    if search:
        base_query += " WHERE " + " OR ".join(
            [f"{col} LIKE '%{search}%'" for col in valid_cols]
    )

    # Validate sorting
    if sort not in valid_cols:
        sort = "Id"

    if sort:
        base_query += f" ORDER BY {sort} {order.upper()}"

    return jsonify(query_db_paginated(base_query, page, limit))


@app.route('/api/users')
def api_users():
    return get_paginated_result("users")

@app.route('/api/stores')
def api_stores():
    return get_paginated_result("stores")

@app.route('/api/orders')
def api_orders():
    user_id = request.args.get('userId')
    order_id = request.args.get('id')
    search = request.args.get('search', '')
    sort = request.args.get('sort', 'Id')
    order = request.args.get('order', 'asc').lower()
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    # Case 1: single order by ID
    if order_id:
        query = f"SELECT * FROM orders WHERE Id = '{order_id}'"
        return jsonify({ "data": query_db(query) })

    # Case 2: filter by UserId + search + pagination
    base_query = "SELECT * FROM orders"
    filters = []

    # Add userId filter if present
    if user_id:
        filters.append(f"UserId = '{user_id}'")

    # Add search filter
    if search:
        filters.append(" OR ".join([
            f"{col} LIKE '%{search}%'" for col in ["Id", "OrderAt", "StoreId", "UserId"]
        ]))

    # Combine filters
    if filters:
        base_query += " WHERE " + " AND ".join([f"({f})" for f in filters])

    # Sorting
    base_query += f" ORDER BY {sort} {order.upper()}"

    # Paginate unless in userId-only mode with no pagination needed
    return jsonify(query_db_paginated(base_query, page, limit))


@app.route('/api/items')
def api_items():
    return get_paginated_result("items")

@app.route('/api/item-sales/<item_id>')
def api_item_sales(item_id):
    query = f"""
        SELECT 
            strftime('%Y-%m', orders.OrderAt) AS OrderMonth,
            COUNT(orderitems.Id) AS ItemCount,
            COUNT(orderitems.Id) * CAST(items.UnitPrice AS REAL) AS TotalRevenue
        FROM orderitems
        JOIN orders ON orderitems.OrderId = orders.Id
        JOIN items ON orderitems.ItemId = items.Id
        WHERE items.Id = '{item_id}'
        GROUP BY OrderMonth, items.Name, items.UnitPrice
        ORDER BY OrderMonth
    """
    return jsonify({ "data": query_db(query) })


@app.route('/api/orderitems')
def api_orderitems():
    order_id = request.args.get('orderId')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    if order_id:
        query = f"SELECT * FROM orderitems WHERE OrderId = '{order_id}'"
        return jsonify({ "data": query_db(query) })

    return get_paginated_result("orderitems")


if __name__ == '__main__':
    app.run(debug=True)
