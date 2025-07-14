from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()       
        self.result = []
        self._newline_tags = {"p", "br", "li", "div"}

    def handle_starttag(self, tag, attrs):
        if tag in self._newline_tags:
            self.result.append("\n")

    def handle_endtag(self, tag):
        if tag in self._newline_tags:
            self.result.append("\n")

    def handle_data(self, data):
        self.result.append(data)

    def get_text(self):
        return "".join(self.result)
  
    @staticmethod
    def strip_html(text):
        if not isinstance(text, str):
            return ""

        parser = HTMLTextExtractor()
        parser.feed(text)
        clean = parser.get_text()

        replacements = {
            '\u2014': '-',   # em dash
            '\u2013': '-',   # en dash
            '\u2018': "'",   # left single quote
            '\u2019': "'",   # right single quote
            '\u201c': '"',   # left double quote
            '\u201d': '"',   # right double quote
            '\xa0': ' ',     # non-breaking space
        }

        for k, v in replacements.items():
            clean = clean.replace(k, v)

        lines = [line.strip() for line in clean.splitlines()]
        return "\n".join(filter(None, lines)).strip()