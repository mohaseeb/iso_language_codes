import requests
from bs4 import BeautifulSoup

iso_lang_codes_wiki = 'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes'
iso_lang_codes_out_csv = 'iso_639-1_language_codes.csv'


def run():
    raw_header, raw_body = scrape_codes_table()
    header, body = clean_codes_table(raw_header, raw_body)
    print_codes_table(header, body)
    write_codes_table_to_csv(header, body)


def scrape_codes_table():
    content = requests.get(iso_lang_codes_wiki).content
    soup = BeautifulSoup(content, 'html.parser')
    row_selector = 'table[id=Table] tr'
    header = [h_cell.text for h_cell in soup.select(row_selector + ' th')]
    body = [
        [b_cell.text for b_cell in row.select('td')]
        for row in soup.select(row_selector)
        if len(row.select('td')) > 0
    ]
    return header, body


def clean_codes_table(header, body):
    def clean_lang_row(row):
        row_ = row[1:]  # we don't care about the lang family color code
        return [cell.strip() for cell in row_]

    return clean_lang_row(header), [clean_lang_row(r) for r in body]


def print_codes_table(header, body):
    def escape_quotes(txt):
        return txt.replace('"', '\\"')

    def row_to_str(row):
        quoted_cells = ['"' + escape_quotes(cell) + '"' for cell in row]
        return f'[{", ".join(quoted_cells)}]'

    print(f'header = {row_to_str(header)}')

    rows_str = ",\n\t".join([row_to_str(r) for r in body])
    print(f'body = [\n\t{rows_str}\n]')


def write_codes_table_to_csv(header, body):
    def row_to_csv_line(row):
        return '|'.join(row) + '\n'

    all_rows = [header]
    all_rows.extend(body)
    all_lines = [row_to_csv_line(row) for row in all_rows]
    with open(iso_lang_codes_out_csv, 'w') as f:
        f.writelines(all_lines)


if __name__ == '__main__':
    run()
