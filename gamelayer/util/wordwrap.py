def wordwrap(font, text, width):
    lines = []
    x = 0
    w = len(text)

    while x < w:
        while font.size(text[x:w])[0] > width:
            w -= 1

        if w != len(text):
            while text[w] != " ":
                w -= 1

        line = text[x:w].strip()
        if len(line) > 0:
            lines.append(line)

        x = w
        w = len(text)

    return lines
