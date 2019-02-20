from unicodedata import normalize, combining
from sys import argv
from bs4 import BeautifulSoup as bs
from requests import get, status_codes, codes, utils, exceptions

list_with_initial_args = argv
base_url = 'https://www.vagalume.com.br/'

#A intensão da normalize_arg é fazer a conversão de caracteres com acentuação para sem acentuação. Ex.: 'ã' se torna 'a'
def normalize_arg(arg):
    #faço a conversão dos caracteres especiais e converto para string
    convert_to_normalized = normalize('NFKD', str(arg))
    #cria a string sem a acentuação fazendo a combinação dos carcteres convertidos.
    band_s_name_without_accents = ''.join([char for char in convert_to_normalized if not combining(char)])
    return band_s_name_without_accents

#Para controlar o argumento da banda e o -top5
def check_amount_args(band_s_name):
    if '-top5' in list_with_initial_args:
        #faço uma cópia da lista original porque vou utilizar ela para fazer outros controles
        modified_list_arg = list_with_initial_args[:]
        modified_list_arg.remove('-top5')
        band_s_name = '-'.join(modified_list_arg[1:]).lower()
        return normalize_arg(band_s_name)
    else:
        band_s_name = '-'.join(list_with_initial_args[1:]).lower()
        return normalize_arg(band_s_name)

band_s_name	= check_amount_args(list_with_initial_args)

page_band = base_url + band_s_name

#Checagem para identificar se não foi informado a banda ou o nome está errado e exibir um pequeno help para o uso correto.
def check_args_is_ok(page_band):
    if page_band == base_url:
        print('''
Não foi informado o nome da banda. Siga o exemplo de uso: python crawler.py Zé do Caroço -top5
Você pode usar o comando -top5 para exibir as 5 músicas mais conhecidas da banda.
Por padrão serão exibidas as 25 primeiras músicas em ordem alfabética''')
    if get(page_band).status_code == codes['not_found']:
        print('\nNão foi localizada essa banda. Verifique a ortografia.')
        print('''
Dicas: 
* Bandas que possuem acento nas letras (Ex.: Titãs) você pode escrever com o acento.
* Bandas que tem caracteres especias como apóstrofo ( ' ), crifrão ( $ ), 'e comercial'
  ( & ) e outros, você deve escrever o nome da banda sem o carácter especial.
- Ex1.: para Gun's n Roses utilize Guns n Roses;
- Ex2.: para Eddy B & Tim Gunter utilize Eddy B Tim Gunter
- Ex2.: para Ca$h Out utilize Cah Out''')

#Aqui vou gerar as músicas de acordo com as opções passadas
def mount_list_of_music(page_band):
    check_args_is_ok(page_band)
    try:
        get_page_band = get(page_band)
        #Quando fiz o teste usando o VS Code do Windows, a página veio no encoding ISO-8859-1 então fiz uma conversão explicita
        get_page_band.encoding = 'utf-8'
        html_page = bs(get_page_band.text, 'html.parser')
        all_musics = html_page.find_all('div', {'class': 'lineColLeft'})
        list_with_everything = list()
        for music in all_musics:
            music_name = music.find('a').text
            list_with_everything.append(music_name)
        #Tratamento para organizar melhor a lista com as músicas    
        clean_list_with_musics = list(dict.fromkeys(list_with_everything))
        if len(list_with_initial_args) >= 3:
            if '-top5' in list_with_initial_args:
                for music in clean_list_with_musics[0:5]:
                    print(music)
            else:
                sorted_list = sorted(clean_list_with_musics)
                for music in sorted_list[0:25]:
                    print(music)
        else:
            sorted_list = sorted(clean_list_with_musics)
            for music in sorted_list[0:25]:
                    print(music)
    except exceptions.RequestException:
        print('Não foi possível acessar o site. Verifique a sua internet ou tente mais tarde.')

mount_list_of_music(page_band)