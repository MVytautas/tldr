"""
I love CLI!
"""

import tldr.scraper.amazon_review_retrieval as amazon
import Summarizer as s

def cli_interface():
    print("""
    ____               _                       __  ___              __  
   / __ \ ___  _   __ (_)___  _      __ _____ /  |/  /____ _ _____ / /__
  / /_/ // _ \| | / // // _ \| | /| / // ___// /|_/ // __ `// ___// //_/
 / _, _//  __/| |/ // //  __/| |/ |/ /(__  )/ /  / // /_/ // /   / ,<   
/_/ |_| \___/ |___//_/ \___/ |__/|__//____//_/  /_/ \__,_//_/   /_/|_|  
                                                                        
<!--       _
       .__(.)< (Please, paste the URL to the reviews!)
        \___)   
 ~~~~~~~~~~~~~~~~~~-->""")
    url = input(">>> ")
    url = url.strip()
    reviews = amazon.get_all_reviews_in_all_pages(url, limit=25)
    # print("*{}*\n {}\n".format(review['Score'], review['Text']))
    prod_positives = [review['Text'] for review in reviews if review['Score'] == 5]
    prod_negatives = [review['Text'] for review in reviews if review['Score'] <= 2]

    s.get_summary(prod_positives, prod_negatives)


if __name__ == "__main__":
    cli_interface()