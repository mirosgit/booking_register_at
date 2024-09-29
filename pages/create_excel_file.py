import openpyxl


class DefaultConfig:

    input_xlsx_name_file = "TestData.xlsx"

    _xlsx_book = openpyxl.reader.excel.load_workbook(filename=input_xlsx_name_file)
    _xlsx_book.active = 0
    _login_data_sheet = _xlsx_book.active

