import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import strimilarity

sentences = [
    'All you have to decide is what to do with the time that is given to you.',
    'You have to decide what to do now, we do not have time.',
    'Do whatever you want to do, we have time.',
    'Hello there. Genral Kenobi.'
]

starty = strimilarity.Strimilarity()

similarity = starty.semantic_similarity(sentences)

print(similarity)

df = pd.DataFrame(similarity)
df.columns = sentences
df.index = sentences
fig, ax = plt.subplots(figsize=(4,4))
hm = sns.heatmap(df, cmap="YlGnBu")
fig = hm.get_figure()
fig.savefig("output.png", bbox_inches="tight")