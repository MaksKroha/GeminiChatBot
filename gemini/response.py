from gemini import client


def get_gemini_response(text):
    return client.models.generate_content(model="gemini-2.0-flash", contents=text).text