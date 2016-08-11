def convertEpoch(epoch):
    timestamp = datetime.datetime.fromtimestamp(epoch)
    date = timestamp.strftime('%Y-%m-%d')
    return date
