with open ("donotfly.kml", 'rt', encoding = 'utf-8') as f:
    while True:
        doc = f.readline()
        if doc is " ":
            print (doc)
        if not doc:
            break