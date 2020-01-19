#first scrape all keywords for smileys from
from bs4 import BeautifulSoup
import requests
import fileinput

page = requests.get("https://www.emojimeanings.net/list-smileys-people-whatsapp")
soup = BeautifulSoup(page.content, 'html.parser')
#soup.select("body > main > div > div > div > table")
#table tableWaHeight tableWa table-responsive table-striped table-hover
x = soup.find("table", {"class" : "table tableWaHeight tableWa table-responsive table-striped table-hover"})
rows = x.find_all("tr")
emojis = {}
for i in range(1, len(rows)):
    cells = rows[i].find_all("td")
    emoji_name, emoji_symbol = cells[1].b.contents[0].lower(), cells[1].contents[0].strip()
    #print(emoji_symbol, emoji_name)
    #, emoji_unicode = , cells[2].contents[0].lower()
    emojis[emoji_symbol] = emoji_name
    #print(emojis)

print(emojis.keys())

#replace all smileys from ../data/sem_eval_data.txt
newfile = open("../data/sem_eval_data_smileys_replaced", "w")
with open("../data/sem_eval_data.txt") as f:
    for line in f.readlines():
        emoji_list={}
        line_list = list(line)
        # print(line_list)
        idx=0
        delete_idx = []
        for char in line_list:
            # print(char)
            if char in emojis:
                #del line_list[idx]
                delete_idx.append(idx)
                if char in emoji_list:
                    emoji_list[char]+=1
                else:
                    emoji_list[char]=1
                # if emojis[char] in emoji_list:
                    
                # else:
                    # line_list.insert(idx, '<'emojis[char]+'> ')

            idx += 1
        j=0
        line_list1=[]
        for i in range(len(line_list)):
            if(j<len(delete_idx) and i==delete_idx[j] ):
                j+=1
            else:
                line_list1.append(line_list[i])
        line_list = line_list1
        newline = str("".join(line_list))
        list_emoji=[]
        for key,value in emoji_list.items():
            for i in range(value):
                list_emoji.append('<'+emojis[key]+'> ')
        newline = newline[:-5] +" "+ str("".join(list_emoji)) + newline[-5:]
        newfile.write(newline)
        
        #line.decode("utf-8").replace(u"\u2022", "*").encode("utf-8")
newfile.close()