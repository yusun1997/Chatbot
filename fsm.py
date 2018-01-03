from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

	def is_going_to_state1(self, update):
		text = update.message.text
		return text.lower() == 'go to state1'

	def is_going_to_state2(self, update):
		text = update.message.text
		return text.lower() == 'go to state2'

	def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'go to state3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'go to state4'

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
        self.go_back(update)

	def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

	def on_enter_state3(self, update):
        update.message.reply_text("I'm entering state3")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

	def on_enter_state4(self, update):
        update.message.reply_text("I'm entering state4")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
