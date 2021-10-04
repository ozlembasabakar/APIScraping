import requests
import pandas as pd 
import sqlalchemy

address = []
bedrooms = []
bathrooms = []
size = []
car_park = []
agent_name = []
area_code = []
phone_number = []
price = []

for j in range(1,51):
    headers = {
        'authority': 'api2.realtor.ca',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.realtor.ca',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.realtor.ca/',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'visid_incap_2269415=8HQea9juRNObJfEiRvWxULswVGEAAAAAQUIPAAAAAAA7XNpmuY+NM7gsa3F0kvbE; nlbi_2269415=xefuE7HKPnf+6Sb3kG5lugAAAAA7d3sWGCEi5fqWQhrONBaX; incap_ses_1345_2269415=iKoZIiepcC0CXPG9nmaqErswVGEAAAAA7BDFzUA3cnFQzORTqBUz4Q==; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=j5s0g2ojjvjusuuzuf3etz4w; visid_incap_2271082=N5nE0PHIT4Wq//EaYOS6V/owVGEAAAAAQUIPAAAAAAABlqZI8dwnjt9N7scQ78zL; nlbi_2271082=9JiRNf2icDq4BUUTcbDG1QAAAABI4pQ5S1jFHuHx50B2PGV5; incap_ses_1290_2269415=cjpyBkCV7mlyTBX7bQDnEZ+XVWEAAAAAM8xKdCw8+0tKOA05QOKVZA==; incap_ses_1190_2269415=VxA1CtIg1xf8cPWvL7uDEBfuVmEAAAAA+RWdh2QkXfZ6GPXJmeJ4rA==; nlbi_2269415_2147483646=td2pDVru/FUjIog7kG5lugAAAAAaNEqXuVm3/Z+hEMyXbe7r; reese84=3:R12YCfGDNXuZBUr39beeVg==:s9Ls4phtgSfgYK4YidyiydgGxPn/CxTJ37+uyA5WatuW3PH7Qmd+XRy0rg+gWYUi7+4okOJ3ntt9Oml56KxPBw16dhzAcuaXG+aQz3CuenXlzH0SijCpmn8oD/BwtCKISQyv6eY3bP95EGmCYA+YDHfjFY34E77s7YIfSTOIM/EAbOhrELHqXHT7UVi1YGZYSy+M/Kr5F9QQFFcDYg37hwS38cfZsPpitKfX+SoNZ4PWdbrvF0Jh+JCMhjcihdj93ya746rWOpml1BNUF3CIz85Ltj3od+2zeyaBPtP3MXr08ZFQcgLcyp+jpQ07O376Vle3f1a+AWy0r+qsT4sVmyHNgD3l6Qq7g8K+D1F3rdxor7N6uo4+vUygRwkaoPzYxesmQjA9zofygaLWpst/fPjIfLiCWUojkGziYK2ZWQT5Rg2pFbATzdbIQRtLKcB5:Kb0dE6ycMsKc0cAN+MHlok3yfPHfwb0WhKlVkMYaB80=; incap_ses_1190_2271082=fl3sZOUFqgy0ifWvL7uDEDnvVmEAAAAAv4e9OvTzLQJiYeNTliSQng==',
    }
    
    data = {
      'ZoomLevel': '9',
      'LatitudeMax': '45.69619',
      'LongitudeMax': '-74.38546',
      'LatitudeMin': '44.80092',
      'LongitudeMin': '-77.21444',
      'Sort': '6-D',
      'PropertyTypeGroupID': '1',
      'PropertySearchTypeId': '1',
      'TransactionTypeId': '2',
      'Currency': 'CAD',
      'RecordsPerPage': '12',
      'ApplicationId': '1',
      'CultureId': '1',
      'Version': '7.0',
      'CurrentPage': str(j),
    }
    
    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)
    
    result_json = response.json()
    
    result_Results = result_json['Results']
    
    '''
    # Address
    result_Results[0]['Property']['Address']['AddressText']
    
    # Bedrooms
    result_Results[0]['Building']['Bedrooms']
    
    # Bathrooms
    result_Results[0]['Building']['BathroomTotal']
    
    # Size 
    result_Results[0]['Land']['SizeTotal']
    
    # Park
    result_Results[0]['Property']['ParkingSpaceTotal']
    
    # Agent Name
    result_Results[0]['Individual'][0]['Name']
    
    # Area Code
    result_Results[0]['Individual'][0]['Phones'][0]['AreaCode']
    
    # Phone Number 
    result_Results[0]['Individual'][0]['Phones'][0]['PhoneNumber']
    
    # Price
    result_Results[0]['Property']['PriceUnformattedValue']
    '''


    
    for result in result_Results:
        
        try:
            address.append(result['Property']['Address']['AddressText'])
        except:
            address.append('Nan')
            
        try:
            bedrooms.append(result['Building']['Bedrooms'])
        except:
            bedrooms.append('Nan')
        
        try:
            bathrooms.append(result['Building']['BathroomTotal'])
        except:
            bathrooms.append('Nan')
    
        try:
            size.append(result['Land']['SizeTotal'])
        except:
            size.append('Nan')
    
        try:
            car_park.append(result['Property']['ParkingSpaceTotal'])
        except:
            car_park.append('Nan')
    
        try:
            agent_name.append(result['Individual'][0]['Name'])
        except:
            agent_name.append('Nan')
            
        try:
            area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
        except:
            area_code.append('Nan')
            
        try:
            phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
        except:
            phone_number.append('Nan')
        
        try:
            price.append(result['Property']['PriceUnformattedValue'])
        except:
            price.append('Nan')
    
