"""
# references
https://sourcemaking.com/design_patterns/command
"""
import abc
import os

# Invoker
class Invoker:

    def __init__(self):
        self._commands = []


    def store_command(self, command):
        self._commands.append(command)

    def exceute_commands(self):
        for command in self._commands:
            command.execute()

    def undo_commands(self):
        for command in reversed(self._commands):
            command.undo()

# Abstract Command
class AbstractCommand(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        """"""


#Concrete Command
class MoveFileCommand(AbstractCommand):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src, self.dest)


    def undo(self):
        self.rename(self.dest, self.src)

    def rename(self, src, dest):
        print('mv {} {}'.format(src, dest))
        os.rename(src, dest)


# Receiver
# class Receiver:

#     def action(self):
#         pass



def main():
    invoker = Invoker()
    invoker.store_command(MoveFileCommand('foo', 'bar'))
    invoker.store_command(MoveFileCommand('bar', 'bars'))
    print(invoker._commands)
    with open('foo', 'w') as f:
        f.write('hello')

    invoker.exceute_commands()
    invoker.undo_commands()

if __name__ == '__main__':
    main()