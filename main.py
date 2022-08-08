""" Pandas Data Cleaning Example Script """
import uuid
from typing import Iterable
import pandas
from pandas import DataFrame


def read_csv(filepath: str) -> DataFrame:
    return pandas.read_csv(filepath)


def save_csv(filepath: str, data: DataFrame):
    data.to_csv(filepath)


def remove_headers(data: DataFrame, drop_list: Iterable[str]) -> DataFrame:
    return data.drop(columns=drop_list)


def rename_headers(data: DataFrame, column_names) -> DataFrame:
    return data.rename(columns=column_names)


def set_uuid_index(data: DataFrame) -> DataFrame:
    data["id"] = [uuid.uuid4() for _ in range(data.shape[0])]
    return data.set_index("id")


if __name__ == '__main__':
    df = read_csv("dirty-data.csv")
    df = set_uuid_index(df)
    df = remove_headers(df, ["bad-header-1", "bad-header-2"])
    save_csv("clean-data.csv", df)
