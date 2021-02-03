import urllib.request
import json
# import requests
titles = []
def getarticleTitles(author):
    content = urllib.request.urlopen('https://jsonmock.hackerrank.com/api/articles?author={}&page=1'.format(author))
    output = content.read()
    data_dict = json.loads(output)
    np = data_dict.get('total_pages')
    # print('page count',np)
    # data = data_dict.get('data')
    # print(data)
    # print(len(data))
    for y in range(np):
        load = urllib.request.urlopen('https://jsonmock.hackerrank.com/api/articles?author={}&page={}'.format(author,(y+1)))
        output_y = load.read()
        data_dict_y = json.loads(output_y)
        data_y = data_dict_y.get('data')
        for x in range(len(data_y)):
            entry = data_y[x]
            title = entry.get('title')
            if title == None:
                title = entry.get('story_title')
            # print(title)
            titles.append(title)
        print(titles)



getarticleTitles('epaga')

# print(output)
# print(data_dict)


# first = data[0]
# print(first)
# title_1 = first.get('title')
# print(title_1)



# key_list = list(data_dict)
# # print(key_list)
# value_list = list(data_dict.values())
# print(value_list)


