import os
import re
import requests
from datetime import datetime, timezone, timedelta
from tqdm import tqdm

HANDLE = "pyliasec"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGUAGES = {
    "C": ".c",
    "Cpp": ".cpp",
    "Go": ".go",
    "Python3": ".py",
}

TIER_IMG_PATH = "assets/tier"

def get_solved_count(handle):
    response = requests.get("https://solved.ac/api/v3/user/show", params={"handle": handle})
    response.raise_for_status()
    return int(response.json()["solvedCount"])

def get_problems(handle, page):
    response = requests.get("https://solved.ac/api/v3/search/problem", params={
        "query": f"solved_by:{handle}",
        "direction": "asc",
        "page": page,
        "sort": "id"
    })
    response.raise_for_status()
    return response.json()

def get_problem_tier(level):
    tier = {
        0: "Unrated", 1: "B5", 2: "B4", 3: "B3", 4: "B2", 5: "B1",
        6: "S5", 7: "S4", 8: "S3", 9: "S2", 10: "S1",
        11: "G5", 12: "G4", 13: "G3", 14: "G2", 15: "G1",
        16: "P5", 17: "P4", 18: "P3", 19: "P2", 20: "P1",
        21: "D5", 22: "D4", 23: "D3", 24: "D2", 25: "D1",
        26: "R5", 27: "R4", 28: "R3", 29: "R2", 30: "R1"
    }
    return f'<img alt="{tier[level]}" src="{TIER_IMG_PATH}/{level}.svg">'

def escape_title(title):
    return title.replace("|", "\\|").replace("\\(", "$").replace("\\)", "$")

def find_solution_paths(problem_id):
    results = []
    for lang_folder, ext in LANGUAGES.items():
        range_folder = f"{problem_id//10000*10000}~{problem_id//10000*10000 + 9999}"
        path = os.path.join(BASE_DIR, lang_folder, range_folder, "solved", f"{problem_id}{ext}")
        if os.path.exists(path):
            rel_path = os.path.relpath(path, BASE_DIR).replace("\\", "/")
            results.append(f"[{lang_folder}]({rel_path})")
    return " ".join(results)

def get_header():
    now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M:%S")
    return f"""<div align="center">

# Baekjoon

**백준 문제 풀이 저장소**

[![solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=pyliasec)](https://solved.ac/pyliasec)
![solved.ac 잔디](http://mazandi.herokuapp.com/api?handle=pyliasec&theme=warm)

마지막으로 업데이트: {now} (KST)

Ctrl+F 단축키로 문제를 찾는 것을 권장합니다.

코드를 그대로 복붙하는 것은 자제 부탁드립니다.

</div>

"""

def get_table(problems):
    table = "| 번호 | 제목 | 레벨 | 코드 |\n|:---:|:---:|:---:|:---:|\n"
    print("Generating table...")
    for pid, title, level in tqdm(problems):
        escaped_title = escape_title(title)
        tier_img = get_problem_tier(level)
        links = find_solution_paths(pid)
        table += f"| {pid} | {escaped_title} | {tier_img} | {links} |\n"
    return table

if __name__ == "__main__":
    solved_count = get_solved_count(HANDLE)
    total_pages = (solved_count - 1) // 50 + 1
    problems = []

    print(f"Fetching problems (total pages: {total_pages})")
    for page in tqdm(range(1, total_pages + 1)):
        data = get_problems(HANDLE, page)
        for item in data["items"]:
            problems.append((int(item["problemId"]), item["titleKo"], int(item["level"])))

    content = get_header() + get_table(problems)

    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md successfully updated.")
