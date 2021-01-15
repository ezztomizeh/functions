def Convert(df):
  col = list(df.columns)
  for i in range(len(col)):
    y = df[col[i]]
    x = list(y)
    for j in range(len(x)):
      if x[j] >= 95 : x[j] = 'A+'
      if x[j] < 95 and x[j] >= 90 : x[j] = 'A-'
      if x[j] < 90 and x[j] >= 85 : x[j] = 'B+'
      if x[j] < 85 and x[j] >= 80: x[j] = 'B-'
      if x[j] < 80 and x[j] >= 75: x[j] = 'C+'
      if x[j] < 75 and x[j] >= 70: x[j] = 'C-'
      if x[j] < 70 and x[j] >= 65: x[j] = 'D+'
      if x[j] < 60 and x[j] >= 50: x[j] = 'D-'
      else : x[j] = 'F'
    df[col[i]] = x
  
  return df
