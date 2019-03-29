import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


useragent=UserAgent()
first_url="http://codingbat.com/java"
page=requests.get(first_url,headers={'user-agent':useragent.chrome})
soup=BeautifulSoup(page.content,'lxml')

index_url="http://codingbat.com"

divs=soup.find_all('div',attrs={'class':'summ'})

links=[index_url+  div.a['href'] for div in divs]


#going to different category pages

for link in links:
    categories=requests.get(link,headers={'user-agent':useragent.chrome})
    cat_soup=BeautifulSoup(categories.content,'lxml')
    div=cat_soup.find('div',attrs={'class':'tabc'})
    q_links=[index_url+td.a['href'] for td in div.div.table.find_all('td')]

#getting the problem statements
    for q_link in q_links:
        problems=requests.get(q_link)
        p_soup=BeautifulSoup(problems.content,'lxml')
        inner_divs=p_soup.find('div',attrs={'class':'indent'})
        problem=inner_divs.table.div.string

        examples=inner_divs.table.div.next_siblings

        all_examples=[ex for ex in examples if ex.string is not None]

        print(problem)
        for example in all_examples:
            print(example)

        print("\n\n")