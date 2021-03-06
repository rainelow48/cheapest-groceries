import pandas as pd
import csv, time, os, requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta


data = pd.read_csv(os.getcwd()+'\\allbakery.csv')
print (data)
filter = data['Price/Unit'].str.contains('p')
print(data[filter].head(20), "\n\n")

def containsp(price):
    if ('p' in price):
        newprice = int(price[:-1])/100
        return newprice
    else:
        return price

ppu = data['Price/Unit'].apply(lambda item: containsp(item))
data['Price/Unit'] = ppu

ppm = data['Price/Measure'].apply(lambda item: containsp(item))
data['Price/Measure'] = ppm


print(data.sort_values(['Price/Unit', 'Price/Measure']).head(50))



# print("using csv now")
# start_time = time.time()
# csv_file = open(os.getcwd()+'\\test files\\test.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Name','Age','Height','Weight'])

# for i in range (0, 100000):
#     csv_writer.writerow([i, str(i)+'p', i, i])
# print("--- %s seconds ---" % (time.time() - start_time))

# today = date.today()
# dtoday = today.strftime("%b %d %Y")
# print(dtoday)
# print(type(dtoday))
# # moddate = time.ctime(os.path.getmtime(os.getcwd()+"\\csv files\\bakery.csv"))
# # testmoddate = time.ctime(os.path.getmtime(os.getcwd()+"\\test files\\test.csv"))
# moddate = date.fromtimestamp(os.path.getmtime("D:\\Coding\\CPP edX\\1.CPP.txt"))
# print(today)
# print(moddate)
# datediff = today - moddate
# print(today < moddate)
# print(datediff)
# print(datediff < timedelta(7))
# print(type(moddate))

# with open('test.csv', 'w+') as f:
#     header = pd.DataFrame({'Name': [],'Age': [],'Height': [],'Weight': []})
#     header.to_csv(f, mode = 'a', header = True)

#     for i in range (0, 100):
#         col = pd.DataFrame([i, i, i, i])
#         row = col.T
#         row.to_csv(f, mode='a')


# name = ["hello", "bye", "die"]
# age = [ 0, 4, 6]
# height = [500, 60, 20329]
# weight = [232, 345, 232352]

# for i in range (0, 3):
#     csv_writer.writerow([name[i], age[i], height[i], weight[i]])

# csv_file.close()

# result = pd.read_csv('test.csv')

# print(result)

# Remove non ascii characters
# stringA = 'àa string withé fuünny charactersß.'

# encodestring = stringA.encode('ascii', 'ignore')
# decodedstring = encodestring.decode()
# print(encodestring)
# print(decodedstring)


# Get url params
# url1 = 'https://www.sainsburys.co.uk/shop/gb/groceries/fruit-veg/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=12518&parent_category_rn=&top_category=12518&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=12518&categoryFacetId2='
# url2 = 'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=13343&parent_category_rn=&top_category=13343&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=13343&categoryFacetId2='
# url3 = 'https://www.sainsburys.co.uk/shop/gb/groceries/dairy-eggs-and-chilled/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=428866&parent_category_rn=&top_category=428866&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=428866&categoryFacetId2='
# url4 = 'https://www.sainsburys.co.uk/shop/CategorySeeAllView?pageSize=120&orderBy=FAVOURITES_FIRST&storeId=10151&categoryFacetId1=12518&promotionId=&listId=&catalogId=10241&searchTerm=&beginIndex=120&top_category=&langId=44&categoryId=12518&parent_category_rn='
# url5 = 'https://www.sainsburys.co.uk/shop/gb/groceries/price-lock-/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=488855&parent_category_rn=&top_category=488855&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=488855&categoryFacetId2='
# param1 = url1.split('&')
# param2 = url5.split('&')
# print(param1)
# print(param2)

# params = {}
# for i in param2:

#     hi = i.split('=')
#     params[hi[0]] = hi[1]

# print(params)



# Waitrose scrape test
# url = 'https://www.waitrose.com/ecom/shop/browse/groceries/food_cupboard'

# csv_file = open(os.getcwd()+'\\test files\\waitrose.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Description'])

# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'lxml')

# counter = 0
# print(len(soup.find_all('article')))
# for i in soup.find_all('article'):
#     name = i.h2
#     print("hi:", name)
#     counter += 1

# print(counter)