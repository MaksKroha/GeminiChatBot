class User:
    def __init__(self):
        self.current_chat = None
        self.history = []
        self.chat_id = None
        self.username = None

    def get_username(self):
        return self.username

    def get_current_chat(self):
        return self.current_chat

    def get_current_chat_name(self):
        return self.current_chat["dialog"]

    def get_current_chat_dialog(self):
        return self.current_chat["dialog"]

    def get_current_chat_modified(self):
        return self.current_chat["modified"]

    def get_history(self):
        return self.history

    def get_chat_id(self):
        return self.chat_id

    def set_username(self, username):
        self.username = username

    def set_current_chat_name(self, chat_name):
        self.current_chat["name"] = chat_name

    def set_current_chat_dialog(self, dialog):
        self.current_chat["dialog"] = dialog

    def set_current_chat_modified(self, modified):
        self.current_chat["modified"] = modified

    def set_current_chat(self, current_chat):
        self.current_chat = current_chat

    def set_history(self, history):
        self.history = history

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id