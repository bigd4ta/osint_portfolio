# Arabic Learning Tool

## Description
The Arabic Learning Tool reads an Arabic article, calculates the frequencies of words in the article, and displays the frequencies to demonstrate the importance of the word. 

It's useful for learning Arabic vocabulary that is relevant to terrorism and counter-terrorism, Salafi-jihadists, current events, violence, and any other vocabulary that is not typically taught in a classroom environment.

## Usage

- Enable reader view in Chrome by navigating to `chrome://flags/#enable-reader-mode` and marking `Enabled`
- Navigate to whatever Arabic page you'd like to understand better (e.g. one from https://bbc.com/arabic)
- `View > Distill Page`

![Distilled Page](page.png?raw=true "Distilled Page")
- Copy the text into `input/` as `article.txt`
- Run `python arabic_helper.py`
- View the result (the text and the words' associated frequencies will be displayed in separate webpages and opened automatically)

![Frequencies](frequencies.png?raw=true "Frequencies")


## Implementation
Arabic is a right-to-left language with non-standard letters that make it very difficult to display correctly using any library within Python. For example, Arabic letters change their appearances depending on where they're located within a word. To solve this problem, I leveraged the language display infrastructure built into the HTML standard -- `<html dir="rtl" lang="ar">` does all the heavy lifting. From there, I represented the output as a webpage.   
