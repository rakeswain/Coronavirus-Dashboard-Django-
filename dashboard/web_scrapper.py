from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_data():
    url = "https://www.worldometers.info/coronavirus/"
    data = {}
    status = 0
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find('td', string="India").parent

        country_data = dict()
        count = 0
        cols = ['country', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases',
                'serious_cases', 'cases_per_m', 'deaths_per_ms', 'first_case']
        for col in table.find_all('td'):

            if len(col.text) != 0:
                country_data[cols[count]] = col.text.strip()
            else:
                country_data[cols[count]] = 0
            count = count + 1
            if count > 10:
                break;
        data = country_data.copy()
        data['total_cases']
    except Exception as e:
        print("Error occurred :" + str(e))
        status = 1
    return data, status


def get_state_data():
    url = "https://www.mohfw.gov.in/"
    data = {}
    status = 0
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find('div', attrs={'class': 'data-table'}).find('table')
        rows = table.find_all('tr')
        rows = rows[1:len(rows) - 2]
        state_dict = {}
        state_arr = []
        column = ['state', 'total_cases', 'foreign_cases', 'cured', 'deaths']
        count = 0
        for row in rows:
            cols = row.find_all('td')[1:]
            for col in cols:
                state_dict[column[count]] = col.text
                count += 1
                if count > 4:
                    break;
            count = 0
            state_arr.append(state_dict.copy())
        data = state_arr.copy()
    except Exception as e:
        print("Error occurred :" + str(e))
        status = 1
    return data, status

