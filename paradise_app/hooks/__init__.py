from .. import __version__ as app_version
from .route import routes
from .jinja import jenvs
from .doc_events import doc_events

app_name = "paradise_app"
app_title = "Paradise App"
app_publisher = "Montego-Arch"
app_description = "It is a demo app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "okekeemmanuelomolola@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/paradise_app/css/paradise_app.css"
# app_include_js = "/assets/paradise_app/js/paradise_app.js"
app_include_js = "/assets/paradise_app/js/desk.js"

# include js, css files in header of web template
# web_include_css = "/assets/paradise_app/css/paradise_app.css"
# web_include_js = "/assets/paradise_app/js/paradise_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "paradise_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Expense Claim" : "public/js/doctype_plugin/expense_claim.js",
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }
#WEBSITE_ROUTE_RULES

website_route_rules = routes
jenv = jenvs

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "paradise_app.install.before_install"
# after_install = "paradise_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "paradise_app.uninstall.before_uninstall"
# after_uninstall = "paradise_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "paradise_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = doc_events

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"paradise_app.tasks.all"
# 	],
# 	"daily": [
# 		"paradise_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"paradise_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"paradise_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"paradise_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "paradise_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "paradise_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "paradise_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["paradise_app.utils.before_request"]
# after_request = ["paradise_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["paradise_app.utils.before_job"]
# after_job = ["paradise_app.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"paradise_app.auth.validate"
# ]

