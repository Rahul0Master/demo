from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyC0P4wV3KIzYShkTJK004KrLkk8IvlA4L4"
SEARCH_ENGINE_ID = "27bc11568bd38475b"

def get_search_results(country_code, search_query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': search_query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'cr': country_code,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json().get('items', [])
        return [{'rank': index + 1, 'link': item.get('link', ''), 'title': item.get('title', '')} for index, item in enumerate(results)]
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country_code = request.form['country_code']
        search_query = request.form['search_query']

        results = get_search_results(country_code, search_query)

        return render_template('index.html', results=results)

    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)























# from flask import Flask, render_template, request, send_from_directory
# import requests
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import os

# app = Flask(__name__)

# API_KEY = "AIzaSyC0P4wV3KIzYShkTJK004KrLkk8IvlA4L4"
# SEARCH_ENGINE_ID = "27bc11568bd38475b"

# credentials_path = os.path.join(os.path.dirname(__file__), 'inlaid-stratum-416614-04ec49464767.json')
# # Set up the Google Sheets API credentials
# scope = ["https://www.googleapis.com/auth/spreadsheets"]
# SAMPLE_SPREADSHEET_ID = "1WsQVo5tP7Jgzt04smcu-DB5HpPXGM5t17Zi6cB-rjO8"

# credentials = ServiceAccountCredentials.from_json_keyfile_name(
#     credentials_path,  # Use the correct path to the credentials file
#     scope
# )
# gc = gspread.authorize(credentials)

# # Specify the Google Spreadsheet key
# SPREADSHEET_KEY = "04ec49464767200504a96f45292a66c1fbe0a90f"


# def get_search_results(country_code, search_query):
#     url = 'https://www.googleapis.com/customsearch/v1'
#     params = {
#         'q': search_query,
#         'key': API_KEY,
#         'cx': SEARCH_ENGINE_ID,
#         'cr': country_code,
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         results = response.json().get('items', [])
#         return [{'rank': index + 1, 'link': item.get('link', ''), 'title': item.get('title', '')} for index, item in enumerate(results)]
#     else:
#         return None
    

# def save_to_google_sheets(results):
#     # Open the specified Google Spreadsheet
#     worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#     # Clear the existing data (optional, remove if not needed)
#     worksheet.clear()

#     # Add headers
#     headers = ["Rank", "Link", "Title"]
#     worksheet.append_row(headers)

#     # Add search results to the spreadsheet
#     for result in results:
#         row_data = [result['rank'], result['link'], result['title']]
#         worksheet.append_row(row_data)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         country_code = request.form['country_code']
#         search_query = request.form['search_query']

#         results = get_search_results(country_code, search_query)

#         if results:
#             save_to_google_sheets(results)

#         return render_template('index.html', results=results)

#     return render_template('index.html', results=None)

# if __name__ == '__main__':
#     app.run(debug=True)