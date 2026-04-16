from odoo import http
from odoo.http import request


class SaleDashboardController(http.Controller):

    @http.route('/sales/dashboard/data', type='json', auth='user')
    def get_data(self, date_from=None, date_to=None):
        from odoo import http
from odoo.http import request


class SaleDashboardController(http.Controller):

    @http.route('/sales/dashboard/data', type='json', auth='user')
    def get_data(self, date_from=None, date_to=None):
        """
        Fetch sales order data for the Sales Dashboard.

        This endpoint is used by the frontend (OWL component) to retrieve
        sales order details based on an optional date range filter. It returns
        a list of sales orders with basic information such as order name,
        customer, total amount, and order date.

        Parameters:
            date_from (str, optional): Start date in 'YYYY-MM-DD' format.
                Filters sales orders created on or after this date.
            date_to (str, optional): End date in 'YYYY-MM-DD' format.
                Filters sales orders created on or before this date.

        Returns:
            list[dict]: A list of dictionaries where each dictionary contains:
                - id (int): Sales order ID
                - name (str): Sales order reference
                - customer (str): Customer name
                - total (float): Total amount of the order
                - date (str): Order date (string format)

        Notes:
            - Uses `sudo()` to ensure data access regardless of user restrictions.
            - Intended for real-time or polling-based dashboard updates.
            - If no date range is provided, backend logic may default
              to recent records (e.g., last 15 days).

        """
        return request.env['sale.dashboard'].sudo().get_sales_data(date_from, date_to)