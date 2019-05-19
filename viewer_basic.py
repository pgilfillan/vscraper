import pickle
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Title", "Date", "URL"]
with open('videos.data', 'rb') as f:
    videos = pickle.load(f)
    for video in videos:
        table.add_row(video)
print(table)
