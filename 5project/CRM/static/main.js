let currentPage = 1;
let currentEndpoint = '';
let currentLimit = 10;
let currentSearch = '';
let currentSort = 'Id';
let currentOrder = 'asc';
let itemChart = null;

function setupControls() {
    const container = document.getElementById('table-container');
    container.innerHTML = `
        <div class="controls">
            <div>
                <input type="text" id="searchBox" placeholder="Search..." value="${currentSearch}">
                <button id="searchBtn">Search</button>
            </div>

            <label>Rows per page: 
                <select id="limitSelect">
                    <option value="5" ${currentLimit == 5 ? 'selected' : ''}>5</option>
                    <option value="10" ${currentLimit == 10 ? 'selected' : ''}>10</option>
                    <option value="50" ${currentLimit == 50 ? 'selected' : ''}>50</option>
                </select>
            </label>
        </div>
        <div id="data-table"></div>
    `;

    document.getElementById('searchBtn').onclick = () => {
        currentSearch = document.getElementById('searchBox').value.trim();
        loadTable(currentEndpoint, 1);
    };

    // When "Enter" is pressed in the input box
    document.getElementById('searchBox').addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            currentSearch = e.target.value.trim();
            loadTable(currentEndpoint, 1);
        }
    });

    document.getElementById('limitSelect').onchange = () => {
        currentLimit = parseInt(document.getElementById('limitSelect').value);
        loadTable(currentEndpoint, 1);
    };
}

async function loadTable(endpoint, page = 1) {
    currentEndpoint = endpoint;
    currentPage = page;
    setupControls(endpoint);

    const res = await fetch(`/api/${endpoint}?page=${page}&limit=${currentLimit}&search=${encodeURIComponent(currentSearch)}&sort=${currentSort}&order=${currentOrder}`);
    const result = await res.json();
    const data = result.data;
    const { page: current = 1, total_pages: total = 1 } = result.pagination || {};

    const tableContainer = document.getElementById('data-table');

    if (!data.length) {
        tableContainer.innerHTML = '<p>No data found.</p>';
        return;
    }

    // Table with sortable headers
    let table = '<table><thead><tr>';
    for (let key in data[0]) {
        let indicator = (currentSort === key) ? (currentOrder === 'asc' ? '▲' : '▼') : '';
        table += `<th onclick="sortBy('${key}')">${key} ${indicator}</th>`;
    }
    table += '</tr></thead><tbody>';

    for (let row of data) {
        table += '<tr>';
        for (let key in row) {
            if (currentEndpoint === 'users' && key === 'Id') {
                table += `<td><a href="#" onclick="loadRelatedOrders('${row[key]}')">${row[key]}</a></td>`;
            } else if (currentEndpoint === 'orders' && key === 'Id') {
                table += `<td><a href="#" onclick="loadOrderItems('${row[key]}')">${row[key]}</a></td>`;
            } else if (currentEndpoint === 'orderitems' && key === 'OrderId') {
                table += `<td><a href="#" onclick="loadOrder('${row[key]}')">${row[key]}</a></td>`;
            } else if (currentEndpoint === 'orderitems' && key === 'ItemId') {
                table += `<td><a href="#" onclick="loadItemSales('${row[key]}')">${row[key]}</a></td>`;
            } else if (currentEndpoint === 'items' && key === 'Id') {
                table += `<td><a href="#" onclick="loadItemSales('${row[key]}')">${row[key]}</a></td>`;
            } else if (currentEndpoint === 'stores' && key === 'Id') {
                table += `<td><a href="#" onclick="loadStoreSales('${row[key]}')">${row[key]}</a></td>`;
            } else {
                table += `<td>${row[key]}</td>`;
            }
        }
        table += '</tr>';
    }

    table += '</tbody></table>';
    table += generatePagination(current, total, endpoint);
    tableContainer.innerHTML = table;
}

