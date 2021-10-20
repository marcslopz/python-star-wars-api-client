""" HttpBin interface class
"""


class HttpBinApiInterface:
    """HttpBin interface class"""

    BASE_URL = "https://httpbin.org/post"

    def send_string_as_file(self, filename: str, content: str) -> int:
        """Send a string as file to HttpBin

        Args:
            filename: file name of the content in httpbin service
            content: content of file to be sent

        Returns:
            status_code returned by httpbin.org
        """
        raise NotImplementedError
