# Third Party
from pyspark.sql import SparkSession
from pytest import fixture

# Our Libraries
from projectname.core import my_spark_function

# About pytest fixtures
# https://docs.pytest.org/en/latest/how-to/fixtures.html#how-to-fixtures


@fixture
def spark():
    """Start a local pyspark instance to test against."""
    # Setup
    spark = SparkSession.builder.appName(__name__).getOrCreate()

    yield spark

    # Tear down
    spark.stop()


def test_spark_starts(spark):
    # Given
    df = spark.read.csv("data/iris.csv")

    # When
    result = my_spark_function(spark, df)

    # Then
    assert result.count() == 151
