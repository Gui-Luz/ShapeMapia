import requests
import shapefile
import json
from core.printer import *

def return_formated_ids(string_ids):
    integer_ids = []
    ids_formated = [i for i in string_ids.replace(' ', '').split(',') if len(i) > 0]
    for id in ids_formated:
        try:
            integer_id = int(id)
            integer_ids.append(integer_id)
        except ValueError:
            pass
    return integer_ids


def extract_jsondata_from_wikimapia(lang, id):
    print_line1(lang, id)
    try:
        wikimapia_id = id
        r = requests.get(
            f'https://api.wikimapia.org/?key=example&function=place.getbyid&id={wikimapia_id}&format=json&pack=&language={lang}')
        json_data = r.json()
    except Exception as e:
        print_line2(lang, id)
        print(f'[+] {id}: {e}')
        json_data = None

    if 'id' in json_data:
        print_line3(lang, id, json_data)
        return json_data
    else:
        print_line4(lang, id)
        return None


def save_shapefile(lang, id, json_data, path):
    if json_data:
        try:
            x = [x['x'] for x in json_data['polygon']]
            y = [y['y'] for y in json_data['polygon']]
            w = shapefile.Writer(f"{path}/{json_data['title']}/{json_data['title']}")
            w.field('id', 'N')
            w.field('name', 'C')
            w.field('description', 'C')
            w.poly([list(zip(x, y))])
            w.record(f"{json_data['id']}", f"{json_data['title']}", f"{json_data['description']}")
            w.close()
            print_line5(lang, json_data)
        except Exception as e:
            print_line6(lang, id)
            print(f"[+] {id}: {e}")
    else:
        pass


def save_json_data(json_data, path):
    if json_data:
        with open(f"{path}/{json_data['title']}/{json_data['title']}.json", 'w') as f:
            json.dump(json_data, f)
    else:
        pass


def main_routine(lang, ids, path):
    for id in ids:
        json_data = extract_jsondata_from_wikimapia(lang, id)
        save_shapefile(lang, id, json_data, path)
        save_json_data(json_data, path)