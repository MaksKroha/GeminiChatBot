from gemini import client


def short_text(text, symbols):
    return client.models.generate_content(model="gemini-2.0-flash",
                                          contents=f"Make this text shorter,"
                                                   f" up to {symbols} symbols,"
                                                   f" with context saving in the original"
                                                   f" language in which it is published - '{text}',"
                                                   f" just send shortened text!").text
