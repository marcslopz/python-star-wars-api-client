""" HttpBinSender is the application service used to send data to httpbin

"""
from python_star_wars_api_client.domain.interfaces.httpbin import HttpBinApiInterface


class HttpBinSender:
    """HttpBinSender application service"""

    def __init__(self, httpbin_class: HttpBinApiInterface):
        self.httpbin_class = httpbin_class()

    def send_file(self, filename: str, content: str) -> int:
        """Sends file content to httpbin

        Args:
            filename: file name of the content in httpbin service
            content: content of file to be sent

        Returns:
            status_code returned by httpbin.org
        """
        return self.httpbin_class.send_string_as_file(filename, content)
