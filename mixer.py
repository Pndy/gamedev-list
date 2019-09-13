import json

# Opens one of the datasets and parses it 
with open('./dataset_new.json', encoding="utf8") as json_file:
    data = json.load(json_file)

    # Opens the other dataset and parses it
    old = open("./dataset_old.json", encoding="utf8")
    data_old = json.load(old)

    # Loops thru all of the topics and entries, looking for empty titles
    # if one is found, it looks for the title from another dataset with the mirror data
    for topic in data:
        for idx, entry in enumerate(data[topic]):
            if entry['title'] == "":
                data[topic][idx]['title'] = data_old[topic][idx]['title']
    
    # finally opens the final dataset,flushes it and saves the modified data into it
    with open("./dataset.json", "w+", encoding="utf8") as f:
        f.flush()
        json.dump(data, f, indent=4)

    