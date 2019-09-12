import json

with open('./dataset.json') as json_file:
    data = json.load(json_file)

    md = open("./README.md", "w+")
    md.flush()

    # Table of contents
    md.write("## Table of Contents\n")
    for topic in data:
        md.write(f"- [{topic}](#{topic.replace(' ', '-')})\n")
    md.write("\r\n")
    
    # Actual data here
    for topic in data:
        md.write(f"#### {topic}\r\n")
        for entry in data[topic]:
            md.write(f"* [{entry['label']}]({entry['url']}) - \n")
        md.write("\n")

    md.close()