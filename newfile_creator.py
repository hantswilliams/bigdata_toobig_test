import pandas as pd 

## lets create a fake file that is too big for github
df = pd.DataFrame({
    'A': range(100000000),
    'B': range(100000000, 200000000),
})

df.to_csv('bigfile.csv', index=False)


