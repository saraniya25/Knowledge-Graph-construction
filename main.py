from src.extractor import extract_triples
from src.graph_builder import build_graph  # assuming graph_builder is inside src/

def main():
    print("You can input multiple sentences or paragraphs. Type 'exit' to stop.")
    all_triplets = []

    while True:
        text = input("Enter a sentence or paragraph (type 'exit' to stop): ")
        if text.lower() == 'exit':
            break

        triples = extract_triples(text)
        if triples:
            print("\n✅ Extracted Triplets:")
            for triplet in triples:
                print(triplet)
            all_triplets.extend(triples)
        else:
            print(f"❌ No triplets extracted from: '{text}'")

    if all_triplets:
        print("\nAll Extracted Triplets:")
        for t in all_triplets:
            print(t)
        build_graph(all_triplets)
    else:
        print("\n❌ No valid triplets were extracted from the input.")

if __name__ == "__main__":
    main()
