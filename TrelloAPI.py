import requests
import json
import msvcrt as m

key = open('api-key','r').read() # Key-file 
token = open('api-token','r').read() #Token-file
board = '' # Board


def getBoards():
    url = 'https://api.trello.com/1/members/me/boards'
    headers = {
   "Accept": "application/json"
   }

    query = {   
    'key': key,
     'token': token
    }

    response = requests.request(
     "GET",
     url,
     headers=headers,
    params=query
    )
    print(response)
    dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(dump)

def getBoard():
    url = 'https://api.trello.com/1/boards/'+board
    headers = {
   "Accept": "application/json"
   }

    query = { 
    'key': key,
     'token': token
    }

    response = requests.request(
     "GET",
     url,
     headers=headers,
    params=query
    )
    #print(response)
    dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    #print(dump)

    return(json.loads(response.text)['id'])

def createCard(listId,name,desc):
    print("\nCreateing Card...")
    url = "https://api.trello.com/1/cards"
    query = {
    'key': key,
    'token': token,
    'idList': listId,
    'name':name,
    'desc':desc
    }
    response = requests.request(
     "POST",
     url,
     params=query
    )
    print(url)
    print(response)
    dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(dump)

def createList(name):
    print("\nCreateing List...")
    url = "https://api.trello.com/1/lists"
    query = {
    'key': key,
    'token': token,
    'idBoard': getBoard(),
    'name':name
    }
    response = requests.request(
     "POST",
     url,
     params=query
    )
    print(url)
    print(response)
    dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(dump)

def getCards(listId):
    #print("\nGetting Cards...")
    url = "https://api.trello.com/1/lists/"+listId+"/cards"    
    query = {
       'key': key,
       'token': token,
    }    
    response = requests.request(
       "GET",
       url,
       params=query
    )
    #print(url)
    #print(response)
    #dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    #print(dump)
    return json.loads(response.text)
        
def getLists():
    print("\nGetting Lists...")
    url = "https://api.trello.com/1/boards/"+board+"/lists"    
    query = {
       'key': key,
       'token': token,
    }    
    response = requests.request(
       "GET",
       url,
       params=query
    )
    print(url)
    print(response)
    return json.loads(response.text)

def deleteCard(id):
    print("\nDeleting card...")
    url = "https://api.trello.com/1/cards/"+id
    query = {
       'key': key,
       'token': token
    } 
    response = requests.request(
       "DELETE",
       url,
       params=query
    )
    print(url)
    print(response)
    print(response.text)

def deleteList(id):
    print("\nDeleting list...")
    url = "https://api.trello.com/1/cards/"+id
    query = {
       'key': key,
       'token': token
    } 
    response = requests.request(
       "DELETE",
       url,
       params=query
    )
    print(url)
    print(response)
    print(response.text)

def editCard(id,name,desc):
    print("\nEditing Card...")
    url = "https://api.trello.com/1/cards/"+id
    query = {
    'key': key,
    'token': token,
    'name':name,
    'desc':desc
    }
    response = requests.request(
     "PUT",
     url,
     params=query
    )
    print(url)
    print(response)
    dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(dump)

def transferCard(card_id,new_listID):
    print("\nTransfering Card...")
    url = "https://api.trello.com/1/cards/"+card_id
    query = {
    'key': key,
    'token': token,
    'idList':new_listID
    }
    response = requests.request(
     "PUT",
     url,
     params=query
    )
    print(url)
    print(response)
    dump = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    print(dump)

def getList(id):
    url = "https://api.trello.com/1/lists/"+id    
    query = {
       'key': key,
       'token': token
    }    
    response = requests.request(
       "GET",
       url,
       params=query
    )
    return json.loads(response.text)

def creatingCard():
    showLists()
    print("\nInput List Number: \n↓↓↓")
    list_num = int(input())
    if(list_num < len(lists)):
        print("\nInput name: \n↓↓↓")
        name = input()
        print("\nInput description: \n↓↓↓")
        desc = input()
        createCard(lists[list_num]['id'],name,desc)
    else:
        print("Input error")

