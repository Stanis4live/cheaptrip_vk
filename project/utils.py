import datetime as DT

# переводит строку во время от начала эпохи
def date_to_unix(date: str):
    dt = DT.datetime.fromisoformat(date)
    return dt.timestamp()


