# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("./input_inventory.csv")

# Need to strip whitespace from data frame
# https://www.geeksforgeeks.org/pandas-strip-whitespace-from-entire-dataframe/

# Default value of display.max_rows is 10 i.e. at max 10 rows will be printed.
# Set it None to display all rows in the dataframe
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def csv_strip_whitespace():
    for i in data.columns:
        data[i] = data[i].str.strip()
    return data


# calling head() method
# storing in new variable
data_top_striped = csv_strip_whitespace().head()


# convert dataframe content to lowercase
def csv_lowercase():
    for i in data.columns:
        data[i] = data[i].str.lower()
    return data

# calling head() method
head_lowercase_data = csv_lowercase().head()
print('Lowercase data frame /n'
      ' {}'.format(head_lowercase_data))

print('Lowercase data frame /n')
print(csv_lowercase())
#
lowercase_data = csv_lowercase()
print('Lowercase data frame /n')

print('Stripped whitespace from data frame /n')



