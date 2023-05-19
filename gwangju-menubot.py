import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import date

def updateMenu():
    todayMenu = requests.request('GET','https://front.cjfreshmeal.co.kr/meal/v1/today-all-meal?storeIdx=6442')
    todayMenuLunch = json.loads(todayMenu.text)['data']['2']
    menu = []
    for i in range(5):
        if i >= len(todayMenuLunch):
            break
        if todayMenuLunch[i]['corner'] == '서비스코너':
            break
        menu.append({
            'name':todayMenuLunch[i]['name'],
            'side':todayMenuLunch[i]['side'],
            'corner':todayMenuLunch[i]['corner'],
            'kcal':todayMenuLunch[i]['kcal'],
            'thumbnailurl':todayMenuLunch[i]['thumbnailUrl']
        })
    return menu

def getRenderString(menu):
    renderstring = ''
    renderstring += '# {} 오늘의 점심\n'.format(date.today().strftime("%Y-%m-%d"))
    for i in range(len(menu)):
        renderstring += '## {}. {}\n'.format(i+1, menu[i]['corner'])
        renderstring += '### {}\n'.format(menu[i]['name'])
        renderstring += '{}\n'.format(menu[i]['side'])
        renderstring += '{} kcal\n'.format(menu[i]['kcal'])
        renderstring += '![{}]({} =600)\n'.format(menu[i]['name'], menu[i]['thumbnailurl'])
        renderstring += '***\n'
    return renderstring

def post(menu, url_hook):
    response = requests.post(
            url_hook,
            headers={'Content-Type':'application/json'},
            data=json.dumps(
                    {
                        "text":menu
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
