# my_loan_plugin/plugin.py

from plugin import InvenTreePlugin
from plugin.mixins import AppMixin, UrlsMixin, NavigationMixin, ReportMixin

class MyLoanPlugin(
    AppMixin,
    UrlsMixin,
    NavigationMixin,
    ReportMixin,
    InvenTreePlugin
):
    """
    Custom InvenTree plugin for managing item loans.
    """

    NAME = "my_loan_plugin"
    SLUG = "my_loan_plugin"
    TITLE = "Item Loan Plugin"
    AUTHOR = "Your Name"
    VERSION = "1.0.0"
    DESCRIPTION = "Plugin to manage item loans, agreements, and returns."

    def setup(self):
        """
        Called by InvenTree after the plugin is loaded.
        You could perform any plugin-specific initialization here.
        """
        pass

    # --- NavigationMixin ---
    def nav_bar_entries(self, request):
        """
        Return a list of tuples (entry_name, url) for the left navigation bar.
        """
        return [("Item Loans", self.plugin_url())]

    # --- UrlsMixin ---
    def get_urls(self):
        """
        Return custom URL patterns for this plugin.
        """
        # Import here to avoid circular imports
        from .urls import urlpatterns
        return urlpatterns

    # --- ReportMixin (Optional Example) ---
    # If you want to generate a PDF or document for loan agreements,
    # define or override relevant methods here, referencing a custom
    # HTML template. For example:
    def get_report_templates(self):
        """
        Return a list of template files for creating loan agreements.
        """
        return ["my_loan_plugin/loan_agreement.html"]
