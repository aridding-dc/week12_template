# Import Libraries
import pandas as pd

##################################
#TODO: Best selling platform for NA/EU and JP
#TODO: Visualize Call of Duty Sales, in North America by Platform
##################################


# Read CSV
raw_data = pd.read_csv('Week 8 - vgsales.csv')

# Create Function
def best_seller(df, agg_col):
  """
  This function creates a groupby by a user-specified column and
  returns the sorted df. 

  df = a dataframe you would like to transform. 
  agg_col = what column would you like to perform the aggregate on? 
  """
 #  Reset index to allow for iloc
  best_seller_df = df.groupby('Genre')[agg_col].mean().reset_index()
  best_seller_df = best_seller_df.sort_values(agg_col, ascending=False)
  return best_seller_df

# Apply function to different regions
best_selling_na = best_seller(raw_data, "NA_Sales")
best_selling_eu = best_seller(raw_data, "EU_Sales")
best_selling_jp = best_seller(raw_data, "JP_Sales")

# Return a statement depicting the top genre. 
print("The best selling genre in NA is {}".format(best_selling_na.iloc[0,0]))
print("The best selling genre in EU is {}".format(best_selling_eu.iloc[0,0]))
print("The best selling genre in JP is {}".format(best_selling_jp.iloc[0,0]))