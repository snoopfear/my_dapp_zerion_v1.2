import os
import json
from sys import stderr, exit

import tls_client
import inquirer
import xlsxwriter
from art import text2art
from loguru import logger
from termcolor import colored
from inquirer.themes import load_theme_from_dict as loadth


# FILES SETTINGS
cwd = os.getcwd()
file_data1 = f'{cwd}/files/database1.json'
file_data2 = f'{cwd}/files/database2.json'
file_query1 = f'{cwd}/files/query1.json'
file_query2 = f'{cwd}/files/query2.json'
file_query3 = f'{cwd}/files/query3.json'
file_wallets = f'{cwd}/files/wallets.txt'
file_excel_table = f'{cwd}/LayerZero Stats.xlsx'

# LOGGING SETTING
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")

WALLETS = []
QUERY1 = 2464151
QUERY2 =  2492847
