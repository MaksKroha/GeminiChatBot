from gemini import client
from gemini import SEPARATOR


def get_gemini_response(text, context=""):
    message = ""
    if context != "":
        message = f"Here's the story of the dialog:\n"
        for i, msg in enumerate(context.strip(SEPARATOR).split(SEPARATOR)):
            message = message + f'Message {"from User" if i % 2 == 0 else " from you"} : {msg}\n'
        message = message + f"Message from User(last): {text}\n"
        message = message + "Based on this dialog, generate a response to last message."

    message = message + f"Generate a response to the following message ({text})" \
                        f" in the original language, using only spaces or newlines" \
                        f" if needed, do not make useless newline symbols" \
                        f" to format the text. Just send your answer!" \
                        f" Answer like you are a little girl (10 years old)"
    print(message)
    return client.models.generate_content(model="gemini-2.0-flash", contents=message).text
