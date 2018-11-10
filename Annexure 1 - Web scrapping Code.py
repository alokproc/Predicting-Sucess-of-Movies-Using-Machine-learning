

# import lxml html parser
import lxml.html 

# import css selector 
from lxml.cssselect import CSSSelector

# for sending http requests
import requests

# create a list of periods beginning 2000

period = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
#period = ['2016']


# declare empty list to which movie name and information web link will be appended. The list of weblinks will be used 
# to collect data for each movie

list_title_name = []
list_title_link = []

for i in period: # 'i' is used access period elements
    r = requests.get('https://bestoftheyear.in/year/'+i+'/')
    # requests html data from the server main page

    tree = lxml.html.fromstring(r.text)
    # creates an element tree from the HTML code requested above

    for j in range(len(tree.cssselect('main div[class="movie-money"]'))): # len function is used to get length of element

        title_name = tree.cssselect('main a[class="movie-name"]')[j]
        # constructing a css selector to extract movie name 

        link = tree.cssselect('main a')[j*2]
        # constructing a css selector to extract link of movie page

        list_title_name.append(title_name.text_content())
        # appending movie name to the list
        
        list_title_link.append(link.attrib['href'])
        # appending movie name to the list

    for k in range(2,11): # loop to parse next pages on the website  
        r = requests.get('https://bestoftheyear.in/year/'+i+'/page/'+str(k)+'/')
        # requests html data from the server page

        if r.status_code == 200: # check if the page exists. r.status_code returns 200 if the page exists
            tree = lxml.html.fromstring(r.text)
            # creates an element tree from the HTML code requested above

            for m in range(len(tree.cssselect('main div[class="movie-money"]'))): # len function is used to get length of element
                title_name = tree.cssselect('main a[class="movie-name"]')[m]
                link = tree.cssselect('main a')[m*2]
                list_title_name.append(title_name.text_content())
                list_title_link.append(link.attrib['href'])
                #list_title_money.append(title_money.text_content())
                #print(list_title_name)
                #print(list_title_money)

list(zip(list_title_name,list_title_link))


movie_name = [] # Name of the movie
list_rating_boty = [] # Movie Rating by BOTY
list_rating_user = [] # Movie Rating by User
list_releasedate = [] # Movie Release Date
list_actors = [] # Movie Actors
list_director = [] # Movie Director(s)
list_budget = [] # Movie Budget
list_box_office_india = [] # India box office revenue
list_box_office_ww = [] # Worldwide box office revenue
list_of_genre = [] # Genre of the movie
list_box_office_india_adjusted = [] # India box office revenue - adjusted
list_box_office_ww_adjusted = [] # Worldwide box office revenue - adjusted
list_first_day_coll = [] # First day collection
list_first_weekend_coll = [] # First weekend collection
list_first_week_coll = [] # First week collection

# Declaring empty list for the data required


