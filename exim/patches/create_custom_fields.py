from __future__ import unicode_literals
import frappe

def execute():
    # create_bank_field()
    pass

def create_bank_field():
    if frappe.get_doc("Custom Field",{'fieldname':"bank_type",'dt':"Bank"}):
        return
    doc = frappe.new_doc("Custom Field")
    doc.dt = "Bank"
    doc.label = "Bank Type"
    doc.fieldname = "bank_type"
    doc.insert_after = "bank_name"
    doc.fieldtype = "Select"
    doc.options="""\nIndian Bank\nForeign Bank"""
    doc.save(ignore_permissions=True)