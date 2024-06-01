import os
import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def ask_rag_llama2(input_quest, context_texts):
    """
    Generate an answer to a question using the RAG (Retrieval-Augmented Generation) model.
    This function takes a question and context texts as input, loads the RAG model,
    generates a system prompt with the question and context, tokenizes the input,
    generates a response using the model, and returns the generated answer.
    Args:
        input_quest (str): The question for which an answer is to be generated.
        context_texts (str): The context or text relevant to the question.
    Returns:
        str: The generated answer.
    """
    timeStart = time.time()
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    model_path = os.path.join(project_root, 'models', 'Llama-2-7b-chat-hf')
    input_token_length = 200

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map='auto'
    )

    print("Load model time: ", - timeStart + time.time())

    sys_prompt = '''Provide an answer to the following question based on the following text. Answer the best of your capabilities.'''

    template = f"""[INST] <<SYS>>\n""" \
               f"""{sys_prompt}\n""" \
               f"""<</SYS>>\n""" \
               f"""Question:\n""" \
               f"""{input_quest}\n""" \
               f"""Text:\n""" \
               f"""{context_texts}[/INST]"""

    inputs = tokenizer.encode(template, return_tensors="pt")

    outputs = model.generate(
        # inputs,
        inputs.to('cuda'),
        max_new_tokens=int(input_token_length),
        temperature=0.9,
        do_sample=True
    )
    init = template.find(']', 7) + 6
    output_str = tokenizer.decode(outputs[0])[init:]
    return output_str
