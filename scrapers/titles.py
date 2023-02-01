import json

def extract_titles(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    titles = []
    for movie in data["grids"][0]["list"]:
        titles.append(movie["title"])

    with open(output_file, 'w') as f:
        for title in titles:
            f.write(title + '\n')


extract_titles("/home/igor/projects/scrapers/rottentomatoes.json", "movies_titles.txt")
