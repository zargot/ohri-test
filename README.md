# Specification

You will need to write a Python function to validate data. 

## Arguments

1. Data from an SQL table that needs to be validated represented as a Python dictionary. The keys in the dictionary are the column names and the values are the column values.

2. The rules to validate the data provided as a Python dictionary. The keys to the dictionary are the columns expected in the data and values are strings that provide the type that the data should have for that column. For example,

```{python}
{
    "email": "string",
    "phone": "number"
}
```

The above rule dictionary states that the data should have at most two keys called `email` and `phone` and their values should be a string and number respectively.

For now, assume that the types allowed are either `string` or `number`.

## Function Return

The function should return a list of strings which has all the validation errors found in the data. Examples are shown below.

```{python}
# The validation rules we will use for this example
contact_rules = {
    "email": "string",
    "phone": "number",
    "address": "string"
}

# This should return a list with 3 strings telling the user that they are
# missing the columns, email, phone and address
data_one = {}

# This should return a list with 1 error, telling the user that the phone
# column should be a number
data_two = {
    "email":"test@email.com",
    "phone": "12345",
    "address": "123 Test Way"
}

# This should return a list with 1 error, telling the user that the 
# postalCode column should not be there
data_three = {
    "email":"test@email.com",
    "phone": 12345,
    "address": "123 Test Way",
    "postalCode": "K6D789
}
```

You can format the validation messages as you wish making sure that they give enough information to the user to correct the error.

## Validation Requirements

The function should perform the following validations:

1. Make sure that the correct columns are present in the data.
2. Make sure no extra columns are present in it
3. Make sure the column value matches the type specified in the validation rule
