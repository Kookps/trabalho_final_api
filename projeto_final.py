from bs4 import BeautifulSoup
import requests
import csv


def tabela_das_estatisticas_acumulativas():
    print("\nEstatisticas acumulativas: \n" + "Lideres de pontos(LDP); \n" + "Lideres de rebotes(LDR); \n" + "Lideres de assistencias(LDA); \n" + "Lideres de blocks(LDB); \n" + "Lideres de roubos de bola(LDRB); \n" + "Lideres de cestos feitos(LDCF); \n" + "lideres de lances livres feitos(LDLLF); \n" + "lideres de triplos feitos(LDTF). \n")

def ldp():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+points+made+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldps = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    file = open("scraped_quotes.csv", "w")
    writer = csv.writer(file)

    writer.writerow(["Pontos totais", "Atletas"])

    for ldp, atleta in zip(ldps, atletas):
        print(ldp.text + " - " + atleta.text)
        writer.writerow([ldp.text, atleta.text])
    file.close()

def ldr():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+rebounds+of+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldrs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})
    
    for ldr, atleta in zip(ldrs, atletas):
        print(ldr.text + " - " + atleta.text)

def lda():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+assists+of+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldas = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for lda, atleta in zip(ldas, atletas):
        print(lda.text + " - " + atleta.text)

def ldb():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+blocks+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldbs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ldb, atleta in zip(ldbs, atletas):
        print(ldb.text + " - " + atleta.text)

def ldrb():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+steals+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldrbs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ldrb, atleta in zip(ldrbs, atletas):
        print(ldrb.text + " - " + atleta.text)

def ldcf():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+field+goals+made+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldcfs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ldcf, atleta in zip(ldcfs, atletas):
        print(ldcf.text + " - " + atleta.text)

def ldllf():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+free+throws+made+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldllfs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ldllf, atleta in zip(ldllfs, atletas):
        print(ldllf.text + " - " + atleta.text)

def ldtf():
    page_to_scrape = requests.get("https://www.statmuse.com/nba/ask?q=most+three+pointers+made+all-time")
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    ldtfs = soup.find_all("text", limit=25, attrs={"class":"fill-black"})
    atletas = soup.find_all("td", limit=25, attrs={"class":"text-left px-2 py-1 sticky left-0 bg-white"})

    for ldtf, atleta in zip(ldtfs, atletas):
        print(ldtf.text + " - " + atleta.text)



"---------------------------------"



def tabela_das_estatisticas_por_jogo():
    print("\nEstatisticas por jogo: \n" + "Pontos por jogo(PPG); \n" + "Rebotes por jogo(RPG); \n" + "Assistencias por jogo(APG); \n" + "Blocks por jogo(BPG); \n" + "Roubos de bola por jogo(SPG); \n" + "Porcentagem de acerto dos lançamentos(FG%); \n" + "Porcentagem de acerto dos lances livre(FT%); \n" + "Porcentagem de acerto do triplo(3FG%). \n")

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
    tipo_de_estatistica = ["EA", "EPJ"]
    print("\nEstatistica acumulativa(EA);")
    print("Estatistica por jogo(EPJ).\n")
    escolha_do_tipo_de_estatistica = input("Escolha a estatistica que queira saber sobre(escreva a sigla): ").upper()
    while escolha_do_tipo_de_estatistica not in tipo_de_estatistica:
        print("Escreveste errado(EPJ - Estatistica por jogo / EA - Estatistica acumulativa)!")
        escolha_do_tipo_de_estatistica = input("Escolha a estatistica que queira saber sobre(escreva a sigla): ").upper()
    if escolha_do_tipo_de_estatistica == "EPJ":
        tabela_das_estatisticas_por_jogo()
        escolha = input("escolha(escreva a sigla da estatistica que quer saber): ").upper() 
    
        per_game_stats_list = ["PPG", "RPG", "APG", "BPG", "SPG", "FG%", "FT%", "3FG%"]

        while escolha not in per_game_stats_list:
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

        elif escolha == "3FG%":
            three_fg()
    
    elif escolha_do_tipo_de_estatistica == "EA":
        tabela_das_estatisticas_acumulativas()
        escolha = input("escolha(escreva a sigla da estatistica que quer saber): ").upper() 
        longevity_stats = ["LDP", "LDR", "LDA", "LDB", "LDRB", "LDCF", "LDLLF", "LDTF"]

        while escolha not in longevity_stats:
            print("\nNão está dentre as estatisticas que atualmente possa reconhecer ou escreveste errado! ")
            escolha = input("escolha(escreva a sigla da estatistica que quer saber): ").upper() 
        
        if escolha == "LDP":
            ldp()

        elif escolha == "LDR":
            ldr()

        elif escolha == "LDA":
            lda()

        elif escolha == "LDB":
            ldb()

        elif escolha == "LDRB":
            ldrb()

        elif escolha == "LDCF":
            ldcf()

        elif escolha == "LDLLF":
            ldllf()

        elif escolha == "LDTF":
            ldtf()

def continua():
    respostas = ["s", "n"]
    continuar = input("\nquer continuar a ver outras estatisticas(s - sim/n - não)? ").lower()
    while continuar not in respostas:
        print("Resposta não reconhecida(s - sim / n - não)")
        continuar = input("\nquer continuar a ver outras estatisticas(s - sim/n - não)? ").lower()
    if continuar == "n":
        return False

def app():
    while True:
        base()
        if continua() == False:
            break

app()
