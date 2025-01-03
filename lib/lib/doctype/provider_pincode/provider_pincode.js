frappe.ui.form.on('Provider Pincode', {
	pin_code: function (frm) {
		let pin= frappe.db.get_doc('Pin Code', frm.doc.pin_code)
		let res = pin.then(
			(val) => {
				frm.set_query("provider_comp", (doc) => {
					// console.log(doc)
					return {
						filters: {
							name : val.provider,
						}
					}
				})
			},
			(err) => {
				frm.set_query("provider_comp",(doc) =>{
					return{
						filters:{
							name:"",
						}
					}
				})
			}
		)
    }
});
