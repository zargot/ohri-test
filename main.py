"""OHRI test."""

from typing import TypeVar

T = TypeVar('T')

def type_name(x) -> str:
    t = type(x)
    if t == str:
        return "string"
    if t == int:
        return "number"

def validate(data, schema: dict[str, T]) -> [str]:
    """Return a list of errors contained in data after validating with schema.
    An empty list means success.

    :param data: One row of column names and values
    :param schema: Column names and types
    """
    errors = [str]
    unused_columns = list(schema.keys())
    for col, val in data.items():
        col_kind = schema.get(col, None)
        if col_kind is None:
            errors.append(f"invalid column `{col}`")
            continue
        unused_columns.remove(col)
        val_kind = type_name(val)
        if val_kind != col_kind:
            errors.append(f"invalid type for column `{col}`: "
                          f"expected {col_kind}, got {val_kind}")
    for col in unused_columns:
        errors.append(f"missing column `{col}`")
    return errors

def test():
    schema = {
        "email": "string",
        "phone": "number",
        "address": "string"
    }
    data_tests = [
        {},
        {
            "email": "test@email.com",
            "phone": "12345",
            "address": "123 Test Way"
        },
        {
            "email": "test@email.com",
            "phone": 12345,
            "address": "123 Test Way",
            "postalCode": "K6D789"
        },
    ]
    for i, data in enumerate(data_tests):
        print(i+1)
        print(validate(data, schema))

if __name__ == "__main__":
    test()
