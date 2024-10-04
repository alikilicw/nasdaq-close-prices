from stock_prices import get_stock_prices
from workbook import get_workbook
from datetime import datetime, timezone

def main_service():
    # get workbook instance and implement formatting
    workbook = get_workbook()
    sheet = workbook.worksheet('Sheet1')
    sheet.format('', {'textFormat': {'bold': True}})
    sheet.format('', {'horizontalAlignment': 'LEFT'})

    # if A1 cell is empty, the doc will be fill at the first time.
    first_time = False
    if sheet.cell(1, 1).value is None:
        first_time = True
        sheet.update_cell(1, 1, 'NAME')

    # get stock prices
    stock_prices = get_stock_prices()

    # in order to align column day by day.
    column_coordinats = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z', 'AA', 'AB', 'AC', 'AD', 'AE','AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ']

    # find out current column and write current date
    current_column = ''
    for column in column_coordinats:
        if sheet.acell(f'{column}1').value is None:
            sheet.update_acell(f'{column}1', str(datetime.now(timezone.utc).date()))
            current_column = column
            break

    # if it's first time, fill the first column with names
    if first_time:
        names = list(stock_prices.keys())
        cell_range = f'A2:A{len(names) + 1}'
        sheet.update(range_name=cell_range, values=[[name] for name in names])

    # write stock prices
    prices = list(stock_prices.values())
    cell_range = f'{current_column}2:{current_column}{len(prices) + 1}'
    sheet.update(range_name=cell_range, values=[[price] for price in prices])