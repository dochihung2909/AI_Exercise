import pandas

df = pandas.read_table('04_gap-merged.tsv')


# 1./ Show the first 5 lines of tsv file.
def show_5_line(file):
    print(file.head(5))


# 2./ Find the number of row and column of this file.
def find_number_row_col(file):
    print(f'Number of rows: {len(file.axes[0])} rows')
    print(f'Number of columns: {len(file.axes[1])} columns')


# 3/ Print the name of the columns.
def print_name_col(file):
    for col in file.columns:
        print(col)


# 4/ What is the type of the column names?
def print_type_col(file):
    print(file.dtypes)


# 5/ Get the country column and save it to its own variable. Show the first 5 observations.
# 6/ Show the last 5 observations of this column.
def print_country(file):
    countries = file['country']
    print(f'First 5 observations\n{countries.head(5)}')
    print(f'Last 5 observations\n{countries.tail(5)}')


# 7/ Look at country, continent and year. Show the first 5 observations of these columns, and the last 5 observations.
def print_three_col(file):
    data = file[['country', 'continent', 'year']]
    print(f'First 5 observations\n{data.head(5)}')
    print(f'Last 5 observations\n{data.tail(5)}')


# 8/ How to get the first row of tsv file? How to get the 100th row.
def print_first_row(file):
    print(f'First row\n{file.iloc[0]}')
    print(f'100th row\n{file.iloc[99]}')


# 9/ Try to get the first column by using a integer index. And get the first and last column by passing the integer index.
def print_first_col_by_interger(file, col_num=0):
    print(file.iloc[:, col_num])


# 10/ How to get the last row with .loc? Try with index -1? Correct?
def get_last_row_with_loc(file):
    # -1 will get the last index
    print(file.loc[file.index[-1]])


# 11/ How to select the first, 100th, 1000th rows by two methods?
def get_by_two_method(file):
    print(f'First\n{file.loc[file.index[0]]}')
    print(f'100th\n{file.iloc[99]}')
    print(f'1000th\n{file.iloc[999]}')


# 12/ Get the 43rd country in our data using .loc, .iloc?
def print_43rd(file):
    print(f'.loc method\n{file.loc[42]}')
    print(f'.iloc method\n{file.iloc[42]}')


# 13/ How to get the first, 100th, 1000th rows from the first, 4th and 6th columns?
def print_in_4th_6th_col(file, col_num=3):
    print(f'First\n{file.iloc[0, col_num]}')
    print(f'100th\n{file.iloc[99, col_num]}')
    print(f'1000th\n{file.iloc[999, col_num]}')


# 14/ Get first 10 rows of our data (tsv file)?
def show_10_rows(file):
    print(file.head(10))


# 15/ For each year in our data, what was the average life expectation?
def average_life(file):
    print(file['year'].mean())


# 17/ Create a series with index 0 for ‘banana’ and index 1 for ’42’?
def pandas_series():
    d = ['banana', 42]
    pds = pandas.Series(data=d, index=['Wes MCKinney', 'Creator of Pandas'])
    print(pds)


# 19/ Create a dictionary for pandas with the data as ‘Occupation’: [’Chemist’, ’Statistician’], ’Born’: [’1920-07-25’, ’1876-06-13’],’Died’: [’1958-04-16’, ’1937-10-16’],’Age’: [37, 61] and the index is ‘Franklin’,’Gosset’ with four columns as indicated.
def pandas_series_dictionary():
    d = {
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]
    }
    pds = pandas.DataFrame(data=d, index=['Franklin', 'Gosset'])
    print(pds)


if __name__ == '__main__':
    pandas_series_dictionary()
