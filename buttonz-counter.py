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


def creating_list_with_websites(websites_file):
    webRegex = re.findall(r'(.+)', websites_file)

    return webRegex


def checking_if_site_have_http(websites):
    websites_to_check = list(websites)
    for i in range(len(websites_to_check)):
        if websites_to_check[i][:4] != 'http':
            websites_to_check[i] = 'http://' + websites_to_check[i]

    return websites_to_check


def downloading_site(website):
    site = requests.get(website)
    site.raise_for_status()

    soup = bs4.BeautifulSoup(site.text, "html.parser")

    return soup


def deleting_what_finded(soup, button):
    for i in range(len(button)):
        soup= soup.replace(button[i], '')

    return soup


def finding_buttons(soup):
    html_buttons = re.findall(r'<button.*?>.*?</button>', soup, re.I)
    soup = deleting_what_finded(soup, html_buttons)
    submit_buttons = re.findall(r'<input.+?type="submit".*?value=".*?>', soup, re.I)
    soup = deleting_what_finded(soup, submit_buttons)
    reset_buttons = re.findall(r'<input.+?type="reset".*?value=".*?>', soup, re.I)
    soup = deleting_what_finded(soup, reset_buttons)
    button_buttons = re.findall(r'<input.+?type="button".*?value=".*?>', soup, re.I)
    soup = deleting_what_finded(soup, button_buttons)
    css_bttns_small = re.findall(r'<.*?class="btn btn-small".*?>', soup, re.I)
    soup = deleting_what_finded(soup, css_bttns_small)
    css_buttons = re.findall(r'<.*?class=".*?button".*?>.+?<', soup, re.I)
    css_buttons2 = re.findall(r'<.*?class=".*?button.*?">\s', soup, re.I)

    buttons = [html_buttons, submit_buttons, reset_buttons, button_buttons, css_bttns_small, css_buttons, css_buttons2]

    return buttons


def calculating_buttons(buttons):
    flat_buttons = list(itertools.chain(*buttons))
    number_of_buttons = len(flat_buttons)

    return number_of_buttons


def sites_buttons_calculate(websites):
    buttons_list = []
    for website in websites:
        soup = str(downloading_site(website))
        buttons = finding_buttons(soup)
        calculated_buttons = calculating_buttons(buttons)
        buttons_list.append(str(calculated_buttons))

    return buttons_list

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