import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")
soup=BeautifulSoup(webpage.text, 'html.parser')
chocolate_ratings = soup.find_all(attrs={"class": "Rating"})
ratings = []
for r in chocolate_ratings[1:]:
    ratings.append(float(r.get_text()))
print(ratings)
plt.hist(ratings)
plt.show
plt.clf()
company_tags = soup.select(".Company")
companies_names = []
for company in company_tags[1:]:
    companies_names.append(company.get_text())
d = {"Company": companies_names, "Rating": ratings}
df = pd.DataFrame.from_dict(d)
mean_vals = df.groupby("Company").Rating.mean()
ten_best = mean_vals.nlargest(10)
print(ten_best)

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")
for td in cocoa_percent_tags[1:]:
    percent = float(td.get_text().strip('%'))
    cocoa_percents.append(percent)
d = {"Company": companies_names, "Rating": ratings, "CocoaPercentage": cocoa_percents}
df = pd.DataFrame.from_dict(d)
plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()

