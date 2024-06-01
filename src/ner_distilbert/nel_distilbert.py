import os
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


def extract_name_and_last_name(text):
    """
    Extracts the items labeled as LABEL_1 and LABEL_2 from the given text using a pre-trained NER model.
    Args:
        text (str): The text from which to extract the labeled items.
    Returns:
        dict: A dictionary containing lists of items labeled 'LABEL_1' and 'LABEL_2'.
    """
    # Define the project root and model path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    model_path = os.path.join(project_root, 'models', 'distilbert-NER')
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    # Initialize the NER pipeline
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    # Perform NER on the input text
    ner_results = nlp(text)

    label_1_tokens = []
    label_2_tokens = []
    # Extract items based on their labels and handle subwords
    for entity in ner_results:
        if entity['entity'] == 'LABEL_1':
            label_1_tokens.append(entity['word'])
        elif entity['entity'] == 'LABEL_2':
            label_2_tokens.append(entity['word'])

    # Function to join tokens and remove ##
    def clean_tokens(tokens):
        words = []
        current_word = ""
        for token in tokens:
            if token.startswith("##"):
                current_word += token[2:]
            else:
                if current_word:
                    words.append(current_word)
                current_word = token
        if current_word:
            words.append(current_word)
        return words

    labeled_items = {
        'name': clean_tokens(label_1_tokens),
        'last_name': clean_tokens(label_2_tokens)
    }
    return labeled_items