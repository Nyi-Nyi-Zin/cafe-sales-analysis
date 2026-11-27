# Type Annotation

# age: int = 20
# name: str = "Aung"


# def clean_name(name: str):
#     return name.capitalize()


# print(clean_name("aung"))

# main.py =>   Relative Path
# D:\Desktop\cafe_sales_analysis\main.py  => Absolute Path
import pandas as pd

test = pd.DataFrame({
    "sample":["mangon","",566,"apple   ","  "]
})

for column in test.columns:
    blank_count = test[column].str.strip().eq("").sum()
    print(test[column].str.strip().eq("").sum())
  