import openai
import streamlit as st

openai.api_key = os.environ.get("OPENAI_API_KEY")
model_engine = "text-davinci-003"

def generate_affiliate_article(prompt, products):
    prompt = (f"{prompt}\n\n"
             f"SEO Affiliate Marketing Article for Amazon Products\n"
             f"Generate a SEO friendly article about the following Amazon products:\n\n")
    product_list = ""
    for i in range(len(products)):
        product_list += f"{products[i]} \n"
    prompt += product_list + "\n"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title("SEO Affiliate Marketing Article Generator")

prompt = st.text_input("Enter a prompt:")
products = [st.text_input(f"Product {i} URL:") for i in range(1, 6)]
if st.button("Generate Article") and any(products):
    products = [p for p in products if p]
    article = generate_affiliate_article(prompt, products)
    st.write("Generated Article:")
    st.write(article)
