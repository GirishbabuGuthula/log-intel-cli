from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering

def cluster_log_messages(messages, distance_threshold=0.7):
    if len(messages) < 2:
        return {}
    
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))

    x = vectorizer.fit_transform(messages)

    clustering = AgglomerativeClustering(
        metric='cosine',
        linkage='average',
        distance_threshold=distance_threshold,
        n_clusters=None
    )

    labels = clustering.fit_predict(x.toarray())

    clusters = {}

    for label, msg in zip(labels, messages):
        clusters.setdefault(str(label), []).append(msg)

    return clusters