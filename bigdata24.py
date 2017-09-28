import requests

def get_encoding_from_headers(headers):
    """Returns encodings from given HTTP Header Dict.
    :param headers: dictionary to extract encoding from.
    """
    content_type = headers.get('content-type')
    if not content_type:
        return None
    content_type, params = cgi.parse_header(content_type)
    if 'charset' in params:
        return params['charset'].strip("'\"")
    if 'text' in content_type:
        return 'ISO-8859-1'

def monkey_patch():
    prop = requests.models.Response.content
    def content(self):
        _content = prop.fget(self)
        if self.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(_content)
            if encodings:
                self.encoding = encodings[0]
            else:
                self.encoding = self.apparent_encoding
            _content = _content.decode(self.encoding, 'replace').encode('utf8', 'replace')
            self._content = _content
        return _content
    requests.models.Response.content = property(content)

def otherway(rep):
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
    if encodings:
        encoding = encodings[0]
    else:
        encoding = req.apparent_encoding
encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')

monkey_patch()