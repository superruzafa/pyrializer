# Pyrializer

A Python object (de)serializer

## Installation

~~~
$ pip install pyrializer
~~~

## Basic usage

You must define classes and describe what attributes and their types using
class attributes like this:

~~~ python
class Person
  name = str
  age = int
  gender = str
~~~

See [Supported types](#supported-types) below.


### Decoding from a serialized value

Decoding an object maps a serialized value into a Python object:

~~~ python
from pyrializer import decode

payload = {
  'name': 'John Doe',
  'age': 52,
  'job': {
    'name': 'Software Engineer',
    'salary': 24000
  },
  'hobbies': ['fishing', 'skating']
}

class Job:
  name = str
  role = str
  salary = int

class Address:
  desc = str
  city = str
  country = str
  zip = int

class Person:
  name = str
  age = int
  job = Job
  hobbies = [str]
  address = Address

person = decode(Person, payload)

person.name          # John Doe
person.job.salary    # 24000
person.job.role      # None
person.hobbies[1]    # skating
person.address.city  # None
~~~


### Encoding to a serialized value

Encoding an object transform a Python object into a serializable format that can
be easily exported to others formats, such as JSON:

~~~ python
from pyrializer import encode

encode(Person, person) # --> { 'name': 'John Doe', ... }
~~~

Additionaly, you can decorate the classes you want to (de)serialize with the
```serializable``` decorator. This decorator extends the classes with two
additional methods:

~~~ python
from pyrializer import serializable

@serializable
class Person:
  ...

person = Person.decode(person_payload)

person.encode() # --> { 'name': 'John Doe', ... }
~~~


## Supported types

Here is some examples of supported types

| \<type>       | JSON equivalent                               |
|---------------|-----------------------------------------------|
| `None`        | Any type                                      |
| `str`         | String                                        |
| `int`         | Integer                                       |
| `float`       | Float                                         |
| `bool`        | Boolean                                       |
| `[]`          | Array of any type                             |
| `ClassName`   | Object                                        |
| _Custom type_ | Any. See [Custom types](#custom-types) below. |

More advanced examples:

~~~ python
class Example:
  array_of_array_of_ints = [ [ int ] ]  # [ [1,2], [3, 4], [], [5, 6] ]
  whatever = None  # 42, False, AnotherObject(), etc...
~~~


## Custom types

Custom types allows to decode values that have been previously encoded using a
primitive type and in a convenience format.

Some examples include:
- Unix timestamps: Dates encoded as integers
- ISO-8601: Dates encoded as strings
- Gender: Male or female encoded as booleans

To declare a Custom Type you need to create a class that inherit the `CustomType`
and define two methods: `decode` and `encode`.

For example, the following snippets declares a custom type to decode an ISO-8601
date into a Python's datetime object and vice versa.

~~~ python
from json import loads
from datetime import datetime
from pyrializer import serializable
from pyrializer.types import CustomType

class ISO_8601(CustomType):
    def decode(self, fvalue):
        return datetime.strptime(fvalue, '%Y-%m-%dT%H:%M:%SZ')

    def encode(self, fvalue):
        return datetime.strftime(fvalue, '%Y-%m-%dT%H:%M:%SZ')

@serializable
class Person:
    name = str
    birthdate = ISO_8601  # here we use the custom type

json_payload = json_loads('''
{
    "name": "John Doe",
    "birthdate": "1984-01-23T09:37:21Z"
}
''')

person = Person.decode(payload)

print(type(person.birthdate))  # <class 'datetime.datetime'>
print(person.birthdate.year)   # 1984

print(person.encode())         # {'name': 'John Doe', 'birthdate': '2000-01-23T09:37:21Z'}
~~~
