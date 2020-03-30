from flask import Flask, request, jsonify, render_template, Markup
import datetime
app = Flask('app')

def generate_link_with_text(text, link):
  # Markdown format
  # return '[%s](%s)' % (text, link)
  # HTML format
  return '<a href="%s">%s</a>' % (link, text)

def generate_long_form_date(yyyy_mm_dd):
  if not yyyy_mm_dd:
    return '[INSERT DATE]'
  return datetime.datetime.strptime(yyyy_mm_dd, '%Y-%m-%d').strftime('%B %-d, %Y')

def generate_short_form_date(yyyy_mm_dd):
  if not yyyy_mm_dd:
    return '[INSERT DATE]'
  return datetime.datetime.strptime(yyyy_mm_dd, '%Y-%m-%d').strftime('%d %b').upper()

def generate_citation(source):
    text = source['text']
    article_date = source['article_date']
    citation_format = source['citation_format']
    date_in_long_form = generate_long_form_date(article_date)
    date_in_short_form = generate_short_form_date(article_date)
    dngts_text = 'DNGTS' if source['DNGTS_option'] == 'y' else ''
    link = generate_link_with_text(source['name'], source['link'])

    citation = ''
    if citation_format == 'KT':
        print('insert KT text here')
        citation = '%s (%s) UID: %s' % (text, link, source['uid'])
    elif citation_format == 'GoASR':
        print('insert GoASR text here')
        citation = '"%s" %s, %s %s' % (source['name'], date_in_long_form, dngts_text, source['link'])
    elif citation_format == 'SIGACT':
        print('insert SIGACT text here')
        citation = '%s: %s (%s) UID: %s' % (date_in_short_form, text, link, source['uid'])
    else:
        print('Unrecognized citation format')
    return citation

def prompt_for_source():
  # Type source name
  # Type source link
  # Select type of document: KT / GoASR / SIGACT
  # KT: text, uid
  # GoASR: date, dngts
  # SIGACT: date, text, uid
  name = input('Source (e.g. Bloomberg): ')
  link = input('Link (e.g. https://...): ')

  incorrect_citation_format = True
  while incorrect_citation_format:
    citation_format = input('Citation format (1:KT 2:GoASR 3:SIGACT): ')
    if citation_format == '1':
      citation_format = 'KT'
      incorrect_citation_format = False
    elif citation_format == '2':
      citation_format = 'GoASR'
      incorrect_citation_format = False
    elif citation_format == '3':
      citation_format = 'SIGACT'
      incorrect_citation_format = False
    else:
      print('Invalid citation format!')

  text = input('Text:')
  if text == '':
    text = '[INSERT TEXT HERE]'

  uid = input('UID: ')
  if uid == '':
    uid = '[INSERT UID HERE]'

  source = {
    'text': text,
    'name': name,
    'link': link,
    'uid': uid,
    'DNGTS_option': input('DNGTS? (y/n): ') == 'y',
    'article_date': input('Date (YYYY-MM-DD): '),
    'citation_format': citation_format
  }
  return source


@app.route('/', defaults={'text': '', 'name': '', 'link': '', 'uid': '', 'dngts_option': '', 'article_date': '', 'citation_format': ''})
def main(text, name, link, uid, dngts_option, article_date, citation_format):
  text = request.args.get('text')
  name = request.args.get('name')
  link = request.args.get('link')
  uid = request.args.get('uid')
  dngts_option = request.args.get('dngts_option')
  article_date = request.args.get('article_date')
  citation_format = request.args.get('citation_format')

  source = {
    'text': text,
    'name': name,
    'link': link,
    'uid': uid,
    'DNGTS_option': dngts_option,
    'article_date': article_date,
    'citation_format': citation_format
  }

  citation = generate_citation(source)
  print(citation)

  return render_template('index.html', text=text, name=name,
    link=link, uid=uid, dngts_option=dngts_option, article_date=article_date, citation_format=citation_format, citation=Markup(citation))

app.run(host='0.0.0.0', port=8080)