def creatingList():
    print("\nInput name: \n↓↓↓")
    name = input()
    createList(name)

def editingCard():
    showLists()
    print("\nInput Number of List: \n↓↓")
    num = int(input())
    if(num < len(lists)):
        id = lists[num]['id']
        print('='*80)
        print("-- List #",num,"\t Name: "+lists[num]['name'], " --")
        print(' ',"-- Cards --")
        i = 0
        cards = getCards(id)
        for card in cards:
            print('#',i, '#', '\t Name: '+card['name'],'\t\t Desc: '+ card['desc'])
            i+=1
        print('='*80)
        print("\nInput Number of Card: \n↓↓")
        num = int(input())
        print("\nInput new name: \n↓↓↓")
        name = input()
        if(name == ''):
            name = cards[num]['name']
        print("\nInput new description: \n↓↓↓")
        desc = input()
        editCard(cards[num]['id'],name,desc)
    else:
        print("Input error")

def transferingCard():
    showLists()
    print("\nInput Number of List: \n↓↓")
    num = int(input())
    if(num < len(lists)):
        id = lists[num]['id']
        print('='*80)
        print("-- List #",num,"\t Name: "+lists[num]['name'], " --")
        print(' ',"-- Cards --")
        i = 0
        cards = getCards(id)
        for card in cards:
            print('#',i, '#', '\t Name: '+card['name'],'\t\t Desc: '+ card['desc'])
            i+=1
        print('='*80)
        print("\nInput Number of Card: \n↓↓")
        num = int(input())
        print("\nInput new List: \n↓↓↓")

        new_num = int(input())
        if(num < len(cards)):
            transferCard(cards[num]['id'],lists[new_num]['id'])
    else:
        print("Input error")

def deletingCard():
    showLists()
    print("\nInput Number of List: \n↓↓")
    num = int(input())
    if(num < len(lists)):
        id = lists[num]['id']
        print('='*80)
        print("-- List #",num,"\t Name: "+lists[num]['name'], " --")
        print(' ',"-- Cards --")
        i = 0
        cards = getCards(id)
        for card in cards:
            print('#',i, '#', '\t Name: '+card['name'],'\t\t Desc: '+ card['desc'])
            i+=1
        print('='*80)
        print("\nInput Number of Card: \n↓↓")
        num = int(input())
        deleteCard(cards[num]['id'])
    else:
        print("Input error")

def showCards():
    print('='*80)
    j=0
    for list in lists:
        cards = getCards(list['id'])
        print('-'*16,'List #',j,': '+ list['name'],'-'*30)
        print(' ',"-- Cards --")
        i = 0
        for card in cards:
            print('#',i, '#', '\t Name: '+card['name'],'\t\t Desc: '+ card['desc'])#,'\t id:' +item['id'])
            i+=1
        j+=1
        print('='*80)

def showLists():
    print('='*80)
    j=0
    for list in lists:
        print('-- ','List #',j,': '+ list['name'],' --')
        j+=1
    print('='*80)



lists = getLists()
menu=-1
while menu != 0:
    print('-'*80)
    print("Press :\n► 1 - Show cards\n► 2 - Create card\n► 3 - Edit card\n► 4 - Transfer card\n► 5 - Delete card\n►",
          "6 - Show lists\n► 7 - Create list \n► 0 - Exit")
    print('-'*80)
    print("\n↓")
    menu = int(input())
    if(menu == 1):
        showCards()
    if (menu == 2):
        creatingCard()
    if (menu == 3):
        editingCard()
    if (menu == 4):
        transferingCard()
    if (menu == 5):
        deletingCard()
    if(menu == 6):
        showLists()
    if (menu == 7):
        creatingList()
        lists = getLists()
    if(menu != 0):
        print("Press enter...")
        input()