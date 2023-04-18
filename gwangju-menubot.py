import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import date

def updateMenu():
    todayMenu = requests.request('GET','https://front.cjfreshmeal.co.kr/meal/v1/today-all-meal?storeIdx=6442')
    todayMenuLunch = json.loads(todayMenu.text)['data']['2']
    menu = [0] * 5
    for i in range(5):
        menu[i] = {
            'name':todayMenuLunch[i]['name'],
            'side':todayMenuLunch[i]['side'],
            'corner':todayMenuLunch[i]['corner'],
            'kcal':todayMenuLunch[i]['kcal'],
            'thumbnailurl':todayMenuLunch[i]['thumbnailUrl']
        }
    return menu

def getRenderString(menu):
    renderstring = ''
    renderstring += '# ' + date.today().strftime("%Y-%m-%d") + ' 오늘의 점심\n'
    for i in range(5):
        renderstring += '## ' + str(i+1) + '. ' + menu[i]['corner'] + '\n'
        renderstring += '### ' + '**' + menu[i]['name'] + '**\n'
        renderstring += menu[i]['side'] + '\n'
        renderstring += str(int(menu[i]['kcal'])) + 'kcal\n'
        renderstring += '![' + menu[i]['name'] + '](' + menu[i]['thumbnailurl'] + ')\n'
        renderstring += '---\n'
    return renderstring

def post(menu, url_hook):
    response = requests.post(
            url_hook,
            headers={'Content-Type':'application/json'},
            data=json.dumps(
                    {
                        "text":menu,
                        "channel":"test-bot"
                    }
                )
            )

def dailyMenuUpdate():
    url_hook_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'url_hook.txt')
    with open(url_hook_file, 'rt') as f:
        url_hook = f.read().strip()
    renderstring = getRenderString(updateMenu())
    post(renderstring, url_hook)

if __name__ == '__main__':
    dailyMenuUpdate()
