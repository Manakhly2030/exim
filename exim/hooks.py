# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "exim"
app_title = "Exim"
app_publisher = "FinByz Tech Pvt Ltd"
app_description = "custom app for exim module"
app_icon = "fa fa-ship"
app_color = "#61b590"
app_email = "info@finbyz.com"
app_license = "GPL 3.0"
app_version = "3.1.0"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/exim/css/exim.css"
# app_include_js = "/assets/exim/js/exim.js"

# include js, css files in header of web template
# web_include_css = "/assets/exim/css/exim.css"
# web_include_js = "/assets/exim/js/exim.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
    "Sales Order": "public/js/doctype_js/sales_order.js",
    "Sales Invoice": "public/js/doctype_js/sales_invoice.js",
    "Delivery Note": "public/js/doctype_js/delivery_note.js",
    "Purchase Receipt": "public/js/doctype_js/purchase_receipt.js",
    "Purchase Invoice": "public/js/doctype_js/purchase_invoice.js",
    "Purchase Order": "public/js/doctype_js/purchase_order.js",
    "Lead": "public/js/doctype_js/lead.js",
    "Payment Entry": "public/js/doctype_js/payment_entry.js",
    "Customize Form": "public/js/doctype_js/customize_form.js",
}

# after_migrate = ["exim.exim.doc_events.update_field_order.after_migrate"]

# fixtures = ["Custom Field"]
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "exim.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "exim.install.before_install"
# after_install = "exim.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "exim.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"exim.tasks.all"
# 	],
# 	"daily": [
# 		"exim.tasks.daily"
# 	],
# 	"hourly": [
# 		"exim.tasks.hourly"
# 	],
# 	"weekly": [
# 		"exim.tasks.weekly"
# 	]
# 	"monthly": [
# 		"exim.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "exim.install.before_tests"

# override_doctype_class = {
# }

# payment term override
from exim.api import get_due_date
from erpnext.controllers import accounts_controller

accounts_controller.get_due_date = get_due_date

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "exim.event.get_events"
# }
# fixtures = ["Custom Field"]

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["module", "in", ["Exim"]],
        ],
    },
    {"dt": "Property Setter", "filters": [["module", "in", ["Exim"]]]},
    # {"dt": "Field Sequence", "filters": [["module", "in", ["Exim"]]]},
]
# override_whitelisted_methods = {
# 	"frappe.utils.print_format.download_pdf": "exim.print_format.download_pdf",
# }

doc_events = {
    "Sales Invoice": {
        "before_save": "exim.exim.doc_events.sales_invoice.before_save",
        "validate": "exim.exim.doc_events.sales_invoice.validate",
        "on_submit": "exim.exim.doc_events.sales_invoice.on_submit",
        "on_cancel": "exim.exim.doc_events.sales_invoice.on_cancel",
    },
    "Purchase Invoice": {
        "on_submit": "exim.api.pi_on_submit",
        "on_cancel": "exim.api.pi_on_cancel",
    },
    (
        "Purchase Invoice",
        "Payment Request",
        "Payment Entry",
        "Journal Entry",
        "Material Request",
        "Purchase Order",
        "Work Order",
        "Production Plan",
        "Stock Entry",
        "Quotation",
        "Sales Order",
        "Delivery Note",
        "Purchase Receipt",
        "Packing Slip",
    ): {
        "before_naming": "exim.api.docs_before_naming",
    },
    "Rodtep Claim": {
        "on_submit": "exim.exim.doctype.rodtep_claim.rodtep_claim.create_jv_on_submit"
    },
    "Duty DrawBack Claim": {
        "on_submit": "exim.exim.doctype.duty_drawback_claim.duty_drawback_claim.create_jv_on_submit"
    },
    "Payment Entry": {
        "on_submit": "exim.api.pe_on_submit",
        "before_cancel": "exim.api.pe_on_cancel",
    },
    ("Delivery Note", "Sales Invoice"): {
        "validate": "exim.exim.doc_events.igst_calculation.cal_igst"
    },
}
