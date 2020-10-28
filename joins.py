from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *
from pyspark.sql import *

row1 = Row(id=1)
row2 = Row(id=2)
row3 = Row(id=3)
row4 = Row(id=4)
row5 = Row(id=5)
row6 = Row(id=6)
row7 = Row(id=7)

df1 = spark.createDataFrame([row1, row2, row3, row4, row5, row6])

df2 = spark.createDataFrame([row4, row5, row6])

key = df1["id"] == df2["id"]

df_left_anti = (
    df1.join(df2, key, "left_anti")
)

df_left_semi = (
    df1.join(df2, key, "left_semi")
)

df_left = (
    df1.join(df2, key, "left")
)

df1.show()
df2.show()
df_left_anti.show()
df_left_semi.show()
df_left.show()