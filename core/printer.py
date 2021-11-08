def print_banner():
    print(
    """
                   _____ _    _ _____                       _
                  / ____| |  | |  __ \                     (_)
                 | (___ | |__| | |__) | __ ___   __ _ _ __  _  __ _
                  \___ \|  __  |  ___/ '_ ` _ \ / _` | '_ \| |/ _` |
                  ____) | |  | | |   | | | | | | (_| | |_) | | (_| |
                 |_____/|_|  |_|_|   |_| |_| |_|\__,_| .__/|_|\__,_|
                                                     | |
                                                     |_| v.1.0


                      ▄æ▓██▓██████▄∞    __,           ▄_
                _▀▄╤╫╪██▀ ╙▀███████      "      ▄¬   ╓▄▄██_   <──
        ╓▄▄▄▄,▄▄████╫█╠███  ┼█████       ╓▓█▄  ▄▄▄█████████████████▄▄▄▄▄
       ▐█████████████▀▀ ▓█╨  ██`  ▀Γ   ▄███████████████████████████████▀"`
       ▄▀"  ▀████████▄ ╟██▌         _▓ ╙█▌███████████████████████─  █▌
             ╙████████████▀█         ╚████████████████████████████"
             ▐██████████▀`          ▓█▀╙▀╫██▓▓██╜███████████████▀ ╫
              ████████▀             ▄████▄▄▄▄██████████████████ kΓ"
               ▀██▌  J             ████████████████▀██████████▀
                 ╙▀▀█ `"           █████████████▀╙   ╟█"  ███  ▌
                     "▓███▄_       ╙█▀▀█████████▌     ╙   ,█` ▄'Γ
                     ▐███████▄▄         ▀██████            ▀╦▀▀█  ≡▄▄,
                      █████████          █████▌ ▄               ,▄╕▐
                        ██████           ████▌ █M            ,▄██████
                        ████Ñ            ╙██▀                ▐███████▌
                       ▐██▀                                       ╙▀▀    Φ
                        █▌                                             ª└
                        ▀w'

    """)

def print_line1(lang, id):
    if lang == 'pt':
        print(f'[+] {id}: Buscando informações do id.')
    if lang == 'en':
        print(f'[+] {id}: Searching id information.')


def print_line2(lang, id):
    if lang == 'pt':
        print(f'[+] {id}: Não foi possível encontrar informação do id.')
    if lang == 'en':
        print(f'[+] {id}: Could not find id info.')


def print_line3(lang, id, json_data):
    if lang == 'pt':
        print(f"[+] {id}: Encontrado - {json_data['title']}.")
    if lang == 'en':
        print(f"[+] {id}: Found - {json_data['title']}.")


def print_line4(lang, id):
    if lang == 'pt':
        print(f"[+] {id}: Shapefile não existe.")
    if lang == 'en':
        print(f"[+] {id}: Shapefile does not exists.")


def print_line5(lang, json_data):
    if lang == 'pt':
        print(f"[+] {json_data['id']}: Shapefile de {json_data['title']} salvo.")
    if lang == 'en':
        print(f"[+] {json_data['id']}: Shapefile for {json_data['title']} was saved.")


def print_line6(lang, id):
    if lang == 'pt':
        print(f"[+] {id}: Não foi possível salvar shapefile.")
    if lang == 'en':
        print(f"[+] {id}: Could not found shapefile.")


def print_line7(lang):
    if lang == 'pt':
        print('\n[+] Bem vindo ao SHPmapia!')
    if lang == 'en':
        print('\n[+] Welcome to SHPmapia!')


def print_line8(lang, PATH):
    if lang == 'pt':
        print(f"[+] Os shapefiles serão salvos no diretório {PATH}.")
    if lang == 'en':
        print(f"[+] Shapefiles will be saved in dir {PATH}.")


def print_line9(lang):
    if lang == 'pt':
        print('[+] Para encontrar os ids busque em https://wikimapia.org.')
    if lang == 'en':
        print('[+] Search for ids at https://wikimapia.org.')


def print_line10(lang):
    if lang == 'pt':
        print(
            '[+] Digite os ids do wikimapia que você deseja converter para shapefile separados por vírgula e pressione '
            'enter.')
    if lang == 'en':
        print(
            '[+] Insert wikimapia ids separated by commas and hit enter.')


def print_line11(lang, ids_formated):
    if lang == 'pt':
        print(f"[+] Ids selecionados: {ids_formated}")
    if lang == 'en':
        print(f"[+] Selected ids: {ids_formated}")

