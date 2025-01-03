// Copyright (c) 2024, lib and contributors
// For license information, please see license.txt

frappe.ui.form.on('Books', {
	refresh: function(frm) {
       frm.add_custom_button(__('Issued Books'), function() {
           frappe.new_doc('Issued Book',{
            book:frm.doc.name
           });

       }, __("Transaction Type"));

       frm.add_custom_button(__('Return Book'), function() {
        // let currentDate = new Date().toISOString().split('T')[0];
        frappe.new_doc('Return Book',{
            // return_date: currentDate,
            book:frm.doc.name
        });
    }, __("Transaction Type"));
   }
});


