---
title: Playing Notes
weight: 20
---

If you’re working with notes a lot, you can use the pynote object instead of the pygen object to pend out note information. In this case, your Python generator needs to be a list of five elements in this order:
```python
[ ontime, pitch, velocity, duration, channel ]
```
That is, the ontime first (which is what Pymax needs), followed by the fields used by the “makenote” and “noteout” Max objects. The pynote object just wraps the pygen object and a makenote object so that the output can be easily sent to a noteout object. 
One more nice thing about using the pynote object is that you can give your note duration in beats, just like your ontime. So a loud middle C eighth note starting immediately would be:
```python
[ 0.0, 60, 100, .5, 1]
```
And a loud middle C sixteenth note starting immediately would be:
```python
[ 0.0, 60, 100, .25, 1]
```
The second (middle) inlet of the pygen object takes messages. So far the only message you can send it is “reset.” This will reset the generator so that it will start from the beginning (under the hood: it just constructs a new generator function based on the arguments you gave it in pymax.add_generator()).