# Copyright (c) 2024, lib and contributors
# For license information, please see license.txt

import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

def execute(filters=None):
    columns = [
        {"label":"Books Name", "fieldname":"name", "fieldtype":"Data", "width":150},
        {"label":"Times Issued", "fieldname":"time_issued", "fieldtype":"Int", "width":150}
	]
    
    data = frappe.get_all("Books", fields=["name", "time_issued"])
    frappe.msgprint(repr(data))
    
    # time_issue_list = frappe.db.sql("""
	# 	SELECT
    #     name,
	# 	time_issued
	# 	FROM tabBooks
	# """, as_dict=1)
    
    
    chart = {
        'data': {
            'labels': [book.name for book in data],
            'datasets': [{'values': [book.time_issued for book in data]}]
		},
        'type': 'bar'
	}
    message = 'Number of times books issued by member'
    
    return columns, data, message, chart