async function loadOrderItems(orderId) {

    const res = await fetch(`/api/orderitems?orderId=${orderId}`);
    const result = await res.json();
    const data = result.data;

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>OrderItems for Order ID: ${orderId}</h2>`;
    // Back button
    // container.innerHTML += `<button onclick="loadTable('orders', currentPage)">← Back to All Orders</button>`;

    if (!data.length) {
        container.innerHTML += `<p>No order items found for this order.</p>`;
        return;
    }

    let table = '<table><thead><tr>';
    for (let key in data[0]) table += `<th>${key}</th>`;
    table += '</tr></thead><tbody>';

    for (let row of data) {
        table += '<tr>';
        for (let key in row) table += `<td>${row[key]}</td>`;
        table += '</tr>';
    }

    table += '</tbody></table>';

    container.innerHTML += table;
}

async function loadRelatedOrders(userId) {
    const res = await fetch(`/api/orders?userId=${userId}`);
    const result = await res.json();

    const orders = result.data || [];
    const topStores = result.top_stores || [];
    const topItems = result.top_items || [];

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>Orders for User ID: ${userId}</h2>`;

    // --- Orders table ---
    if (!orders.length) {
        container.innerHTML += '<p>No orders found for this user.</p>';
    } else {
        let orderTable = '<table><thead><tr>';
        for (let key in orders[0]) orderTable += `<th>${key}</th>`;
        orderTable += '</tr></thead><tbody>';
        for (let row of orders) {
            orderTable += '<tr>';
            for (let key in row) {
                if (key === 'Id') {
                    orderTable += `<td><a href="#" onclick="loadOrderItems('${row[key]}')">${row[key]}</a></td>`;
                } else {
                    orderTable += `<td>${row[key]}</td>`;
                }
            }
            orderTable += '</tr>';
        }
        orderTable += '</tbody></table>';
        container.innerHTML += orderTable;
    }

    // --- Top Stores table ---
    if (topStores.length) {
        container.innerHTML += `<h3>Top 5 Stores Ordered From</h3>`;
        let storeTable = '<table><thead><tr>';
        for (let key in topStores[0]) storeTable += `<th>${key}</th>`;
        storeTable += '</tr></thead><tbody>';
        for (let row of topStores) {
            storeTable += '<tr>';
            for (let key in row) {
                storeTable += `<td>${row[key]}</td>`;
            }
            storeTable += '</tr>';
        }
        storeTable += '</tbody></table>';
        container.innerHTML += storeTable;
    }

    // --- Top Items table ---
    if (topItems.length) {
        container.innerHTML += `<h3>Top 5 Items Ordered</h3>`;
        let itemTable = '<table><thead><tr>';
        for (let key in topItems[0]) itemTable += `<th>${key}</th>`;
        itemTable += '</tr></thead><tbody>';
        for (let row of topItems) {
            itemTable += '<tr>';
            for (let key in row) {
                itemTable += `<td>${row[key]}</td>`;
            }
            itemTable += '</tr>';
        }
        itemTable += '</tbody></table>';
        container.innerHTML += itemTable;
    }
}


async function loadOrder(orderId) {
    const res = await fetch(`/api/orders?id=${orderId}`);
    const result = await res.json();
    const data = result.data;

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>Order Info for Order ID: ${orderId}</h2>`;

    if (!data.length) {
        container.innerHTML += '<p>Order not found.</p>';
        return;
    }

    let table = '<table><thead><tr>';
    for (let key in data[0]) table += `<th>${key}</th>`;
    table += '</tr></thead><tbody>';

    for (let row of data) {
        table += '<tr>';
        for (let key in row) table += `<td>${row[key]}</td>`;
        table += '</tr>';
    }

    table += '</tbody></table>';
    container.innerHTML += table;
}

async function loadItemSales(itemId) {
    const res = await fetch(`/api/item-sales/${itemId}`);
    const result = await res.json();
    const data = result.data;

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>Monthly Sales for Item ID: ${itemId}</h2>`;

    if (!data.length) {
        container.innerHTML += '<p>No sales data found for this item.</p>';
        return;
    }

    let table = '<table><thead><tr>';
    for (let key in data[0]) table += `<th>${key}</th>`;
    table += '</tr></thead><tbody>';

    for (let row of data) {
        table += '<tr>';
        for (let key in row) {
            table += `<td>${row[key]}</td>`;
        }
        table += '</tr>';
    }

    table += '</tbody></table>';
    container.innerHTML += table;

    // Step 1: insert the canvas
    container.innerHTML += `<canvas id="itemChart" width="800" height="400"></canvas>`;

    // Step 2: Wait until the canvas is fully rendered in layout
    requestAnimationFrame(() => {
        const canvas = document.getElementById('itemChart');
        if (!canvas) return console.error("Canvas not found");

        const labels = data.map(row => row.OrderMonth);
        const itemCounts = data.map(row => row.ItemCount);
        const revenues = data.map(row => row.TotalRevenue);

        // Destroy previous chart if exists
        if (itemChart) itemChart.destroy();

        // Step 3: draw the chart
        itemChart = new Chart(canvas, {
            type: 'bar',
            data: {
                labels,
                datasets: [
                    {
                        label: 'Item Count',
                        data: itemCounts,
                        backgroundColor: 'rgba(54, 162, 235, 0.6)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        yAxisID: 'y1'
                    },
                    {
                        label: 'Total Revenue',
                        type: 'line',
                        data: revenues,
                        borderColor: 'rgba(255, 99, 132, 1)',                       
                        yAxisID: 'y2'
                    }
                ]
            },
            options: {
                responsive: true,
                interaction: {
                    mode: 'index',
                    intersect: false
                },
                stacked: false,
                scales: {
                    y1: {
                        type: 'linear',
                        position: 'left',
                        title: { display: true, text: 'Item Count' }
                    },
                    y2: {
                        type: 'linear',
                        position: 'right',
                        title: { display: true, text: 'Total Revenue' },
                        grid: { drawOnChartArea: false }
                    }
                }
            }
        });
    });

}

