import os
import curses
import pycfg
from pyarch import load_binary_into_memory
from pyarch import cpu_t
from time import sleep
from process_executor import process_executor as ProcessExecutor

class os_t:
	def __init__ (self, cpu, memory, terminal):
		self.cpu = cpu
		self.memory = memory
		self.terminal = terminal

		self.terminal.enable_curses()

		self.console_str = ""
		self.terminal.console_print("this is the console, type the commands here\n")

	def printk(self, msg):
		self.terminal.kernel_print("kernel: " + msg + "\n")

	def panic (self, msg):
		self.terminal.end()
		self.terminal.dprint("kernel panic: " + msg)
		self.cpu.cpu_alive = False

	def interrupt_keyboard (self):
		key = self.terminal.get_key_buffer()
		
		if ((key >= ord('a')) and (key <= ord('z'))) \
		or ((key >= ord('A')) and (key <= ord('Z'))) \
		or ((key >= ord('0')) and (key <= ord('9'))) \
		or (key == ord(' ')) or (key == ord('-')) \
		or (key == ord('_')) or (key == ord('.')):
			strchar = chr(key)
			self.console_str += strchar
			self.terminal.console_print(strchar)
		elif key == curses.KEY_BACKSPACE:
			self.console_str = self.console_str[:-1]
			self.terminal.console_print('\r')
			self.terminal.console_print(self.console_str)
			return
		elif (key == curses.KEY_ENTER) or (key == ord('\n')):
			self.execute_command(self.console_str)
			return

	def handle_interrupt (self, interrupt):
		if interrupt == pycfg.INTERRUPT_KEYBOARD:
			self.interrupt_keyboard()
		return

	def syscall (self):
		# self.terminal.app_print(msg)
		return
	
	def execute_command(self, command):	
		if command == 'sudo rachid install':
			self.install_something()
		elif command == 'sudo apt update':
			self.update_package()
		elif command == 'clear':
			self.clear_console()
		elif command == 'close terminal':
			self.close_terminal()
		elif command == 'start process':
			process_executor = ProcessExecutor()
			process_executor.do_process('execute_class.py', 'placeholder_function')
		else:
			self.terminal.app_print('\nComando nao existe!')
			sleep(2)
			self.clear_console()
		return
	
	def install_something(self):
		self.terminal.app_print('\nInstalando pacote...')
		sleep(1)
		self.terminal.app_print('\nBaixando dependencias...')
		sleep(1)
		self.terminal.app_print('\nPacote instalado com sucesso!')
		self.clear_console()
		return

	def update_package(self):
		self.terminal.app_print('\nAtualizando pacotes...')
		sleep(1)
		self.terminal.app_print('\nBaixando dependencias...')
		sleep(1)
		self.terminal.app_print('\nPacotes atualizados com sucesso!')
		self.clear_console()
		return
	
	def clear_console(self):
		self.console_str = ''
		self.terminal.console_print('\r')
		return
	
	def close_terminal(self):
		self.terminal.app_print('\nEncerrando processos...')
		sleep(1)
		self.terminal.app_print('\nProcessos encerrados...')
		sleep(1)
		self.clear_console()
		self.terminal.end()
		self.cpu.cpu_alive = False
		return