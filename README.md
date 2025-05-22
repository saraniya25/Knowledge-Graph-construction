
# 📚Knowledge Graph Construction From Text:

This project extracts subject–predicate–object triplets from user-input sentences and visualizes them as a knowledge graph.


## ✨Features

- Extracts triplets like (subject, relation, object) from English text.

- Supports multiple user inputs.
- Visualizes knowledge graphs using NetworkX and matplotlib.
-  Handles basic passive and active voice constructs.



## 📁 Project Structure
```bash
 Knowledge-Graph-Construction/
├── main.py                # Main program to run the input loop and visualize graph
├── src/
│   ├── extractor.py       # spaCy-based triplet extraction logic
│   └── graph_builder.py   # Graph construction and aesthetic visualization
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
## 🚀 Installation

1. Clone the Repository

```bash
git clone https://github.com/AmreenShaheen/Knowledge-Graph-Construction.git
cd knowledge-graph-construction
```
2. Install Dependencies

```bash
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # on Windows use: venv\Scripts\activate
```
3. Install the required packages
```bash
pip install -r requirements.txt
```
4. Download the spaCy language model
```bash
python -m spacy download en_core_web_sm
```


    
## 💻 Usage/Examples

```
python main.py
```
You will be prompted to enter multiple sentences or paragraphs. Type exit to stop and visualize the knowledge graph.

Example Input:
```
Elon Musk founded SpaceX.

```
Expected Triplets:
```
('Musk', 'found', 'SpaceX.')

```




## 📊 Output
- A static but a visual graph window will open.

- Nodes represent entities (subjects/objects).

- Arrows represent the relationships (predicates).

- Labels are clean and color-coded for clarity.