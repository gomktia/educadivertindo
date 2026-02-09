
import os

def inspect_all_video_tags():
    filepath = "/Users/pantera/Desktop/Projetos/Recetario Ancestral/index.html"
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    search_term = "<video class=ls-video"
    count = content.count(search_term)
    print(f"Found {count} occurrences of '{search_term}'")
    
    start_search = 0
    for i in range(count):
        idx = content.find(search_term, start_search)
        if idx != -1:
            print(f"Occurrence {i+1} at index {idx}:")
            print(content[idx:idx+300])
            print("-" * 20)
            start_search = idx + 1

if __name__ == "__main__":
    inspect_all_video_tags()
