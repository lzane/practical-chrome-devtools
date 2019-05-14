# 1. inspect the element which disappear on blur

## Question

?> Think of a floating layer which will disappear after blur event, or even the DOM node is destroyed. In this case we can not inspect the floating layer and find out its DOM tree or the styles on it.

A good example will be the Github search input, which will show up the search result while you typing. Suppose you want to inspect the DOM tree and CSS style of the search dialog. Open [github](https://www.github.com) and try out if you can solve this problem.

## Answer

> - Press `Command + \` or `Control + \` (for Windows) to pause the js from execution.
> - Use the inspect tool `Command + Shift + C` or `Control + Shift + C` (for Windows) to inspect the freezing search dialog.

![inspect_elements_hide_on_blur](../media/inspect_elements_hide_on_blur.gif)

