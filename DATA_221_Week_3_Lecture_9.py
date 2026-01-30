# #ec9c6bf605104eceaf0bd59545721eaa
#
# from newsapi import NewsApiClient
#
# news_api = NewsApiClient(api_key = "ec9c6bf605104eceaf0bd59545721eaa")
#
# articles =news_api.get_everything(q="artificial intelligence", language="en", page_size=3)
#
# for article in articles["articles"]:
#     print(article["title"])
#     print(article["source"]["name"])
#
# from sklearn.preprocessing import StandardScaler
# data = [[10, 90], [12, 96], [9, 120], [13, 112], [8, 88]]
#
# scaler = StandardScaler()
# data2 = scaler.fit_transform(data)
#
# print(data)
# sum = 0
# sum2 = 0
#
# for element in data:
#     for item in element:
#         sum = item + sum
#
# mean = sum/5
# print(mean)
#
# for element in data2:
#     for item in element:
#         sum2 = item + sum2
#
# mean2 = sum2 / 5
# print(mean2)