import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
import time
import thread

def get_sheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('twiver-e3110dd3a50f.json', scope)
    gc = gspread.authorize(credentials)
    return gc.open("Twiver").sheet1

def get_html(url):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    browser.quit()
    return html

def tweet_not_found(twitter_page):
    # Twitter displays whether a tweet exists differently depending on which version of their
    # site they serve. Light mode and dark mode have different behavior, so we need to handle both.

    # Dark mode shows a 'Learn more' link that handles all cases
    if 'https://help.twitter.com/rules-and-policies/notices-on-twitter' in twitter_page:
        return True

    # Light mode shows a generic message we can use
    if 'This Tweet is unavailable.' in twitter_page:
        return True

    return False

def get_tweet_status(tweet_url):
    twitter_page = get_html(tweet_url)
    if tweet_not_found(twitter_page):
        return 'Tweet not found'
    return 'Tweet exists'

def update_spreadsheet_row(sheet, tweet, index):
    status = get_tweet_status(tweet)
    sheet.update_cell(2 + index, 2, status)

sheet = get_sheet()

while True:
    tweets = sheet.col_values(1)[1:]
    for index in range(len(tweets)):
        tweet = tweets[index]
        thread.start_new_thread(update_spreadsheet_row, (sheet, tweet, index))
    # Wait five minutes before refreshing the spreadsheet again
    time.sleep(60 * 5)