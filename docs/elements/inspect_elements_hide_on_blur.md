# 检查失去焦点就会消失的元素

## 问题

!> 一个浮层在 blur 事件发生时就会消失，甚至销毁 DOM 结点，致使我们无法使用检查工具选中这个浮层。导致我们也没法检查这个浮层的 DOM 树以及上面的样式。

例如 Github 上面的这个输入框，输入内容的时候会显示搜索结果。假如现在需要检查这个浮层的 DOM 树，并查看样式等等。现在打开 [github](https://www.github.com) 首页，看看你是否能够解决这个问题。

## 答案

> - 按下`Command + \` 或者 `Control + \` （ Windows 下 ）使 js 暂停运行
> - 在使用检查工具（`Command + Shift + C` 或者 `Control + Shift + C`）选取搜索结果

![inspect_elements_hide_on_blur](../media/inspect_elements_hide_on_blur.gif)

