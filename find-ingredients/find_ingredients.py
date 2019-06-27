import pandas as pd 
import numpy as np

df = pd.read_csv('ingredients v1.csv', delimiter=',', encoding='utf-8')

def get_columns():
	df.drop(['id', 'asins', 'brand', 'categories', 'dateAdded', 'dateUpdated', 'ean', 'manufacturer', 'manufacturerNumber', 'name', 'sizes', 'upc', 'weight', 'Unnamed: 15'],axis=1, inplace=True)

	print(df.info())

def iter_ingredients():
	for index, row in df.iterrows():

		ingredients_str = row['features.value']

		for char in '.():\\*':

			ingredients_str = ingredients_str.replace(char, '')

		ingredients_str = ingredients_str.replace(',', ' ')
		ingredients_str = ' '.join(ingredients_str.split())

		print(ingredients_str)

		if index == 8:
			break

if __name__ == '__main__':
	get_columns()
	iter_ingredients()