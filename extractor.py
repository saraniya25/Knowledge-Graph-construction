import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_triples(text):
    doc = nlp(text)
    triples = []

    for sent in doc.sents:
        subject = ""
        relation = ""
        obj = ""

        for token in sent:
            if "subj" in token.dep_:
                subject = token.text
            if token.dep_ == "ROOT":
                relation = token.lemma_
            if "obj" in token.dep_ or token.dep_ == "xcomp":
                obj = token.text

        if subject and relation:
            triples.append((subject, relation, obj))

    return triples
