import dotenv
from openai import OpenAI

client = OpenAI(
api_key = open("APIKEY", "r").read())




def recommendation(skin_issue):
    prompt = f"I have a skin issue: {skin_issue}. Please do extensive research to recommend me the right products for my problem. "

    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages = [{
     "role": "user",
     "content": prompt,
    },
    {
     "role": "system",
     "content": "You are a skincare expert who is part of AesticAI whose job is to recommend the right products and skincare routines to people. Depending on their skin issue, you should recommend a list of the top 3 products that would help their issue. You should explain how to use this product,for how long, and how often but keep it brief and the the point. Don't make the response too lengthy and only respond in one block of text.",
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

print(recommendation("blackheads"))
