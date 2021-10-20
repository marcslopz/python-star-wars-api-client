""" HttpBin implementation with requests library
"""
import requests

from python_star_wars_api_client.domain.interfaces.httpbin import HttpBinApiInterface


class HttpBinWithRequests(HttpBinApiInterface):
    """HttpBin implementation with requests library"""

    def send_string_as_file(self, filename: str, content: str) -> int:
        """Send a string as file to HttpBin

        Args:
            filename: file name of the content in httpbin service
            content: content of file to be sent

        Returns:
            status_code returned by httpbin.org
        """
        files = {"file": (filename, content)}
        response = requests.post(self.BASE_URL, files=files)
        return response.status_code
