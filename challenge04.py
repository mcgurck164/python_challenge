import requests
import re
import numpy as np
import pandas as pd


def get_html(url):
    res = requests.get(url, timeout=60)
    res.raise_for_status()
    return res.text


def solve():
    BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    START_NUM = "12345" # Part 1
    START_NUM = "8022" # Part 2
    START_NUM = "63579" # Part 3

    nums = [START_NUM]
    urls = []
    texts = []

    num = START_NUM

    while True:
        urls.append(BASE_URL + nums[-1])
        text = get_html(urls[-1])
        texts.append(text)

        pattern = r"[\d]+"
        pattern = r"the next nothing is ([\d]+)"
        match = re.search(pattern, texts[-1])
        # TODO: Checken, wie man prüft, ob re einen match findet
        if match:
            num = match.group(1)
            nums.append(num)
        else:
            break

    df = pd.DataFrame({"URL": urls, "Num": nums, "Text": texts})
    return df


if __name__ == "__main__":
    df = solve()
    df.to_excel("challenge04_3.xlsx", index=False)
    print(df)
