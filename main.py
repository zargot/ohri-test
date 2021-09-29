"""OHRI test."""

from typing import TypeVar

_T = TypeVar('T')

def _type_name(val) -> str:
    t = type(val)
    if t == str:
        return "string"
    elif t == int:
        return "number"
    else:
        return "unknown"

def validate(data, schema: dict[str, _T]) -> [str]:
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
        val_kind = _type_name(val)
        if val_kind != col_kind:
            errors.append(f"invalid type for column `{col}`: "
                          f"expected {col_kind}, got {val_kind}")
    for col in unused_columns:
        errors.append(f"missing column `{col}`")
    return errors

def _test():
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
        {
            "phone": 1.1
        }
    ]
    for i, data in enumerate(data_tests):
        print(i+1)
        print(validate(data, schema))

if __name__ == "__main__":
    _test()
