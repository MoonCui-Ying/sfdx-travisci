from util import get_rundate
from db import Spreadsheet

def main():
    RUNDATE = get_rundate()
    sheet = Spreadsheet(path='CodeCoverage_{}.xlsx'.format(RUNDATE))
    sheet.open()
    sheet.close()

if __name__ == '__main__':
    main()