import pandas as pd
import csv

# csv_file = open('test.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Name','Age','Height','Weight'])


# name = ["hello", "bye", "die"]
# age = [ 0, 4, 6]
# height = [500, 60, 20329]
# weight = [232, 345, 232352]

# for i in range (0, 3):
#     csv_writer.writerow([name[i], age[i], height[i], weight[i]])

# csv_file.close()

# result = pd.read_csv('test.csv')

# print(result)


# stringA = 'àa string withé fuünny charactersß.'

# encodestring = stringA.encode('ascii', 'ignore')
# decodedstring = encodestring.decode()
# print(encodestring)
# print(decodedstring)

url1 = 'https://www.sainsburys.co.uk/shop/gb/groceries/fruit-veg/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=12518&parent_category_rn=&top_category=12518&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=12518&categoryFacetId2='
url2 = 'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=13343&parent_category_rn=&top_category=13343&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=13343&categoryFacetId2='
url3 = 'https://www.sainsburys.co.uk/shop/gb/groceries/dairy-eggs-and-chilled/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=428866&parent_category_rn=&top_category=428866&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=428866&categoryFacetId2='
url4 = 'https://www.sainsburys.co.uk/shop/CategorySeeAllView?pageSize=120&orderBy=FAVOURITES_FIRST&storeId=10151&categoryFacetId1=12518&promotionId=&listId=&catalogId=10241&searchTerm=&beginIndex=120&top_category=&langId=44&categoryId=12518&parent_category_rn='
url5 = 'https://www.sainsburys.co.uk/shop/gb/groceries/price-lock-/seeall?fromMegaNav=1#langId=44&storeId=10151&catalogId=10241&categoryId=488855&parent_category_rn=&top_category=488855&pageSize=60&orderBy=FAVOURITES_FIRST&searchTerm=&catSeeAll=true&beginIndex=0&categoryFacetId1=488855&categoryFacetId2='
param1 = url1.split('&')
param2 = url5.split('&')
print(param1)
print(param2)

params = {}
for i in param2:

    hi = i.split('=')
    params[hi[0]] = hi[1]

print(params)