size_total = []
for i in range(0, len(size)):
    
    if "Nan" in size[i]:
        size_total.append(size[i])
        
    if "x" in size[i]:
        a1 = size[i].split(" x ")
        a2 = float(a1[0])
        a3 = a1[1].split(" ")[0]
        a4 = float(a3)
        size_total.append(round(float(a2 * float(a4) * 0.093), 2))
        
    if "X" in size[i]:
        x = size[i].split(" ft")
        y = float(x[0])
        z = x[1].split(" X ")[1]
        
        if z == "*":
            size_total.append('Nan')
        else:
            size_total.append(round(float(y * float(z) * 0.093), 2))
   
    if "sqft" in size[i]:
        v = float(size[i].split(" sqft")[0])
        size_total.append(round(float(v * 0.09290304), 2))
    
    if "m2" in size[i]:
        size_total.append(float(size[i].split(" m2")[0]))
               
    if "ac" in size[i]:
        q1 = size[i].split(" ac")
        
        if "-" in q1[0]:
            q2 = q1[0].split(" - ")
            q3 = float(q2[0])
            q4 = float(q2[1])
            q5 = float(q3 * q4)
            size_total.append(round(float(q5 / 0.00024711),2))
        else:
            q6 = q1[0]
            q6 = float(q6)   
            size_total.append(round(float(q6 / 0.00024711),2))  

bedroom_fix = []
for k in range(len(bedrooms)):
    if "+" in bedrooms[k]:
        k1 = bedrooms[k].split("+")
        k2 = int(k1[0])
        k3 = int(k1[1])
        k4 = k2 + k3
        bedroom_fix.append(k4)
    elif "Nan" in bedrooms[k]:
        bedroom_fix.append(bedrooms[k])
    else:
        k5 = int(bedrooms[k])
        bedroom_fix.append(k5)
        

bathroom_fix = []
for l in range(len(bathrooms)):
    
    if "Nan" in bathrooms[k]:
        bathroom_fix.append(bathrooms[k])
        
    else:
        l1 = float(bathrooms[l])
        bathroom_fix.append(l1)

park_fix = []
for m in range(len(car_park)):
    
    if "Nan" in car_park[m]:
        park_fix.append(car_park[m])
        
    else:
        m1 = int(car_park[m])
        park_fix.append(m1)

price_fix = []
for n in range(len(price)):
    
    if "Nan" in price[n]:
        price_fix.append(price[n])
        
    else:
        n1 = int(price[n])
        price_fix.append(n1)



dataset = pd.DataFrame({'Address' : address,
                            'Bedrooms' : bedroom_fix,
                            'Bathrooms' : bathroom_fix,
                            'Park' : park_fix,
                            'Size(m2)' : size_total,
                            'Agent Name' : agent_name,
                            'Area Code' : area_code,
                            'Phone Number' : phone_number,
                            'Price($)' : price_fix})



dataset.to_excel('dataset.xlsx', index = False)









engine = sqlalchemy.create_engine('postgresql://postgres:ozlem123@localhost:5432')
 
dataset.to_sql('api_dataset', engine)



