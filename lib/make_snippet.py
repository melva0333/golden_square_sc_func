def make_snippet(text):
    words = text.split(" ")
    if len(words) > 5:
        return " ".join(words[0:5]) + "..."
    else:
        return text

