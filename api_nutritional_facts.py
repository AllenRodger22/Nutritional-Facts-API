from flask import Flask

import pandas as pd

data = pd.read_csv('data_nutrition.csv')

app = Flask('_myapp_')

@app.route('/food-info/<foodname>',methods=['GET'])
def get_food_info(foodname):
  q = data.query(f"product_name == '{foodname}'")
  protein = q['proteins_100g'].median()
  fat = q['fat_100g'].median()
  carb = q['carbohydrates_100g'].median()
  response = {'nutritional facts:':{'protein_per_100g:':round(protein,2),'fat_per_100g:':round(fat,2),'carbohydrate_per_100g:':round(carb,2)}}
  
  return response

app.run(host='0.0.0.0')