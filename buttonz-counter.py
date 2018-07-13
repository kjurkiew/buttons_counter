import re
import requests
import bs4
import itertools
from sys import argv


def opening_file(file_name):
    file_with_websites = open(file_name)
    try:
        websites = file_with_websites.read()
    finally:
        file_with_websites.close()

    return websites


def creating_list_with_websites(websites):
    list_with_websites = list(re.findall(r'(.+)', websites))

    return list_with_websites


def checking_if_site_have_http(list_with_websites):
    for i in range(len(list_with_websites)):
        if list_with_websites[i][:4] != 'http':
            list_with_websites[i] = 'http://' + list_with_websites[i]

    return list_with_websites


def sites_buttons_calculate(websites):
    buttons_list = []
    for website in websites:
        soup = str(downloading_site(website))
        buttons = finding_buttons(soup)
        calculated_buttons = calculating_buttons(buttons)
        buttons_list.append(str(calculated_buttons))

    return buttons_list


def downloading_site(website):
    site = requests.get(website)
    site.raise_for_status()

    soup = bs4.BeautifulSoup(site.text, "html.parser")

    return soup


def finding_buttons(result):
    soup = bs(result, 'lxml')
    html_buttons = soup.find_all("button")
    result = deleting_what_finded(result, html_buttons)
    submit_buttons = soup.find_all('input', {'type': 'submit'})
    result = deleting_what_finded(result, submit_buttons)
    reset_buttons = soup.find_all('input', {'type': 'reset'})
    result = deleting_what_finded(result, reset_buttons)
    button_buttons = soup.find_all('input', {'type': 'button'})
    result = deleting_what_finded(result, button_buttons)
    css_bttns_small = soup.find_all(class_=re.compile("btn"))
    result = deleting_what_finded(result, css_bttns_small)
    css_buttons = soup.find_all(class_=re.compile("button"))

    buttons = [html_buttons, submit_buttons, reset_buttons, button_buttons, css_bttns_small, css_buttons]

    return buttons

def calculating_buttons(buttons):
    flat_buttons = list(itertools.chain(*buttons))
    number_of_buttons = len(flat_buttons)

    return number_of_buttons

def deleting_what_finded(soup, button):
    for i in range(len(button)):
        soup= soup.replace(button[i], '')

    return soup


def bubble_sort(list, websites):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1 - i):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list [j]
                websites[j], websites[j+1] = websites[j+1], websites[j]
    return list, websites


def saving_to_csv(buttons_list, websites_before_check, output_file):
    file = open(output_file, 'w')
    file.write('address, number_of_buttons\n')
    sorting = bubble_sort(buttons_list, websites_before_check)
    buttons_list = sorting[0]
    websites_before_check = sorting[1]
    for i in range(len(buttons_list)):
        file.write(websites_before_check[i] + ', ' + buttons_list[i] + '\n')
    file.close()


if __name__ == '__main__':
    arguments = argv
    file_name = arguments[1]
    output_file = arguments[2]
    websites_file = opening_file(file_name)
    websites = creating_list_with_websites(websites_file)
    websites_checked = checking_if_site_have_http(websites)
    buttons_list = sites_buttons_calculate(websites_checked)
    saving_to_csv(buttons_list, websites, output_file)
