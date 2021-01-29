"""host:ora_adprd.dc.nova
port:1521
database:ADPRD
username:SRVDATA
pwd:b1gd4t###drc2018
"""
url = "jdbc:oracle:thin:@ora_adprd.dc.nova:1521:ADPRD"
properties = {"user" : "SRVDATA", "password" : "b1gd4t###drc2018"}

df = (
    spark.read.format("jdbc")
        .option("url", url)
        .option("driver", "oracle.jdbc.OracleDriver")
        .option("dbtable", "ac_admin.ecad_order_mis")
        .option("properties", properties)
        .load()
)

export SPARK_CLASSPATH="/home/flpp/Downloads/ojdbc7.jar"
