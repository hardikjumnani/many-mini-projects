import json
import requests
from pywebio import output as pwo
from pywebio import session as pws

def get_fun_fact(_):
    pwo.clear()
    pwo.put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)
    data = json.loads(response.text)
    useless_fact = data['text']

    pwo.style(pwo.put_text(useless_fact), 'color:blue; font-size: 30px')

    pwo.put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

if __name__ == '__main__':
    pwo.put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    pwo.put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    pws.hold()