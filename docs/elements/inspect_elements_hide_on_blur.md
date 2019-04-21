# 检查失去焦点就会消失的元素

## 问题

在日常前端开发的时候经常会遇到这种情况，一个浮层在 blur 事件发生时就会消失，甚至销毁DOM结点，致使我们无法使用检查工具选中这个浮层。导致我们也没法检查这个浮层的DOM树以及上面的属性。

例如Github上面的这个输入框，输入内容的时候会显示搜索结果。假如现在需要检查这个浮层的DOM树，并查看样式等等。现在打开github首页，看看你是否能够解决这个问题。

## 答案

> - 按下`Command + \` 或者 `Control + \` （ Windows 下 ）使js暂停运行
> - 在使用检查工具（`Command + Shift + C` 或者 `Control + Shift + C`）选取搜索结果

![inspect_elements_hide_on_blur](../media/inspect_elements_hide_on_blur.gif)

