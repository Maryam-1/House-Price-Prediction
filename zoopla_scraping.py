"""
The below python script was used to automatically scrape property listing data from a real estate website, presumably Zoopla, based on the URLs and references in the code. It employs several libraries to execute HTTP requests, process HTML content, and handle data:

- `requests`: For performing HTTP requests to the Zoopla API and property detail pages.
- `BeautifulSoup`: For parsing and extracting data from HTML content retrieved from property detail pages.
- `pandas`: For organizing scraped data into structured DataFrames, performing data cleaning, and saving the data into an Excel file.
- `numpy`: For numerical operations that may be required during data transformation (though not explicitly used in the provided snippet).
- `urllib3`: For disabling warnings related to unverified HTTPS requests, which is generally used to avoid security warnings during development.

The script is structured to execute the following tasks:

1. **Data Retrieval**: Utilizes predefined cookies and headers to simulate browser requests and avoid bot detection, fetching property listing data from the Zoopla API.

2. **Data Extraction**: Applies the `BeautifulSoup` library to parse detailed HTML content from property listing pages, extracting relevant information like postcodes, geographic coordinates, and property features.

3. **Data Transformation**: Implements functions to normalize and prepare the scraped data for analysis, including categorizing property types and converting strings to numeric values where appropriate.

4. **Data Storage**: Aggregates the cleaned data into a single DataFrame and saves the data into an Excel file for further analysis or reporting.

5. **Error Handling**: Includes error handling mechanisms to manage common issues such as timeouts and connection errors, ensuring the scraper's robustness.

6. **Function Definitions**: Contains several function definitions, each responsible for a specific part of the scraping process, such as sending requests, parsing responses, and cleaning the data.

7. **Script Execution**: The `main()` function orchestrates the scraping process across different property types and manages pagination to navigate through multiple listing pages.

This script exemplifies the use of online scraping to acquire real estate data, providing an efficient means of automatically collecting massive volumes of data from the web.
"""

#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sys
import time
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from datetime import datetime
import json
import urllib3
urllib3.disable_warnings()

# Function to send a POST request and get the response with the JSON data
def get_response(json_data):
    # Cookies required for the POST request
    cookies = {
        'zooplapsid': 'a6b5134902dfd23940704ce0dc35f6ca',
        '_ga': 'GA1.3.1483749591.1652981863',
        'ajs_anonymous_id': '90988938-5dc1-432c-9633-8f1e03b3f590',
        'zooplasid': '4a58d17ef0a87c95418947cd35370bb5',
        '_gid': 'GA1.3.731505751.1654036191',
        'cookie_consents': '{"schemaVersion":4,"content":{"brand":1,"consents":[{"apiVersion":1,"stored":false,"date":"Tue, 31 May 2022 22:30:07 GMT","categories":[{"id":1,"consentGiven":true},{"id":3,"consentGiven":false},{"id":4,"consentGiven":false}]}]}}',
    }
    # Headers required for the POST request
    headers = {
        'authority': 'api-graphql-lambda.prod.zoopla.co.uk',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8,de;q=0.7',
        'origin': 'https://www.zoopla.co.uk',
        'referer': 'https://www.zoopla.co.uk/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'x-api-key': '3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu',
    }
    # Send a POST request to the specified URL with the provided cookies, headers, and JSON data
    response = requests.post('https://api-graphql-lambda.prod.zoopla.co.uk/graphql', cookies=cookies, headers=headers, json=json_data)
    return response.json() # Return the JSON response

