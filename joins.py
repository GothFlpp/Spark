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

data_proc = "2021-02-22 13:00:00"

df1 = (
    spark.createDataFrame([row1, row2, row3, row4, row5, row6])
        .withColumn("data", (lit("9902")))
        .withColumn("unix", unix_timestamp("data", "yyMM"))
)

df1.show()




df2 = spark.createDataFrame([row4, row5, row6])

df3 = spark.createDataFrame([row1, row2, row3])

key12 = df1["id"] == df2["id"]
key23 = df2["id"] == df3["id"]
key233 = coalesce(df2["id"], df1["id"]) == df3["id"]

df_join = (
    df1
        .join(df2, key12, "full_outer")
        .join(df3, key233, "full_outer")

)

df_join.show()

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