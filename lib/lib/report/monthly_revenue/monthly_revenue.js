// Copyright (c) 2024, lib and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Monthly Revenue"] = {
	"filters": [
		{
			'fieldname': 'month',
			'label': __('Month'),
			'fieldtype': 'Select',
			'options': [
                { "label": "January", "value": "1" },
                { "label": "February", "value": "2" },
                { "label": "March", "value": "3" },
                { "label": "April", "value": "4" },
                { "label": "May", "value": "5" },
                { "label": "June", "value": "6" },
                { "label": "July", "value": "7" },
                { "label": "August", "value": "8" },
                { "label": "September", "value": "9" },
                { "label": "October", "value": "10" },
                { "label": "November", "value": "11" },
                { "label": "December", "value": "12" }
            ],
            'reqd': 1
		},
		{
			'fieldname': 'Book',
			'label': __('Book'),
			'fieldtype': 'Link',
			'options': 'Books',
			'reqd': 1
		}
	],
	onload: function(report){
		report.page.add_inner_button(__("Add Issue Book"), function() {

			let d = new frappe.ui.Dialog({
				title: 'Add Issue Book',
				fields: [
					{
						label: 'Book',
						fieldname: 'book',
						fieldtype: 'Link',
						options: 'Books',
						reqd: 1
					},
					// {
					// 	label: 'Book Title',
					// 	fieldname: 'book title',
					// 	fieldtype: 'Data'
					// },
					// {
					// 	label: 'Author',
					// 	fieldname: 'author',
					// 	fieldtype: 'Data',
					// 	// options: 'Books'
					// },
					{
						label: 'Member',
						fieldname: 'member',
						fieldtype: 'Link',
						options: 'Member',
						reqd: 1
					},
					{
						label: 'Issue Date',
						fieldname: 'issue_date',
						fieldtype: 'Date',
						reqd: 1
					}
				],
				size: 'small', // small, large, extra-large 
				primary_action_label: 'Submit',
				primary_action(values) {
					console.log(values);
					frappe.db.insert({
						"doctype": "Issued Book",
						"book": values.book,
						// "book_title": values.book_title,
						// "author": values.author,
						"member": values.member,
						"issue_date": values.issue_date
					}).then(function(doc){
						// frappe.call({
						// 	method:"frappe.client.submit",
						// 	args: {
						// 		doc: "Issued Book",
						// 		// name: doc.name
						// 	},
						// 	callback: function(response){
						// 		console.log(response)
						// 	} 
						// })
					});
					d.hide();
				}
			});
			d.show();			
		});
	}
};
