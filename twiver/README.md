# Twitter Response Verifier (TwiVer)

## Description
Twiver looks up tweets that are replying to other tweets using a browser and verifies that the replies are responding to tweets that still exist. The status of the tweets are automatically logged into a Google spreadsheet and organized for expediency. 

It is helpful for indicating whether a tweet leads to a dead-end during an open-source investigation. 

## Implementation
This uses the Google Sheets API through the `gspread` Python library, `selenium` for viewing the page (it needs a real browser to account for the page loading information that's not in the original page source), and the `thread` library for multithreading (it takes a while to load pages so it's useful to load many at once).

![Spreadsheet](spreadsheet.png?raw=true "Spreadsheet")
