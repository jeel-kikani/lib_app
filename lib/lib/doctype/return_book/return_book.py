import frappe
from frappe.model.document import Document
from datetime import datetime
from lib.utils.email import send_book_details
   

class ReturnBook(Document):
    def before_save(self):
        # Ensure return date is not earlier than issue date
        return_date = datetime.strptime(self.return_date, "%Y-%m-%d").date()
        difference = (return_date - self.issue_date).days
        if return_date < self.issue_date:
            frappe.throw("Return Date cannot be earlier than Issue Date.")
            
        # Rent fee calculation - charge extra based on the number of late days
        if difference > 0:
            self.rent_fee = self.rent_fee * difference  # Assuming rent is per day
        else:
            self.rent_fee = self.rent_fee  # No extra fee if returned on time

        n = frappe.get_doc("Issued Book" ,self.issue_id)
        # frappe.msgprint(repr(self.issue_id))
        if n.book != self.book or n.member != self.member:
            frappe.throw("Not book")

        # if self.book == n:
        #     frappe.msgprint(repr(self.return_date))


    def on_submit(self):
        # Only update member's outstanding debt if the status is 'Active'
        if self.status == "Active":
            member = frappe.get_doc("Member", self.member)
            member.outstanding_debt = float(member.outstanding_debt) + float(self.rent_fee)  
            member.save()
            # frappe.msgprint(f"Member's outstanding debt updated. Current debt: {member.outstanding_debt}")
        

        child_table = frappe.get_all("Member Child", filters=[{"books_name": self.book},{"parent":self.member},{"issued_date":self.issue_date}])
        if child_table:
            child = frappe.get_doc("Member Child", child_table[0])
            child.return_date = self.return_date
            child.save()

        # send_birthday_reminder(
        #     recipients=["jeelkikani56@gmail.com"],
        #     reminder_text="Issued Books List:",
        #     Books_issued_persons=[
        #         {"name": "Alice", "birthday": "2024-01-01"},
        #         {"name": "Bob", "birthday": "2024-01-15"}
        #     ]
        # )
        member_child = frappe.get_doc("Member", self.member)
        recipients = (member_child.email) if member_child.email else []
        pdf_content = frappe.attach_print(self.doctype, self.name, print_format="Standard")
        # user_data = frappe.db.get_value(
		# 	"User", frappe.session.user, ["email"]
		# )

        new_email = {
            "transation_type":"Return Books",
            "recipients":recipients,
            # "cc":user_data,
            "reminder_text":"Returns Books List:",
            "book": self.book,
            "book_title": self.book_title,
            "author": self.author,
            "member": self.member,
            "issue_date":self.issue_date,
            "return_date":self.return_date,
            "rent_fee":self.rent_fee,
            "attachments":[pdf_content]
        }
        # frappe.throw(repr(new_email))
        frappe.enqueue(send_book_details,**new_email)
        # send_book_details(
        #     **new_email
        # )