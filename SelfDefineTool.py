def decorator():
    def inner(info):
        head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>长难句理解</title>
</head>
<body>
<label for="details">请输入详细信息：</label>
<br>
<textarea name="details" id="details" rows="40" cols="80">这是一个可编辑的文本框。</textarea>
"""
        tail = """
</body>
</html>
"""
        head += info
        head += tail
        return head

    return inner


def p():
    def inner(info):
        srt_p = "<p>{}</p>".format(info)
        return srt_p

    return inner


def run():
    web_page = decorator()
    p_label = p()
    all_p = ""
    for uni in open("Contents.txt", mode="r", encoding="utf-8").readlines():
        all_p += p_label(uni)
    content = web_page(all_p)
    with open("沉浸翻译.html", mode="w", encoding="utf-8") as f:
        f.write(content)
