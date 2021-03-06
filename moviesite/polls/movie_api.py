from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import sys
import re
import json

def get_data(movie):

    try: 
        br = Browser()
        br.open("http://www.imdb.com/find?s=tt&q="+movie)
        link = list(br.links(url_regex = re.compile(r"/title/tt*")))[0]
    
    
    except:
        print "Not Found!"
        exit(3);
   
    res = br.follow_link(link)
    soup = BeautifulSoup(res.read())
    title_year = soup.find('span', id = 'titleYear')
    year_str = str(title_year)
    year = re.search('.*([0-9]{4}).*',year_str).group(1)
    title = soup.find('title').contents[0]
    rate = soup.find('span',itemprop = 'ratingValue')
    rating = str(rate.contents[0])

    actors = []
    actors_soup = soup.findAll('span',itemprop = 'actors')
    for i in actors_soup:
        i_str=str(i)
        j = i_str.rpartition('itemprop="name"')[-1];
        actors.append(re.search('\>(.*?)\<',j).group(1))
    
    directors = []
    director_soup = soup.findAll('span',itemprop = 'director')
    for i in director_soup:
        i_str = str(i)
        j = i_str.rpartition('itemprop="name"')[-1];
        directors.append(re.search('\>(.*?)\<',j).group(1))
    
    votes = soup.find('span',itemprop = 'ratingCount').contents[0]
    response = []
    response.append({ "Movie : ": title})
    response.append({"Rating: ": rating})
    response.append({"Votes ": votes})
    response.append({"Release Year : ": year}) 
    response.append({"Director : ": directors})
    response.append({"Actors : ": actors})
    return json.dumps(response)

'''
if len(sys.argv) != 2:
    print "\nSyntax: python %s 'Movie title'" % (sys.argv[0])
    exit()
else :
        movie = '+'.join(sys.argv[1].split())
'''
movie = "lagaan"
get_data(movie)
