class URLChecker:

    @classmethod
    def is_valid_url(cls, url):
        if url.lower().startswith('http://') and url.endswith(' ') and url.find('.'):
            return True
        else:
            return False
