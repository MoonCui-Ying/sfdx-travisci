import xlsxwriter


class Spreadsheet:
    def __init__(self, path):
        self._path = path
        self._workbook = None
        self._sheet_apex_classes = None
        self._sheet_team_totals = None

    def open(self):
        self._workbook = xlsxwriter.Workbook(self._path)
        self._sheet_apex_classes = self._workbook.add_worksheet('ApexClasses')
        self._sheet_team_totals = self._workbook.add_worksheet('TeamTotals')

    def close(self):
        if self._workbook:
            self._workbook.close()
            self._workbook = None
    