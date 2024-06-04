import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
df.DATE = pd.to_datetime(df["DATE"])
## Total number of posts 
#print(df.groupby("TAG").sum())
## Total number of months
#print(df.groupby("TAG").count())

##print(type(df["DATE"][1]))
#print(dates)
#print(type(dates))

## Pivoting a table
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
roll_df = reshaped_df.rolling(window=6).mean()

#print(reshaped_df)

## Structuring the graph
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0,35000)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)

## Ploting the data onto the table
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)
    
plt.legend(fontsize=16)

plt.show()