from dotenv import load_dotenv, dotenv_values
from openai import OpenAI
import os


load_dotenv()
var1 = os.getenv("OPENAI_KEY")

client = OpenAI(
api_key = var1
)

def recommend_products(skin_issue):
    prompt = f"I have a skin issue: {skin_issue}. Please do extensive research to recommend me the right products for my problem. "

    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [{
     "role": "user",
     "content": prompt,
    },
    {
     "role": "system",
     "content": "You are a skincare expert who is part of AesticAI whose job is to recommend the right products and skincare routines to people. Depending on their skin issue, (very important) you have to give a very brief one-sentence reason as to how this skin problem arises, then recommend a list of the top 3 products that would help their issue. You should explain how to use this product,for how long, and how often but keep it brief and the the point. Don't make the response too lengthy and only respond in one block of text. Refrain from using measurements such as teaspoon or tablespoon and use more visualizable measurements e.g. dime-sized, pea-sized, handful .",
    },
    {
     "role": "user",
     "content": "generate the top 3 products(with a companyproduct) that the user should use. Also include how to use it(ie apply twice a day on damp skin). and give a estimated usage timeline(ie continue this for ___ days/months/weeks and you should be fine). give it to me in one paragraph without additional formatting)",
    },
    {
     "role": "assistant",
     "content": "For treating acne, consider starting with these three products: CeraVe Foaming Facial Cleanser, Paula's Choice 2% BHA Liquid Exfoliant, and La Roche-Posay Effaclar Duo Acne Treatment Cream. Begin by using the CeraVe cleanser twice daily, morning and night, on damp skin, then rinse thoroughly to remove oil and impurities without disrupting the skin barrier. After cleansing, apply Paula’s Choice BHA Exfoliant once daily in the evening on dry skin, which will gently exfoliate pores and reduce inflammation; avoid applying on damp skin to prevent irritation. Finish with La Roche-Posay’s Effaclar Duo, a spot treatment that should be applied in a thin layer over problem areas once or twice a day as needed. Stick to this routine for 6-8 weeks, and you should begin to see significant improvement in acne, with continued use helping to prevent future breakouts.  ",
    }]
        )     
    result = response.choices[0].message.content
    return result
def recommend_routine(specific_products):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [{
     "role": "user",
     "content": f" I have a skin problem, here are the products that have been recommended to me and how to use them: {specific_products}.  now generate an entire skin care routine implementing these products to help the user have perfect skin. I want you to use the format, Morning, shower -> this product(include quantity and duration) -> this product -> this product(in the best order) and then continue for the rest of the day    ",
    },
    {
     "role": "system",
     "content": "You are a skincare expert who is part of AesticAI whose job is to recommend the right products and skincare routines to people depending on their skin issue. You should integrate these products that are given with their uses into a skincare routine using not only the products given but also other products that are used to better skin in general. You should explain how to use this product,for how long, and how often but keep it brief and to the point.use the format, Morning, shower -> this product(include quantity and duration) -> this product -> this product(in the best order) and then continue for the rest of the day. MAKE A MAXIMUM OF 8 BULLET POINTS DO NOT MAKE THEM TOO LONG ",
    },
    {
     "role": "system",
     "content": "Do not try to do any formatting other than bullet points. By that I mean do not try to make any words bold or italic or anything like that."
     },
    { "role": "system",
     "content": f"You HAVE to implement the exact products that are given in this: {specific_products}. Make sure to use the exact names and methods given in that paragraph. Refrain from using measurements such as teaspoon or tablespoon and use more visualizable measurements e.g. dime-sized, pea-sized, handful "}
    ]
    )  
    result = response.choices[0].message.content
    return result
def learn_more_products(products):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [{
     "role": "user",
     "content": f" I have a skin problem, here are the products that have been recommended to me and how to use them: {products}. I want to learn more ",
    },
    {
     "role": "system",
     "content": f"You are a skincare expert who is part of AesticAI whose job is to expand and go into more detail on these products. this response is meant to be a response for the learn more section of this: {products}. Just give more details and be more precise so that the user comes out learning more about the products and how to use them. Do not try to make the text bold or italic or anything like that. Also I want outputting one paragraph  ",
    },
    ]
    )  
    result = response.choices[0].message.content
    return result

    
