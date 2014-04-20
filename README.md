# Kivy Widget Area Display

Kivy Widget Area Display is a Python module to help displaying the area of a Kivy widget for solving layout issues.

## Overview

Let's say you are designing a Kivy app and you have several widgets that are not where you intented to put them or their placement or size is otherwise rather unexpected. It would be helpful if you could see exactly where the area of the widget is.

The solution that Kivy offers natively is to use the widget's own canvas to draw a rectangle around itself. To draw a red rectangle around a label, thus showing its placement and size, you would do something like this:

```
<Label>:
  text: 'Hello world'
  canvas:
    Color:
      rgba: 1, 0, 0, 0.5
    Rectangle:
      size: self.size
      pos: self.pos
```

Although consistent, that's not very convenient for bug fixing.
Using KWAD, this does the same thing:

```
<Label>:
  text: 'Hello world'
  a: self.show_area(color='red')
```

Or even shorter:

```
<Label>:
  text: 'Hello world'
  a: self.show_area('r')
```

Note that the 'a' in the previous examples is just a custom attribute and it can be named anything (as long as it is not already defined by Kivy). An attribute with some name is required, as (at least to my knowledge) kv language requires an attribute to be attached to a method.

## Installation

Put the `wadisp.py` file either into your Kivy project directory or into your Python directory's /Lib/site-packages dir.

## Usage

1. Import it into your app with `import wadisp`
2. Call `wadisp.attach()` (a good place to run it is before you call your app's run() method)
3. Call `self.show_area()` inside the class/object whose area you want to be displayed.
  * You can call it in Python side or using the kv language
  * By default, this sets the color to be green
  * You can change the color to red with `self.show_area('r')`, yellow with `self.show_area('y')` and so forth. See the list of supported colors below in the API section. Most of the time this is all you need.

See the widgetareaexample.py for a comprehensive example of usage.

## API

#### `wadisp.attach()`

This function gives the Kivy's Widget class a new method called `show_area()` which is from that point on available for all widgets. You must call this function before using the `show_area()` method.

#### `show_area(color='green', alpha=0.5, group=None)`

After attaching this method with `wadisp.attach()`, you can call `self.show_area()` inside a widget to draw a rectangle around it.

##### Parameters

All parameters are optional.

###### `color`

Pass in the color for the rectangle. It can be a string or a tuple/list. The following strings are currently supported:
* blue
* cyan
* fuchsia
* green
* orange
* pink
* red
* yellow

The default color is green.

You can also pass in just a substring of those, so `color='b'` sets the color to blue.

If those are not enough and you want a more fine-tuned color, passing in a tuple or a list of either RGB or RGBA colors is possible. They work exactly as rgb and rgba attributes in kv language. If an RGBA list/tuple (4 values) is passed in, the `alpha` parameter is ignored.

For example, `color=(1, 1, 0)` sets the color to yellow, using alpha of whatever is set using the `alpha` parameter. On the other hand, `color=(1, 0.7, 0, 1)` sets the color to orangeish with alpha of 1. 

###### `alpha`

Sets the color's alpha channel. It should be a value between 0 and 1. The value is 0.5 by default.

###### `group`

In some (rare) cases you might need to define a group for the canvas (see canvas.after and canvas.before in the Kivy documentation). The supported options are 'before' and 'after'. No group is used by default.

If you have two widgets on the top of each other, but you can see the area of only one of them, try setting `group='after'` for the one not visible or `group='before'` for the one hiding the other. See the Kivy documentation for more information.
