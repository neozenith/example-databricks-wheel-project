# Standard Library
import sys
from pathlib import Path
from typing import List

# Third Party
from pyspark.sql import DataFrame, SparkSession


def main():
    """Entrypoint for running as a module or a Databricks job."""
    spark = SparkSession.builder.getOrCreate()

    # Hook into underlying log4j logger
    log4jLogger = spark._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger(__name__)
    logger.setLevel(log4jLogger.Level.WARN)

    # Possibly use argparse here for more advanced arg processing
    my_spark_program(spark, list(sys.argv))


def my_spark_program(spark: SparkSession, args: List[str]):
    """Main entrypoint for Spark job."""
    print(args)
    #  # Data IN
    #  source_filename = args[1]
    #  df = spark.read.csv(source_filename)
    #
    #  # Process
    #  result = my_spark_function(spark, df)
    #
    #  # Data OUT
    #  output_path = str(Path(source_filename).parent / "output.parquet")
    #  result.write.parquet(output_path)


def my_spark_function(spark: SparkSession, df: DataFrame) -> DataFrame:
    """Pipeline step to transform DataFrame in, to DataFrame out."""
    return df
