---
title: Pymaxmusic
weight: 25
pre: "<b>1. </b>"
---

# PYMAXMUSIC

##### Author: [Daniel Brown](http://www.danielbrownmusic.com)

  
PyMaxMusic is a simple framework for communication between Python and Max/MSP, with an emphasis on real-time music generation.  
  

It can either be viewed as a way to use Max/MSP as an interface for controlling a music composition system written in Python, or, conversely, as a way to control Max/MSP patches using Python. The first way is better for note-based (“traditional”) music generation, the second way is better for electroacoustic music.  
  
Pymax is designed around two ideas:

+ First, Python generators are called by the Pymax system to produce events (notes or sounds) over time. You can make these events tempo-dependent or not.

+ Second, objects that you declare in your Python code can be reflected by Max objects which allow you to get and set object variables and call object methods.

This way, Python objects can be used as “controls” which manipulate the parameters of the events that the generators create. Create any number of Python classes to act as controls, and then any number of generators that take instances of these classes to their constructors. The generators will produce events in Max over time, whose parameters you can via the Max interfaces to the “control” objects.

This is a very simple architecture that allows you to write music-generation systems cleanly and easily, focusing on the process of creating music.


Python is fantastic for building systems with very complicated architectures. If you’re comfortable with command-line coding, you can write in just a few lines an algorithm that would require a lot of patching in a visual language like Max. And Python has piles of libraries that do anything you want. You can use all the capabilities of Python to compose musical material, and then send it to Max for playback. And then, of course, you can use all of MSP’s fantastic audio capabilities to make your notes sound great.  
  
Python is not fast enough for DSP, so neither is PyMaxMusic. Audio processing is done tens of thousands of times a second. But musical information moves at a different, much slower rate than audio. Really fast musical events may occur between ten or so times a second, but often take several seconds to occur.  
  
In essence, PyMaxMusic treats Python as the composer, and Max/MSP as the performer. 


