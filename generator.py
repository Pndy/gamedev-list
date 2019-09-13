import json

# Opens dataset.json, not included but can be found at
# https://old.reddit.com/r/Unity3D/comments/d2wwcx/the_biggest_game_development_resources_list_is/ezyqd6e/
# or the 'final' dataset from here: https://pastebin.com/TTqEiG1S
with open('./dataset.json', encoding="utf8") as json_file:
    # parses the file as
    data = json.load(json_file)

    # Opens the README file for editing, and flushes/deletes the whole document
    md = open("./README.md", "w+", encoding="utf8")
    md.flush()

    # Table of contents
    md.write("## Table of Contents\n")
    for topic in data:
        md.write(f"- [{topic}](#{topic.replace(' ', '-')})\n")
    md.write("\r\n")
    
    # Divider
    md.write("---\n")
    
    # Actual data here
    for topic in data:
        md.write(f"#### {topic}\r\n")
        for entry in data[topic]:
            md.write(f"* [{entry['label']}]({entry['url']}) - {entry['title']}\n")
        md.write("\n")
    
    # Closes the README file
    md.close()