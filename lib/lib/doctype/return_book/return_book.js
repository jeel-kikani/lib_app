// Copyright (c) 2024, lib and contributors
// For license information, please see license.txt

frappe.ui.form.on('Return Book', {
	refresh: function(frm) {
		console.log(frm);
		if (frappe.user.has_role('Librarian Role') && frm.doc.docstatus == 1){
			frm.add_custom_button('Payment', function(){
				frappe.new_doc('Payments', {
					member:frm.doc.member,
					book:frm.doc.book,
					return_id:frm.doc.name
				});
				// console.log(frm)
			})
		}
	}
});
