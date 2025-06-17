import requests
from bs4 import BeautifulSoup
import time

def get_live_scores():
    url = 'https://www.cricbuzz.com/cricket-match/live-scores'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    match_blocks = soup.find_all('div', class_='cb-mtch-lst')
    
    if not match_blocks:
        print("❌ No live matches found.")
        return

    for block in match_blocks:
        title_tag = block.find('h3')
        if not title_tag:
            continue

        title = title_tag.text.strip()

        score_tag = block.find('div', class_='cb-ltst-wgt-hdr')
        score = score_tag.text.strip() if score_tag else "Score not available"

        print(f"\n🏏 Match: {title}")
        print(f"📊 {score}")
        print("-" * 60)

if __name__ == '__main__':
    while True:
        print("\n📡 Fetching live scores...\n")
        get_live_scores()
        time.sleep(30)
