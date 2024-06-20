import json
import pandas as pd

data = []
for year in [2004, 2014, 2024]:
    # Load Kanji search data
    with open(f'normalized_kanji_data_{year}.json') as f:
        kanji_data = json.load(f)

    # Load similarity data
    with open(f'{year}_tau_similarity.json') as f:
        tau_similarity = json.load(f)
    with open(f'{year}_spearman_similarity.json') as f:
        spearman_similarity = json.load(f)

    # Combine data into a DataFrame
    
    for prefecture, kanji_list in kanji_data.items():
        for kanji, frequency in kanji_list:
            data.append({
                'Prefecture': prefecture,
                'Year': year,
                'Kanji': kanji.split(':')[0],
                'Frequency': frequency,
                'Tau Similarity': tau_similarity.get(prefecture, 0),
                'Spearman Similarity': spearman_similarity.get(prefecture, 0)
            })

df = pd.DataFrame(data)
df.to_csv('combined_data.csv', index=False)
