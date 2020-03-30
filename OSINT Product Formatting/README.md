# OSINT Product Formatting

## Description
The OSINT Product Formatting tool displays an interface 

Quickly and easy formatting open source intelligence products so that more time may be devoted to analysis. 


## Usage
- Run `python web_server.py`
- Open `localhost:8080` in your web browser
- Fill in the form
![Form](form.png?raw=true "Form")
- Copy the resulting citation
![Result](result.png?raw=true "Result")


## Implementation 
For this project, I used a flask webserver for the backend and a basic HTML form for the frontend. I also used the `prompt_for_source` function to debug without having to click around the frontend. It was particularly useful when hooking up the frontend to the backend. 
