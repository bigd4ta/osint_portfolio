# coding=utf-8
import tempfile
import webbrowser

def display_article(article_text):
    html = '<html dir="rtl" lang="ar"><meta charset="utf-8"><p>%s</p></html>' % article_text

    tmp = tempfile.NamedTemporaryFile(delete=False)
    path = tmp.name + '.html'

    with open(path, 'w') as f:
        f.write(html)
        url = 'file://' + f.name

    webbrowser.open(url)

def display_frequencies(frequency_list):
    list_of_strings = [', '.join([str(x) for x in frequency_pair]) for frequency_pair in frequency_list]
    stringified_list = '\n'.join(["<p>%s</p>" % pair for pair in list_of_strings])
    display_article(stringified_list)

def sort_function(list_element):
  return -1 * list_element[1]

def count_frequencies(article_text):
    words = article_text.split()
    word_frequencies = []
    for word in set(words):
      word_frequencies.append([word, words.count(word)])
    word_frequencies.sort(key=sort_function)
    return word_frequencies

def save(write_path, frequency_list):
    pass # TODO
    # This function should save information to a file for later use

def load(read_path):
    pass # TODO
    # This function should return information loaded from a file we had previously written to using `save`

def process_article(url, output_path):
    pass # TODO
    # This function should get the article from the internet, extract its text, then save and return the output

def pick_article():
    pass # TODO
    # Picks the best article from a folder based on whatever you want to optimize (e.g. most unknown words)


article_path = 'input/article.txt'
article_text = open(article_path, 'r+').read()
display_article(article_text)
frequency_list = count_frequencies(article_text)
display_frequencies(frequency_list)
