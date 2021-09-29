"""OHRI test."""

from typing import TypeVar

T = TypeVar('T')

def typeName(x) -> str:
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
    unusedColumns = list(schema.keys())
    for col, val in data.items():
        colKind = schema.get(col, None)
        if colKind == None:
            errors.append(f"invalid column `{col}`")
            continue
        unusedColumns.remove(col)
        valKind = typeName(val)
        if valKind != colKind:
            errors.append(f"invalid type for column `{col}`: "
                          f"expected {colKind}, got {valKind}")
    for col in unusedColumns:
        errors.append(f"missing column `{col}`")
    return errors

def test():
    schema = {
        "email": "string",
        "phone": "number",
        "address": "string"
    }
    data_one = {}
    data_two = {
        "email": "test@email.com",
        "phone": "12345",
        "address": "123 Test Way"
    }
    data_three = {
        "email": "test@email.com",
        "phone": 12345,
        "address": "123 Test Way",
        "postalCode": "K6D789"
    }
    print(validate(data_one, schema))
    print(validate(data_two, schema))
    print(validate(data_three, schema))

if __name__ == "__main__":
    test()
