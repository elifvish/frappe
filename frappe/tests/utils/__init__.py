import logging

import frappe

logger = logging.Logger(__file__)

from .generators import *


def check_orpahned_doctypes():
	"""Check that all doctypes in DB actually exist after patch test"""
	from frappe.model.base_document import get_controller

	doctypes = frappe.get_all("DocType", {"custom": 0}, pluck="name")
	orpahned_doctypes = []

	for doctype in doctypes:
		try:
			get_controller(doctype)
		except ImportError:
			orpahned_doctypes.append(doctype)

	if orpahned_doctypes:
		frappe.throw(
			"Following doctypes exist in DB without controller.\n {}".format("\n".join(orpahned_doctypes))
		)


from frappe.deprecation_dumpster import (
	tests_change_settings as change_settings,
)
from frappe.deprecation_dumpster import (
	tests_debug_on as debug_on,
)
from frappe.deprecation_dumpster import (
	tests_FrappeTestCase as FrappeTestCase,
)
from frappe.deprecation_dumpster import (
	tests_IntegrationTestCase as IntegrationTestCase,
)
from frappe.deprecation_dumpster import (
	tests_patch_hooks as patch_hooks,
)
from frappe.deprecation_dumpster import (
	tests_timeout as timeout,
)
from frappe.deprecation_dumpster import (
	tests_UnitTestCase as UnitTestCase,
)
