import frappe
from frappe.utils import getdate, flt, get_first_day, get_last_day
from datetime import datetime

def execute(filters=None):
    columns = [
        {"label": "Book ID", "fieldname": "name", "fieldtype": "Data", "width": 150},
        {"label": "Books Title", "fieldname": "book_title", "fieldtype": "Data", "width": 150},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Int", "width": 150}
    ]
    # frappe.msgprint(repr(filters))
    
    # if filters and filters.get('month'):
    month = filters.get('month') if filters else None
    
    
    
    # Fetch data from 'Books' table, and calculate revenue if month is selected
    if month:
        year = 2024
        start_date = get_first_day(f"{year}-{month}-01")
        end_date = get_last_day(f"{year}-{month}-01")
        data = frappe.db.sql("""
            SELECT
                name,
                book_title,
                SUM(rent_fee) AS revenue
            FROM
                `tabReturn Book`
            WHERE
                return_date BETWEEN %s AND %s
            GROUP BY
                book
        """, (start_date, end_date), as_dict=True)
    else:
        data = frappe.get_all("Books", fields=["name", "book_title", "SUM(rent_fee) AS revenue"])

    # Handle missing 'revenue' gracefully by providing a default value
    chart = {
        'data': {
            'labels': [book.name for book in data],
            'datasets': [{'values': [flt(book.get('revenue',0)) for book in data]}]
        },
        'type': 'bar'
    }

    message = 'Monthly revenue' if month else 'Total revenue'

    return columns, data, message, chart

