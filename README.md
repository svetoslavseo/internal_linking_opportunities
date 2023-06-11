Web Page Keyword Analyzer
The Web Page Keyword Analyzer is a Python script that crawls web pages, searches for specific keywords, and calculates a score based on the presence and location of those keywords. The script is designed to help analyze the relevance and keyword usage of web pages.

Prerequisites
Python 3.x
Libraries: pandas, BeautifulSoup, requests
Installation
Clone the repository or download the script file.
Install the required libraries by running the following command:
Copy code
pip install pandas beautifulsoup4 requests
Usage
Prepare a list of web page URLs in a CSV file. The URLs should be listed under the column named "Top pages".
Create a text file containing the keywords you want to search for. Each keyword should be listed on a separate line.
Update the script with the appropriate file paths for the URLs CSV file and the keywords text file.
Run the script using the following command:
Copy code
python web_page_keyword_analyzer.py
The script will crawl each web page, search for the keywords, and calculate a score for each page based on keyword occurrences and location.
The results will be saved in a new CSV file named "result.csv". The file will contain information about keyword matches, hyperlinks, and scores for each web page.
Customization
The script uses the "EditorialArticle_content__ZaKcB" class to search for content within the web page. You can modify the value of the div_class_name variable in the script to match the appropriate class for your target web pages.
The script assigns weights to different elements (meta title, h1, h2, h3, h4) based on keyword occurrence in those elements. You can adjust the weights by modifying the corresponding score values in the script.
Feel free to customize the script further based on your specific requirements and the structure of the target web pages.
Notes
If the script fails to find the specified div class within a web page, it will print a warning message indicating the URL where the issue occurred.
The score assigned to each web page is limited to a maximum of 1.0.
License
This project is licensed under the MIT License.

Feel free to contribute to the project by submitting issues or pull requests.

Please note that the script's performance may vary depending on the number and complexity of the web pages being analyzed. It is recommended to test the script on a small set of pages before processing a larger dataset.
