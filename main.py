import pandas as pd
from bs4 import BeautifulSoup
import requests

# URL in a variable "target-page"
target_page = "https://www.pickswise.com/nfl/picks/"

# Div class to search within
div_class_name = 'EditorialArticle_content__ZaKcB'

# From an external TXT file is getting a link of keywords storing them in a pandas dataFrame
with open('keywords.txt', 'r') as f:
    keywords = f.read().splitlines()

keywords_df = pd.DataFrame(keywords, columns=['keyword'])

# From an external CSV file with list of URLs the script is crawling the pages
urls_df = pd.read_csv('pages.csv')
urls_df['keyword_found'] = False
urls_df['keyword_hyperlinked'] = False
urls_df['hyperlink_target_page'] = False
urls_df['found_keyword'] = ''
urls_df['score'] = 0.0

# Crawling the pages from the CSV file and is looking in the text of the pages does some of the keywords is mentioned.
for i, row in urls_df.iterrows():
    url = row['Top pages']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the div with the specified class
    div_content = soup.find('div', {'class': div_class_name})

    if div_content:
        found_keywords = []
        for keyword in keywords:
            if keyword in div_content.text:
                found_keywords.append(keyword)
                urls_df.loc[i, 'keyword_found'] = True

                keyword_occurrences = div_content.text.count(keyword)
                urls_df.loc[i, 'score'] += min(keyword_occurrences * 0.1, 1.0)

                for a in div_content.find_all('a', href=True, string=True):
                    if keyword in a.text:
                        urls_df.loc[i, 'keyword_hyperlinked'] = True
                        if a['href'] == target_page:
                            urls_df.loc[i, 'hyperlink_target_page'] = True
                            break

                meta_title = soup.find('meta', {'property': 'title'}) or soup.find('meta', {'name': 'title'})
                if meta_title and keyword in meta_title.get('content', ''):
                    urls_df.loc[i, 'score'] += 0.5

                h1_title = soup.find('h1')
                if h1_title and keyword in h1_title.text:
                    urls_df.loc[i, 'score'] += 0.3

                h2_titles = soup.find_all('h2')
                for h2_title in h2_titles:
                    if keyword in h2_title.text:
                        urls_df.loc[i, 'score'] += 0.2
                        break

                h3_h4_titles = soup.find_all(['h3', 'h4'])
                for h3_h4_title in h3_h4_titles:
                    if keyword in h3_h4_title.text:
                        urls_df.loc[i, 'score'] += 0.1
                        break

        if found_keywords:
            urls_df.loc[i, 'found_keyword'] = ', '.join(found_keywords)
    else:
        print(f"Couldn't find div with class {div_class_name} in {url}")

    # Limit score to 1.0
    urls_df.loc[i, 'score'] = round(min(urls_df.loc[i, 'score'], 1.0), 2)


# Save results to a new CSV file
urls_df.to_csv('result.csv', index=False)