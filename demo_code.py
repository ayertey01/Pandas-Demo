import pandas as pd

#data frames using the 'df'.
df = pd.read_csv('file directory')
df
# using an attribute to find the number of columbs and rows
df.shape
#using the .info() to provide information about the csv file
df.info()
#to display all the columbs use
pd.set_option('display.max_columns', number_of_column)
#using a schema 
schema_df= pd.read_csv('directory')
schema_df
#the use of head and tail can be incorporated in  the code 
schema_df.tail(10)
#showing last 10 of the schema
shema_df.head(10)
#showing first 5 of the schema