# Function to get listings from a specific page number and property type
def get_page_listings(page_num, property_type):
    # JSON data structure for the POST request
    json_data = {
        'operationName': 'getListingData',
        'variables': {
            'path': f'/for-sale/property/england/?added=24_hours&property_type={property_type}&pn={page_num}',
        },
        'query': 'query getListingData($path: String!) {\n  breadcrumbs(path: $path) {\n    label\n    tracking\n    uri\n    noAppend\n    i18nLabelKey\n    __typename\n  }\n  seoAccordions(path: $path) {\n    category\n    expanded\n    geo\n    name\n    propertyType\n    section\n    transactionType\n    rows {\n      links {\n        category\n        geo\n        propertyType\n        section\n        transactionType\n        uri\n        __typename\n      }\n      __typename\n    }\n    links {\n      category\n      geo\n      propertyType\n      section\n      transactionType\n      uri\n      __typename\n    }\n    __typename\n  }\n  discoverMore(path: $path) {\n    housePricesUri\n    findAgentsUri\n    __typename\n  }\n  searchResults(path: $path) {\n    analyticsTaxonomy {\n      url\n      areaName\n      activity\n      brand\n      countryCode\n      countyAreaName\n      currencyCode\n      listingsCategory\n      outcode\n      outcodes\n      page\n      postalArea\n      radius\n      radiusAutoexpansion\n      regionName\n      resultsSort\n      searchGuid\n      searchIdentifier\n      section\n      searchLocation\n      viewType\n      searchResultsCount\n      expandedResultsCount\n      totalResults\n      emailAllFormShown\n      emailAllTotalAgents\n      bedsMax\n      bedsMin\n      priceMax\n      priceMin\n      location\n      propertyType\n      __typename\n    }\n    analyticsEcommerce {\n      currencyCode\n      impressions {\n        id\n        list\n        position\n        variant\n        __typename\n      }\n      __typename\n    }\n    adTargeting {\n      activity\n      areaName\n      bedsMax\n      bedsMin\n      brand\n      brandPrimary\n      countyAreaName\n      countryCode\n      currencyCode\n      listingsCategory\n      outcode\n      outcodes\n      page\n      postalArea\n      priceMax\n      priceMin\n      propertyType\n      regionName\n      resultsSort\n      searchLocation\n      searchResultsCount\n      section\n      totalResults\n      url\n      viewType\n      __typename\n    }\n    metaInfo {\n      title\n      description\n      canonicalUri\n      __typename\n    }\n    pagination {\n      pageNumber\n      totalResults\n      totalResultsWasLimited\n      __typename\n    }\n    listings {\n      regular {\n        numberOfVideos\n        numberOfImages\n        numberOfFloorPlans\n        numberOfViews\n        listingId\n        title\n        publishedOnLabel\n        publishedOn\n        availableFrom\n        priceDrop {\n          lastPriceChangeDate\n          percentageChangeLabel\n          __typename\n        }\n        isPremium\n        highlights {\n          description\n          label\n          url\n          __typename\n        }\n        otherPropertyImages {\n          small\n          large\n          caption\n          __typename\n        }\n        branch {\n          name\n          branchDetailsUri\n          phone\n          logoUrl\n          branchId\n          __typename\n        }\n        features {\n          content\n          iconId\n          __typename\n        }\n        image {\n          src\n          caption\n          responsiveImgList {\n            width\n            src\n            __typename\n          }\n          __typename\n        }\n        transports {\n          title\n          poiType\n          distanceInMiles\n          features {\n            zone\n            tubeLines\n            __typename\n          }\n          __typename\n        }\n        flag\n        listingId\n        priceTitle\n        price\n        alternativeRentFrequencyLabel\n        address\n        tags {\n          content\n          __typename\n        }\n        listingUris {\n          contact\n          detail\n          __typename\n        }\n        __typename\n      }\n      extended {\n        numberOfVideos\n        numberOfImages\n        numberOfFloorPlans\n        numberOfViews\n        listingId\n        title\n        publishedOnLabel\n        publishedOn\n        availableFrom\n        priceDrop {\n          lastPriceChangeDate\n          percentageChangeLabel\n          __typename\n        }\n        isPremium\n        highlights {\n          description\n          label\n          url\n          __typename\n        }\n        otherPropertyImages {\n          small\n          large\n          caption\n          __typename\n        }\n        branch {\n          name\n          branchDetailsUri\n          phone\n          logoUrl\n          branchId\n          __typename\n        }\n        features {\n          content\n          iconId\n          __typename\n        }\n        image {\n          src\n          caption\n          responsiveImgList {\n            width\n            src\n            __typename\n          }\n          __typename\n        }\n        transports {\n          title\n          poiType\n          distanceInMiles\n          features {\n            zone\n            tubeLines\n            __typename\n          }\n          __typename\n        }\n        flag\n        listingId\n        priceTitle\n        price\n        alternativeRentFrequencyLabel\n        address\n        tags {\n          content\n          __typename\n        }\n        listingUris {\n          contact\n          detail\n          __typename\n        }\n        __typename\n      }\n      featured {\n        numberOfVideos\n        numberOfImages\n        numberOfFloorPlans\n        numberOfViews\n        listingId\n        title\n        publishedOnLabel\n        publishedOn\n        availableFrom\n        priceDrop {\n          lastPriceChangeDate\n          percentageChangeLabel\n          __typename\n        }\n        isPremium\n        featuredType\n        highlights {\n          description\n          label\n          url\n          __typename\n        }\n        otherPropertyImages {\n          small\n          large\n          caption\n          __typename\n        }\n        branch {\n          name\n          branchDetailsUri\n          phone\n          logoUrl\n          __typename\n        }\n        features {\n          content\n          iconId\n          __typename\n        }\n        image {\n          src\n          caption\n          responsiveImgList {\n            width\n            src\n            __typename\n          }\n          __typename\n        }\n        transports {\n          title\n          poiType\n          distanceInMiles\n          features {\n            zone\n            tubeLines\n            __typename\n          }\n          __typename\n        }\n        flag\n        listingId\n        priceTitle\n        price\n        alternativeRentFrequencyLabel\n        address\n        tags {\n          content\n          __typename\n        }\n        listingUris {\n          contact\n          detail\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    filters {\n      fields {\n        group\n        fieldName\n        label\n        isRequired\n        inputType\n        placeholder\n        allowMultiple\n        options\n        value\n        __typename\n      }\n      __typename\n    }\n    links {\n      saveSearch\n      createAlert\n      __typename\n    }\n    sortOrder {\n      currentSortOrder\n      options {\n        i18NLabelKey\n        value\n        __typename\n      }\n      __typename\n    }\n    seoBlurb {\n      category\n      transactionType\n      __typename\n    }\n    title\n    userAlertId\n    savedSearchAndAlerts {\n      uri\n      currentFrequency {\n        i18NLabelKey\n        value\n        __typename\n      }\n      __typename\n    }\n    polyenc\n    __typename\n  }\n}\n',
    }
    try:
        response = get_response(json_data)
        return response['data']['searchResults']['listings']['regular']
    except Exception as e:
        # Printing out any errors that occur during the request
        print(f"Error occurred during requests.post: {e}")
        return None

