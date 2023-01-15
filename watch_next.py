import spacy

# Advanced language model
nlp = spacy.load("en_core_web_md")

# Reading file and storing results.
movies = {}

with open("movies.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        line = line.split(' :')
        movies[line[0]] = line[1]


def recommender(sentence_to_compare):
    """Returns a recommendation based on results of comparing descriptors."""
    model_sentence = nlp(sentence_to_compare)
    rating = 0
    movie = None
    for key, descriptor in movies.items():
        similarity = nlp(descriptor).similarity(model_sentence)
        if similarity > rating:
            rating = similarity
            movie = key
    return movie


# Movie description to be compared with movies in dictionary
watched_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous " \
                "for the Earth, the illuminati trick Hulk into a shuttle and launch him into space" \
                "to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet " \
                "Sakaar where he is sold into slavery and trained as a gladiator."

# Call function to compare
recommended = recommender(watched_movie)

# Display results
print(f"We recommend {recommended} - {movies[recommended]}")
