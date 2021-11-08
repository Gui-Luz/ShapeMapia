import os
from core.printer import *
from core import return_formated_ids, main_routine


if __name__ == '__main__':
    LANG = 'en'
    PATH = str(os.path.abspath(os.getcwd())) + '/shapefiles'

    print_banner()
    print_line7(LANG)
    print_line8(LANG, PATH)
    print_line9(LANG)
    print_line10(LANG)
    ids = input('[+] ')
    ids_formated = return_formated_ids(ids)
    print_line11(LANG, ids_formated)
    main_routine(LANG, ids_formated, PATH)
    print(f"[+] ARIGATÔ.")




