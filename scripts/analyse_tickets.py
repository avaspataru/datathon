import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sold_tickets = pd.read_csv('london_ticket_sales.csv')
print(sold_tickets)

all_tickets = pd.read_csv('london_tickets_for_sale.csv', encoding='latin1')
print(all_tickets)
