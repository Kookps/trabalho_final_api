from bs4 import BeautifulSoup
import requests


def tabela_das_estatistica():
    print("Escolha dentre uma dessas estatisticas disponiveis para saber o top 25 na história da nba: \n" + "PPG - pontos por jogo; \n" + "RPG - rebotes por jogo; \n" + "APG - assistencias por jogo; \n" + "BPG - blocks por jogo; \n" + "SPG - roubos de bola por jogo; \n" + "FG% - porcentagem de acerto dos lançamentos; \n" + "FT% - porcentagem de acerto dos lances livre; \n" + "3FG% - porcentagem de acerto do triplo. \n")

def ppg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+ppg+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ppgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ppg, atleta in zip(ppgs, atletas):
        print(ppg.text + " - " + atleta.text)

def rpg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+rpg+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    rpgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for rpg, atleta in zip(rpgs, atletas):
        print(rpg.text + " - " + atleta.text)

def bpg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+bpg+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    bpgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for bpg, atleta in zip(bpgs, atletas):
        print(bpg.text + " - " + atleta.text)

def apg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+apg+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    apgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for apg, atleta in zip(apgs, atletas):
        print(apg.text + " - " + atleta.text)

def spg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+spg+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    spgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for spg, atleta in zip(spgs, atletas):
        print(spg.text + " - " + atleta.text)

def fg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+fg%25+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    fgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for fg, atleta in zip(fgs, atletas):
        print(fg.text + " - " + atleta.text)

def ft():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+ft%25+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    fts = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ft, atleta in zip(fts, atletas):
        print(ft.text + " - " + atleta.text)

def three_fg():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=all-time+3fg%25+leaders")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    three_fgs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for three_fg, atleta in zip(three_fgs, atletas):
        print(three_fg.text + " - " + atleta.text)

def base():
    tabela_das_estatistica()
    escolha = input("escolha(escreva a sigla da estatistica que quer saber): ").upper() 
    
    stats_list = ["PPG", "RPG", "APG", "BPG", "SPG", "FG%", "FT%", "3FG%"]

    while escolha not in stats_list:
        print("\nNão está dentre as estatisticas que atualmente possa reconhecer ou escreveste errado! ")
        escolha = input("escolha(escreva a sigla da estatistica que quer saber): ").upper() 
    if escolha == "PPG":
        ppg()

    elif escolha == "RPG":
        rpg()

    elif escolha == "BPG":
        bpg()

    elif escolha == "APG":
        apg()

    elif escolha == "SPG":
        spg()

    elif escolha == "FG%":
        fg()

    elif escolha == "FT%":
        ft()

    elif escolha == "3FG%":
        three_fg()

def continua():
    respostas = ["s", "n"]
    continuar = input("\n quer continuar a ver outras estatisticas(s - sim/n - não)? ")
    while continuar not in respostas:
        print("Resposta não reconhecida(s - sim / n - não)")
        continuar = input("\n quer continuar a ver outras estatisticas(s - sim/n - não)? ")
    if continuar == "n":
        return False

def app():
    while True:
        base()
        if continua() == False:
            break

app()
