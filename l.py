import requests
import pandas as pd
from bs4 import BeautifulSoup
reviewlist=[]
def extractReviews(reviewUrl, pageNumber):
    r = requests.get(reviewUrl)
    soup = BeautifulSoup(r.text, 'html.parser')
    reviews = soup.findAll("div", {"class": "user_reviews_"})
    for i in reviews:
        title=i.findAll('strong')
        for j in title:
            k=i.find('p')
            x=i.find('h3')
            review = {
                'title':x.text.strip(),
                'subject': j.text.strip(),
                'body':k.text.strip(),
            }
            print(review)
            reviewlist.append(review)
def main():
    productUrl = "https://www.careers360.com/colleges/dayananda-sagar-college-of-engineering-bangalore/reviews"
    for i in range(4):
        print(f"Running for page {i}")
        try: 
            reviewUrl = productUrl + "?pageNumber=" + str(i)
            extractReviews(reviewUrl, i)
        except Exception as e:
            print(e)
        
   
    df = pd.DataFrame(reviewlist)
    df.to_excel('C:/Users/shars/Desktop/Python/Web_Scraping/Posts/output1.xlsx', index=False)

main()