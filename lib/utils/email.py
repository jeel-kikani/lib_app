import frappe

def send_book_details(
        recipients,
        # cc,
        transation_type,
        reminder_text,
        book,
        book_title,
        author,
        member,
        attachments = [],
        issue_date=None,
        return_date=None,
        rent_fee=None):
    
    try:
        context = {
            'transation_type': transation_type,
            'reminder_text': reminder_text,
            'book':book,
            'book_title': book_title,
            'author':author,
            'member':member,
            'issue_date':issue_date,
            'return_date':return_date,
            'rent_fee':rent_fee

        }
        rendered_message = frappe.render_template('templates/emails/Books_issue.html', context)
        
        librarian_users = frappe.get_all(
            "User",
            filters={"role": "Librarian Role"},
            fields=["email"]
        )
        cc = [user["email"] for user in librarian_users]

        # Send the email
        frappe.sendmail(
            recipients=recipients,
            cc=cc,
            message=rendered_message,
            subject=frappe._(transation_type),
            header=frappe._(transation_type),
            attachments=attachments
        )
    except Exception as e:
        frappe.log_error(message=str(e), title="Failed to Send Mail")
        frappe.throw(frappe._("Error while sending Mail: {0}").format(str(e)))