# Function to request detailed data for a specific listing
def request_listing_data(listing):
    dict1={}
    dict1['url'] = 'https://www.zoopla.co.uk'+listing['listingUris']['detail']
    # Retrieve features from the listing and add them to the dictionary
    f = listing['features']
    for i in f:
        dict1[i['iconId']] = i['content'] 
    ln = dict1['url']
    while True:
        try:
            # params = (
            #     ('access_token', 'proxy_token'),
            #     ('url', ln),
            # )
            # response = requests.get('https://api.quickscraper.co/parse', params=params)
            # Make a GET request to the listing URL
            response = requests.get(ln, params=params)            
            print('status:', response.status_code)
            response.text.split('"latitude": ')[1].split(',')[0]
            break
        except Exception as e:
            print(f"Error occurred during requests.get: {e}")
            print(ln)
            time.sleep(30)
            continue
    return response, dict1

# Function to parse the detailed listing data from the response
def parse_listing(response, dict1, listing, dict2):
    # Attempt to parse various details from the response
    try:
        postcode_district = response.text.split('"incode":"')[1].split('"')[0]
        outcode = response.text.split('"outcode":"')[1].split('"')[0]
        postcode =  outcode+ ' '+ postcode_district
    except:
        postcode = ''
        postcode_district = ''
        outcode = ''
    try:
        lat = float(response.text.split('"latitude": ')[1].split(',')[0].strip())
        lon = float(response.text.split('"longitude": ')[1].split('\n')[0].strip())
    except:
        lat = ''
        lon = ''
    try:
        acorn_type = int(response.text.split('"acornType":')[1].split(',')[0])
    except:
        acorn_type = ''
    # Using BeautifulSoup to parse HTML content and extract descriptions
    s1 = BeautifulSoup(response.text,'lxml')
    description = s1.find('section',{'data-testid':"page_features_section"}).text.strip()
    property_type =response.text.split('"propertyType":"')[1].split('"')[0]
    dict1['property_type'] = property_type 
    dict1['postcode'] = postcode
    dict1['outcode'] = outcode
    dict1['postcode_district'] = postcode_district
    dict1['acorn_type'] = acorn_type
    dict1['display_address'] = listing['address'].replace(postcode,outcode)
    dict1['price'] = listing['price']
    dict1['latitude'] = lat
    dict1['longitude'] = lon
    dict1['description'] = description
    # Add parsed data to the dictionary and create a DataFrame
    dict2[listing['listingId']] = pd.DataFrame(dict1,index=[0])

# Function to clean and organize the property data collected
def clean_property_data(dict2, dt):
    # Concatenate the individual DataFrames into a single DataFrame
    df = pd.concat(dict2.values(),sort=False)
    df['listing_condition']='pre-owned'
    df['price'] = pd.to_numeric(df["price"].replace("[£,]", "", regex=True), errors ='coerce').fillna(0).astype('int')
    df['listing_id'] = np.NaN
    df = df.rename(columns={'chair': 'num_recepts','bed':'num_beds','bath':'num_baths'})
    df.replace('', np.nan, inplace=True)
    df = df[['property_type','price','postcode_district','num_baths','postcode','outcode','acorn_type',
        'display_address','num_recepts','num_beds','url','listing_condition','latitude','longitude','description']]
    df['date'] = dt
    df.drop_duplicates(inplace=True)
    # Save the cleaned DataFrame to an Excel file
    df.to_excel('zoopla_data.xlsx',index=False)

# Main function to start the data scraping process
def main():
    try:
        # Setting the current date for use in the DataFrame
        dt = datetime.today().strftime('%Y-%m-%d')
        # Defining the list of property types to scrape
        property_types = ['farms_land','semi_detached','flats','detached','terraced','bungalow','park_home']
        # Dictionary to hold the DataFrames for each listing
        dict2 = {}
        # Loop over each property type and scraping the data
        for property_type in property_types:
            page_num = 1
            while True:
                listings = get_page_listings(page_num, property_type)
                print('\nScraping page #',page_num)
                if listings is None or len(listings) == 0:
                    print('Completed.')
                    break
                for listing in listings:
                    response, dict1 = request_listing_data(listing)
                    parse_listing(response, dict1, listing, dict2)
                    sys.stdout.write(".")
                    sys.stdout.flush()
                page_num += 1
        clean_property_data(dict2, dt)
    except Exception as e:
        print(e)
        send_discord_notification(df,e)


if __name__ == '__main__':
    main()
