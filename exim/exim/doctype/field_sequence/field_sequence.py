# Copyright (c) 2023, FinByz Tech Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FieldSequence(Document):
	# def before_save(self):
	# 	if frappe.db.exists('Property Setter', {'doc_type': self.doc_type, "property": "field_order"}):
	# 		del_doc_name = frappe.db.get_value('Property Setter', {'doc_type': self.doc_type, "property": "field_order"}, 'name')
	# 		frappe.delete_doc('Property Setter', del_doc_name)
	
	def validate(self):
		for row in self.get('field_sequence_table'):
			row.doc_type = self.doc_type
			if row.field_name == self.add_fields_before_section:
				frappe.throw("You can't select the <b>" +row.field_name+"</b> in the Field Sequence Table.")
	
	def on_update(self):
		if self.apply_changes:
			doc = frappe.get_doc("Customize Form")
			doc.doc_type = self.doc_type
			doc.fetch_to_customize()
			doc.save_customization()

		self.apply_changes = 0
