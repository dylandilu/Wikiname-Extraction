# Wikiname-Extraction
The script is a tool to extrac gazetteer for target language from [Wikipedia](https://www.wikipedia.org/).

The script is written in Pythton 3.6+

# Usage
[Downlad](https://www.dropbox.com/s/x0w1fljdz33ynoh/all-data.uniq?dl=0) preprocessed Wiki dataabse.

```
python gaz_mine.py --target_language LAN_CODE --output_dir OUTPUT_DIR --database PATH_DOWNLOADED_WIKI_DATABASE
```

LAN_CODE is ISO 639-1 language code

output format (names in TARGET language, English and Name type, separted by tab)
```
一一九號橋      Number 119 Bridge       GPE
一一五號橋      Number 115 Bridge       GPE
一宮市  Ichinomiya, Aichi       GPE
一宮町  Ichinomiya, Chiba       GPE
一戶町  Ichinohe, Iwate GPE
一月山口        January Col     GPE
```