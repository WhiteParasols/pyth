let currentPage = 1;
let currentEndpoint = '';
let currentLimit = 10;
let currentSearch = '';
let currentSort = 'Id';
let currentOrder = 'asc';
let itemChart = null;

function setupControls(endpoint) {
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
    const { page: current, total_pages: total } = result.pagination;

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
                table += `<td><a href="#" onclick="loadSingleOrder('${row[key]}')">${row[key]}</a></td>`;
            } else if (currentEndpoint === 'items' && key === 'Id') {
                table += `<td><a href="#" onclick="loadItemSales('${row[key]}')">${row[key]}</a></td>`;
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
    const data = result.data;
    // const { page, total_pages } = result.pagination;

    const container = document.getElementById('table-container');
    container.innerHTML = `<h2>Orders for User ID: ${userId}</h2>`;
    //container.innerHTML += `<button onclick="loadTable('users', currentPage)">← Back to All Users</button>`;

    if (!data.length) {
        container.innerHTML += `<p>No orders found for this user.</p>`;
        return;
    }

    let table = '<table><thead><tr>';
    for (let key in data[0]) table += `<th>${key}</th>`;
    table += '</tr></thead><tbody>';

    for (let row of data) {
        table += '<tr>';
        for (let key in row) {
            if (key === 'Id') {
                table += `<td><a href="#" onclick="loadOrderItems('${row[key]}')">${row[key]}</a></td>`;
            } else {
                table += `<td>${row[key]}</td>`;
            }
        }

        table += '</tr>';
    }

    table += '</tbody></table>';
    container.innerHTML += table;
}

async function loadSingleOrder(orderId) {
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
