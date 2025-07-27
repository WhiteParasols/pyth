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

@app.route('/api/store-sales/<store_id>')
def api_store_sales(store_id):
    sales_query = f"""
        SELECT 
            strftime('%Y-%m', orders.OrderAt) AS OrderMonth,
            SUM(CAST(items.UnitPrice AS REAL)) AS Revenue,
            COUNT(orderitems.Id) AS ItemCount
        FROM orderitems
        JOIN orders ON orderitems.OrderId = orders.Id
        JOIN items ON orderitems.ItemId = items.Id
        JOIN stores ON orders.StoreId = stores.Id
        WHERE stores.Id = '{store_id}'
        GROUP BY OrderMonth
        ORDER BY OrderMonth;
    """

    customers_query = f"""
        SELECT 
            users.Id AS UserId,
            users.Name AS UserName,
            COUNT(orders.Id) AS OrderCount
        FROM orders
        JOIN users ON orders.UserId = users.Id
        WHERE orders.StoreId = '{store_id}'
        GROUP BY users.Id, users.Name
        ORDER BY OrderCount DESC
        LIMIT 10;
    """

    return jsonify({
        "sales": query_db(sales_query),
        "customers": query_db(customers_query)
    })

@app.route('/api/store-monthly/<store_id>/<month>')
def api_store_monthly_sales(store_id, month):
    summary_query = f"""
        SELECT 
            strftime('%Y-%m-%d', orders.OrderAt) AS OrderDate,
            SUM(CAST(items.UnitPrice AS REAL)) AS Revenue,
            COUNT(orderitems.Id) AS ItemCount
        FROM orderitems
        JOIN orders ON orderitems.OrderId = orders.Id
        JOIN items ON orderitems.ItemId = items.Id
        WHERE strftime('%Y-%m', orders.OrderAt) = '{month}'
          AND orders.StoreId = '{store_id}'
        GROUP BY OrderDate
        ORDER BY OrderDate;
    """

    top_users_query = f"""
        SELECT 
            users.Id AS UserId,
            users.Name AS UserName,
            COUNT(orders.Id) AS OrderCount
        FROM orders
        JOIN users ON orders.UserId = users.Id
        WHERE orders.StoreId = '{store_id}'
        AND strftime('%Y-%m', orders.OrderAt) = '{month}'
        GROUP BY users.Id, users.Name
        ORDER BY OrderCount DESC
        LIMIT 5;
    """

    return jsonify({
        "summary": query_db(summary_query),
        "top_users": query_db(top_users_query)
    })

if __name__ == '__main__':
    app.run(debug=True)
