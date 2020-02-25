# Pyrializer

A Python object (de)serializer

## Basic usage

You must define classes and describe what attributes and their types using
class attributes like this:

~~~ python
class Example
  field_name = type1
  other_field_name = type2
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

class Person:
  name = str
  age = int
  job = Job
  hobbies = [str]

person = decode(Person, payload)

person.name        # John Doe
person.job.salary  # 24000
person.job.role    # None
person.hobbies[1]  # skating
~~~


### Encoding to a serialized value

Encoding an object transform a Python object into a serializable format that can
be easily exported to others formats, such as JSON:

~~~ python
from serializer import encode

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

| \<type>     | JSON equivalent  |
|-------------|------------------|
| `None`      | Any value        |
| `str`       | String           |
| `int`       | Integer          |
| `float`     | Float            |
| `bool`      | Boolean          |
| `[<type>]`  | Array of \<type> |
| `ClassName` | Object           |

More advanced examples:

~~~ python
class Example:
  array_of_array_of_ints = [ [ int ] ]  # [ [1,2], [3, 4], [], [5, 6] ]
  whatever = None  # 42, False, AnotherObject(), etc...
~~~
