import pandas as pd
import matplotlib.pyplot as plt

## Colours

colours = pd.read_csv("data/colors.csv")

count = colours.nunique()

istrans = colours.groupby('is_trans').count()

#print(colours)
#print(count)
#print(istrans)


## Sets

sets = pd.read_csv("data/sets.csv")

first = sets.sort_values("year").head()

countOf = sets[sets["year"] == 1949]

parts = sets.sort_values("num_parts", ascending=False).head()

#print(first)
#print(countOf)
#print(parts)

sets_by_year = sets.groupby("year").count()

print(sets_by_year.head())

## Structuring the graph
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

for column in sets_by_year:
    plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2],
             linewidth=3)

plt.show()

## Themes