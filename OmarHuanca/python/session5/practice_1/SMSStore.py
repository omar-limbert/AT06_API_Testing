from OmarHuanca.SingletonLogger import SingletonLogger


class SMSStore:
    def __init__(self):
        self.inbox = []
        self.messages_unread_index = 0
        self.logger = SingletonLogger.__call__().get_logger()

    def __str__(self):
        rows = []
        print("Inbox [ {} ] Total message(s)".format(self.message_count()))
        for sms in self.inbox:
            rows.append(self.view_sms(sms))
        print("Inbox [ {} ] New message(s)".format(self.get_unread_indexes()))
        return '\n'.join(rows)

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        sms_tuple = (False, from_number, time_arrived, text_of_sms)
        self.inbox.append(sms_tuple)

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        return self.messages_unread_index

    def view_sms(self, sms):
        has_been_read, from_number, time_arrived, text_of_sms = sms
        if not has_been_read:
            new_message_flag = "*"
            self.messages_unread_index += 1
        else:
            new_message_flag = " "
        return " | ".join([new_message_flag, from_number, time_arrived, text_of_sms])


if __name__ == "__main__":
    script = SMSStore()
    script.add_new_arrival("12345678", "8:55", "Hello")
    script.add_new_arrival("87654321", "2:55", "Bye")
    script.add_new_arrival("12312345", "4:55", "How are you?")
    script.add_new_arrival("45645678", "6:55", "How is it doing?")
    print(script)
