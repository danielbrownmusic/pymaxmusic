---
title: add_object
weight: 10
---

#### pymax.add_object( &lt; object_name &gt;, &lt; object &gt;  )

	&lt; object_name&gt;  : string
	A string that will be used in Max/MSP to call the object.
&lt; object&gt; 
The object to be called.

Adds an already constructed object to the Pymax system, giving it the given object name, which the Max pyobj will use to call this object.
For example, the following code will add foo, an instance of class Foo, to the system. In Max/MSP, you can create an object with pyobj foo_name, which will accept the messages get a  and set a &lt; value &gt; :

class Foo():
    def __init__(self):
        self.bar = 2
 
foo_instance = Foo()
pymax.add_object(“foo_name”, foo )
