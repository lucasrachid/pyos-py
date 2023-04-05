from time import sleep

class execute_class:

    def placeholder_function(self):
        self.terminal.app_print('\nEncerrando processos em...')
        self.terminal.app_print('\n5...')
        sleep(1)
        self.terminal.app_print('\n4...')
        sleep(1)
        self.terminal.app_print('\n3...')
        sleep(1)
        self.terminal.app_print('\n2...')
        sleep(1)
        self.terminal.app_print('\n1...')
        sleep(1)
        self.terminal.app_print('\nEncerrando terminal...')
        self.terminal.end()
        self.cpu.cpu_alive = False
        pass
