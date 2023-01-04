from transformers import pipeline


def Generate_Text(
        txt):
    gen = pipeline("text-generation", model="gpt2")
    output = gen(txt, max_length=100,
                 num_return_sequences=1)
    return output[0]['generated_text']


print(Generate_Text("Science of the future"))
