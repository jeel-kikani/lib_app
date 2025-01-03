// Copyright (c) 2024, lib and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Member', {
// 	member_author: function(frm){
// 		let member_author = frm.doc.member_author;

// 		if(member_author){
// 			frappe.call({
// 				method: "lib.lib.doctype.member.member.get_member_author",
// 				args: {member_author: member_author}
// 			}).done((r) => {
// 				console.log(r)
// 			})
// 		}
// 		// console.log("+++++++++++++++++++++++++++++++++++++++++++++++")
// 	}
// });