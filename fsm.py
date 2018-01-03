from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'hi'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'i want to play a game'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'you idiot'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'bye'

    def is_going_to_statedefault(self, update):
        return True

    def on_enter_statedefault(self, update):
        update.message.reply_text("-Hi \n -I want to play a geme \n -you idiot \n -bye ")
        self.go_back(update)

    def on_exit_statedefault(self, update):
        print('Leaving state default')

    def on_enter_state1(self, update):
        update.message.reply_text("Hi")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("But I don't want to")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("fuck you")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("Bye~")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
