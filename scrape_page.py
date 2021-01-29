import requests
import pandas as pd

URL = 'https://www.baseball-almanac.com/hitting/hihr5.shtml'

def get_table(html, table):
	df = pd.read_html(html, attrs={'class': 'boxed'}, header=1)[0]
	return df

def main():
	html = requests.get(URL).text
	df = get_table(html, {'class': 'boxed'})
	df.to_csv('HR Year-by-Year Leaders.csv', index=None)

if __name__ == '__main__':
	main()