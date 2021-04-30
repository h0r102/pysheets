from pysheets.sheet import _Sheet


class Sheet(_Sheet):
    def __init__(self, **kw):
        super(Sheet, self).__init__(kw)
