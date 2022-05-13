from bs4 import BeautifulSoup
import re


def main():
    file_path = 'Intelligence-Bushtarion.html'
    with open(file_path, 'rb') as f:
        buff = f.read()
        the_list = []
        soup = BeautifulSoup(buff, "html.parser")
        results = soup.find(id="main-page-data")
        tabs = results.find_all("tr")
        for t in tabs:
            if len(t.contents) == 5:
                # res = t.find_all("td", class_="lightheader")
                # for r in res:
                if 'Attacking' in t.contents[3].text:
                    tick = re.findall('([0-9]*?) ticks ago', t.contents[1].text.replace("This tick.", "0 ticks ago.").replace("Last tick.", "1 ticks ago."))[0]
                    target_id = re.findall('\[([0-9]*?)\]',t.contents[3].text)[0]
                    #print(f'tick: {tick}; id: {target_id}')
                    the_list.append((tick, target_id))
        print('id, ticks_ago')
        for r in the_list:
            print(f'{r[0]}, {r[1]}')

        simplified_list = []
        for r in the_list:
            if int(r[0]) < 144:
                simplified_list.append(r[1])
        final = ', '.join(set(simplified_list))
        print(final)


if __name__ == "__main__":
    main()