for i in list_title_link: # 'i' is used access period elements
    r = requests.get(i) # requests html data from the server main page
    if r.status_code == 200:
        mytree = lxml.html.fromstring(r.text)
        # creates an element tree from the HTML code requested above

        name_of_movie = mytree.cssselect('h1[class="entry-title"]')[0]
        # constructing a css selector to extract movie name
        movie_name.append(name_of_movie.text_content())
        # appending movie name to list

        len_rating = len(mytree.cssselect('span[class="figure-value"]'))
        if len_rating == 2:
            rating_boty = mytree.cssselect('span[class="figure-value"]')[0]
            list_rating_boty.append(rating_boty.text_content())
            rating_user = mytree.cssselect('span[class="figure-value"]')[1]
            list_rating_user.append(rating_user.text_content())
        # constructing a css selector to extract movie rating and appending the same to a list

        releasedate = mytree.cssselect('td[class="value"]')[0]
        list_releasedate.append(releasedate.text_content())
        # constructing a css selector to extract release date and appending the same to a list

        actors = mytree.cssselect('td[class="value"]')[1]
        list_actors.append(actors.text_content())
        # constructing a css selector to extract actors and appending the same to a list

        director = mytree.cssselect('td[class="value"]')[2]
        list_director.append(director.text_content())
        # constructing a css selector to extract director(s) and appending the same to a list

        budget = mytree.cssselect('td[class="value"]')[3]
        list_budget.append(budget.text_content())
        # constructing a css selector to extract budget and appending the same to a list
        
        box_office_india = mytree.cssselect('td[class="value"]')[4]
        list_box_office_india.append(box_office_india.text_content())
        # constructing a css selector to extract india box office revenue and appending the same to a     list

        box_office_ww = mytree.cssselect('td[class="value"]')[5]
        list_box_office_ww.append(box_office_ww.text_content())
        # constructing a css selector to extract worldwide box office revenue and appending the same to a list

        len_genre = len(mytree.cssselect('span[itemprop="genre"] a[rel="tag"]'))
        list_genre = []
        for i in range(len_genre):
            genre = mytree.cssselect('span[itemprop="genre"] a[rel="tag"]')[i]
            list_genre.append(genre.text_content())
        list_of_genre.append(list_genre)
        # constructing a css selector to extract genre and appending the same to a list

        len_adj_rev = len(mytree.cssselect('div[class="prediction-inner"] td'))
        if len_adj_rev == 2:
            box_office_india_adjusted = mytree.cssselect('div[class="prediction-inner"] td')[0]
            list_box_office_india_adjusted.append(box_office_india_adjusted.text_content())
            box_office_ww_adjusted = mytree.cssselect('div[class="prediction-inner"] td')[1]
            list_box_office_ww_adjusted.append(box_office_ww_adjusted.text_content())
        else:
            box_office_india_adjusted = "NA"
            list_box_office_india_adjusted.append(box_office_india_adjusted)
            box_office_ww_adjusted = "NA"
            list_box_office_ww_adjusted.append(box_office_ww_adjusted)
        # constructing a css selector to extract adjusted revenue and appending the same to a list

        if len(mytree.cssselect('table[class="bo-table"] td')) == 0:
            first_day_coll = "NA"
            first_weekend_coll ="NA"
            first_week_coll ="NA"
            list_first_day_coll.append(first_day_coll)
            list_first_weekend_coll.append(first_weekend_coll)
            list_first_week_coll.append(first_week_coll)
            
        else:   
            first_day_coll = mytree.cssselect('table[class="bo-table"] td')[1]
            list_first_day_coll.append(first_day_coll.text_content())
            first_weekend_coll = mytree.cssselect('table[class="bo-table"] td')[3]
            list_first_weekend_coll.append(first_weekend_coll.text_content())
            first_week_coll = mytree.cssselect('table[class="bo-table"] td')[5]
            list_first_week_coll.append(first_week_coll.text_content())
# constructing a css selector to extract 1st day, weekend and week revenue and appending the same to a list


import pandas as pd
df = pd.DataFrame()
df['Movie Name'] = movie_name
#df['BOTY Rating'] = list_rating_boty
#df['User rating'] = list_rating_user
df['Relase Date'] = list_releasedate
df['Actors'] = list_actors
df['Director'] = list_director
df['Budget'] = list_budget
df['India BO Revenue'] = list_box_office_india
df['World BO Revenue'] = list_box_office_ww
df['Genre'] = list_of_genre
df['Adjusted India BO'] = list_box_office_india_adjusted
df['Adjusted World BO'] = list_box_office_ww_adjusted
df['First Day Collection'] = list_first_day_coll
df['First Weekend Collection'] = list_first_weekend_coll
df['First Week Collection'] = list_first_week_coll
df


# saving data to excel

from pandas import ExcelWriter

writer = ExcelWriter('C:/Users/nikhilgore/My Folders/BDAP/Capstone/Movie_List_Final.xlsx')
df.to_excel(writer)
writer.save()


