"""Pytest fixtures for Databricks tests."""

import csv
import json
import pathlib

import pytest
from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession


@pytest.fixture()
def spark() -> SparkSession:
    """Create a Databricks Spark session only for tests that need Spark."""
    return DatabricksSession.builder.getOrCreate()


@pytest.fixture()
def load_fixture(spark: SparkSession):
    """Load JSON or CSV test data from the fixtures directory."""

    def _loader(filename: str):
        path = pathlib.Path(__file__).parent.parent / "fixtures" / filename
        suffix = path.suffix.lower()

        if suffix == ".json":
            rows = json.loads(path.read_text())
            return spark.createDataFrame(rows)

        if suffix == ".csv":
            with path.open(newline="") as f:
                rows = list(csv.DictReader(f))
            return spark.createDataFrame(rows)

        raise ValueError(f"Unsupported fixture type for: {filename}")

    return _loader
