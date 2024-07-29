def find_outliers_IQR(df): # dataframe
   q1=df.quantile(0.25)
   q3=df.quantile(0.75)

   IQR=q3-q1

   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))] # actual definition, we need greater than Q3
# if you want values in the upper 75th percentile
#    o_75 = df[(df>(q3))]

   return outliers

# usage 
wt_o_75 = find_outliers_IQR(df["column_name"])