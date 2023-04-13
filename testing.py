import pandas as pd
import matplotlib.pyplot as plt

testing_df = pd.DataFrame()

values = [1,2,3]
names = ["Hristo", "Vristo", "Tristo"]

testing_df["values"] = values
testing_df["names"] = names
print(testing_df)

dict_comp = {name:len(name) for name in names}
print(dict_comp)

numbers = range(10)
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print(new_dict_comp)