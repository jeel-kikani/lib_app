# Copyright (c) 2024, lib and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from lib.utils.email import send_book_details
 
class IssuedBook(Document):
    def on_submit(self, user=None):
        book = frappe.get_doc("Books", self.book)
        if int(book.quantity) > 0:
            book.quantity = int(book.quantity) - 1
            book.time_issued = int(book.time_issued) + 1
            # Update Member's issued books count
            member = frappe.get_doc("Member", self.member)
            # if int(member.books_issued) < 3:
            #     member.books_issued = int(member.books_issued) + 1
            #     member.save()
            # else:
            #     frappe.throw(f"Member '{member.name}' has already issued the maximum allowed books.")
            book.save()
        else:
            frappe.throw(f"The book '{book.book_title}' is out of stock.")

    # def on_save(self):
        member_child = frappe.get_doc("Member", self.member)
        # frappe.throw(repr(member_child))
        member_child_new = [{
            'books_name': self.book,
            'issued_date': self.issue_date,
            'return_date': ""
        }]
        # member_child.my_member = []

        for dt in member_child_new:
            member_child.append("my_member",dt)
        member_child.save()

        # send_birthday_reminder(
        #     recipients=["jeelkikani56@gmail.com"],
        #     reminder_text="Issued Books List:",
        #     books_issued_persons=[
        #         {"book": self.book,
        #          "book_title": self.book_title,
        #          "author": self.author
        #         }
        #     ]
        # )
        # attachments = []
        # issued_attachment = frappe.get_doc()
        # cur_doc = "Issued Book"
        # attachments.append(
        #     frappe.attach_print(
        #         doctype="Issued Book",
        #         name=self.name,
        #         doc=cur_doc,
        #         print_format=frappe.get_meta("Issued Book").default_print_format,
        #         letterhead=None,
        #     )
        # )
        pdf_content = frappe.attach_print(self.doctype, self.name, print_format="Standard")
 
        recipients = (member_child.email) if member_child.email else []

        # user_data = frappe.db.get_value(
		# 	"User", frappe.session.user, ["email"]
		# )
        
        # librarian_users = frappe.get_all(
        #     "User",
        #     filters={"role": "Librarian Role"},
        #     fields=["email"]
        # )
        # librarian_user_ids = [user["email"] for user in librarian_users]

        # user_data= frappe.db.get_value(
        #     "User", user.get("user_name")
        # )
        # frappe.msgprint(repr(librarian_user_ids))

        # librarian_userss = frappe.get_all(
        #     "User",
        #     filters={"role": "LibrarianMember Role"},
        #     fields=["parent"]
        # )
        # librarian_user_idss = [user["parent"] for user in librarian_userss]

        # frappe.throw(repr(librarian_user_idss))


        new_email = {
            "transation_type":"Issued Books",
            "recipients":recipients,
            # "cc":librarian_user_ids,
            "reminder_text":"Issued Books List:",
            "book": self.book,
            "book_title": self.book_title,
            "author": self.author,
            "member": self.member,
            "issue_date":self.issue_date,
            "attachments":[pdf_content]
        }
        # frappe.throw(repr(new_email))
        frappe.enqueue(send_book_details,**new_email)
        # send_book_details(
        #     **new_email
        # )