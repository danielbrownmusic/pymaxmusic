---
title: add_class
weight: 15
---

#### pymax.add_class( &lt; object_name &gt;, &lt; class &gt;, &lt; arguments to class constructor &gt; )

Constructs a new object of class class_type, passing the given initialization arguments to the class constructor, and puts this object in the Pymax system, giving the object the given object name, which the Max pyobj will use to call this object.

If you don’t need or want to declare an object instance, you can use add_class, which will create a named instance of the class that the Pymax system will use.

For example, the following code creates an instance of class Baz, initialized with arguments 2 and “hello,” which can be called in Max with the object _pyobj baz_:

```python
class Baz():
    def __init__(self, some_int, some_string):
        self.a = some_int
        self.b = some_string

pymax.add_class(“baz”, Baz, 2, “hello”)
```
This does exactly the same thing as

```python
baz = Baz(2, “hello”)
pymax.add_object(“baz”, baz)
```