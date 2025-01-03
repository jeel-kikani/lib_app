// Copyright (c) 2024, lib and contributors
// For license information, please see license.txt

// frappe	.ui.form.on('Issued Books', {
	// refresh: function(frm) {

	// }
//     after_save(frm){
//         frm.refresh_fields('my_member')
//     }
// });


// frappe.ui.form.on('Issued Book', {
//     refresh(frm) {
//         if (frm.doc.name) {
//             frappe.call({
//                 method: 'on_submit', 
//                 args: {
//                     issue_book_id: frm.doc.name
//                 },
//                 // callback: function(response) {
//                 //     // The response.message will contain the count of issued books
//                 //     var count = response.message;
//                 //     if (count === 3) {
//                 //         // Show a message if the count is exactly 3
//                 //         frappe.msgprint(`Member ${frm.doc.member_id} has issued books 3 times.`);
//                 //     } else {
//                 //         // Optionally, show the count for other scenarios
//                 //         frappe.msgprint(`Member ${frm.doc.member_id} has issued books ${count} times.`);
//                 //     }
//                 // }
//             });
//         }
//     }
// });