async function loadStoreSales(storeId) {
    const res = await fetch(`/api/store-sales/${storeId}`);
    const result = await res.json();

    const salesData = result.sales;
    const customerData = result.customers;

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>Monthly Sales for Store ID: ${storeId}</h2>`;

    // First Table: Monthly Sales
    if (!salesData.length) {
        container.innerHTML += '<p>No sales data found for this store.</p>';
    } else {
        let salesTable = '<table><thead><tr>';
        for (let key in salesData[0]) salesTable += `<th>${key}</th>`;
        salesTable += '</tr></thead><tbody>';

        for (let row of salesData) {
            salesTable += '<tr>';
            for (let key in row) {
                if (key === 'OrderMonth') {
                    salesTable += `<td><a href="#" onclick="loadStoreMonthSales('${storeId}', '${row[key]}')">${row[key]}</a></td>`;
                } else {
                    salesTable += `<td>${row[key]}</td>`;
                }
            }
            salesTable += '</tr>';
        }

        salesTable += '</tbody></table>';
        container.innerHTML += salesTable;
    }

    // Second Table: Top 10 Regular Customers
    container.innerHTML += `<h3>Top 10 Regular Customers</h3>`;

    if (!customerData.length) {
        container.innerHTML += '<p>No customer data found for this store.</p>';
        return;
    }

    let custTable = '<table><thead><tr>';
    for (let key in customerData[0]) custTable += `<th>${key}</th>`;
    custTable += '</tr></thead><tbody>';

    for (let row of customerData) {
        custTable += '<tr>';
        for (let key in row) {
            if (key === 'UserId') {
                custTable += `<td><a href="#" onclick="loadRelatedOrders('${row[key]}')">${row[key]}</a></td>`;
            } else {
                custTable += `<td>${row[key]}</td>`;
            }
        }
        custTable += '</tr>';
    }

    custTable += '</tbody></table>';
    container.innerHTML += custTable;
}

async function loadStoreMonthSales(storeId, month) {
    const res = await fetch(`/api/store-monthly/${storeId}/${month}`);
    const result = await res.json();
    const summary = result.summary;
    const topUsers = result.top_users;

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>Monthly Sales for ${month} (Store ID: ${storeId})</h2>`;

    // Monthly Revenue + Item Count
    if (!summary.length) {
        container.innerHTML += '<p>No summary found for this month.</p>';
    } else {
        let summaryTable = '<table><thead><tr>';
        for (let key in summary[0]) summaryTable += `<th>${key}</th>`;
        summaryTable += '</tr></thead><tbody>';

        for (let row of summary) {
            summaryTable += '<tr>';
            for (let key in row) {
                summaryTable += `<td>${row[key]}</td>`;
            }
            summaryTable += '</tr>';
        }

        summaryTable += '</tbody></table>';
        container.innerHTML += summaryTable;
    }

    // Top 5 Regular Customers
    container.innerHTML += `<h3>Top 5 Regular Customers in ${month}</h3>`;
    if (!topUsers.length) {
        container.innerHTML += '<p>No customer data for this month.</p>';
    } else {
        let userTable = '<table><thead><tr>';
        for (let key in topUsers[0]) userTable += `<th>${key}</th>`;
        userTable += '</tr></thead><tbody>';
        for (let row of topUsers) {
            userTable += '<tr>';
            for (let key in row) {
                if (key === 'UserId') {
                    userTable += `<td><a href="#" onclick="loadRelatedOrders('${row[key]}')">${row[key]}</a></td>`;
                } else {
                    userTable += `<td>${row[key]}</td>`;
                }
            }
            userTable += '</tr>';
        }
        userTable += '</tbody></table>';
        container.innerHTML += userTable;
    }
}

function sortBy(column) {
    if (currentSort === column) {
        currentOrder = currentOrder === 'asc' ? 'desc' : 'asc';
    } else {
        currentSort = column;
        currentOrder = 'asc';
    }
    loadTable(currentEndpoint, 1);
}

function generatePagination(current, total, endpoint) {
    let html = '<div class="pagination">';

    const range = 2;
    const start = Math.max(1, current - range);
    const end = Math.min(total, current + range);

    if (current > 1) {
        html += `<button onclick="loadTable('${endpoint}', 1)">«</button>`;
        html += `<button onclick="loadTable('${endpoint}', ${current - 1})">‹</button>`;
    }

    if (start > 1) html += `<span>...</span>`;

    for (let i = start; i <= end; i++) {
        if (i === current) {
            html += `<button class="active">${i}</button>`;
        } else {
            html += `<button onclick="loadTable('${endpoint}', ${i})">${i}</button>`;
        }
    }

    if (end < total) html += `<span>...</span>`;

    if (current < total) {
        html += `<button onclick="loadTable('${endpoint}', ${current + 1})">›</button>`;
        html += `<button onclick="loadTable('${endpoint}', ${total})">»</button>`;
    }

    html += '</div>';
    return html;
}
