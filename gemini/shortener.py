from gemini import client
from exception import log_exception


# Shortens the provided text to a specified number
# of symbols while preserving its context and
# original language. Uses the Gemini API to
# generate the shortened text. If an error occurs
# during the process, it logs the exception and
# returns an error message. The optional
# clarification parameter allows additional
# instructions for the text shortening process.
def short_text(text, symbols, clarification=""):
    try:
        return client.models.generate_content(model="gemini-2.0-flash",
                                              contents=f"Make this text shorter,"
                                                       f" up to {symbols} symbols,"
                                                       f" with context saving in the original"
                                                       f" language in which it is published - '{text}',"
                                                       f" just send shortened text!" + clarification).text
    except Exception as e:
        log_exception(str(e))
        return "Error has occurred, please try again later."
