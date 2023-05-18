import cmd 

class MyCmd(cmd.Cmd):
    prompt = "kc0des >> "  #the prompt attribute represents the command prompt string that is displayed to the user in a command-line interpreter.
    doc_header = "MyCmd - Custom Command-Line Interpreter" # It represents the header text that is displayed at the top of the help documentation for the command-line interpreter.
    undoc_header = "Undocumented Commands:"
    ruler = "="  # Custom ruler character in the help documentation
    #identchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Only uppercase letters are valid identifiers
    #use_rawinput = False """The use_rawinput attribute is a built-in attribute of the cmd.Cmd class in Python. It determines whether the cmd.Cmd instance should use the raw_input() function (or its equivalent) to read user input or the sys.stdin.readline() function."""


    def do_authors(self, line):
        print("Kayc0des is the author of MyCmd")

    def do_hello(self, line):
        print("Hello, world!")
        print("Last command:", self.lastcmd)
    
    def do_quit(self, line):
        return True  # Exiting the command loop
    
    """The emptyline() method is called when the user enters an empty 
    line (i.e., just presses the Enter key) in the command-line interface."""
    def emptyline(self):
        print("Please enter a command or 'help' for assistance ") 


    """The default(line) method is called when the entered command does not
    match any of the defined command methods (i.e., methods starting with do_)."""
    def default(self, line):
        print(f"Command '{line}' not recognized. Type 'help' for a list of available commands.")
    

    """ It is called when tab completion is requested for an unrecognized or incomplete command."""
    def completedefault(self, text, line, begidx, endidx):
        commands = ['authors', 'hello', 'help', 'quit']
        matches = [command for command in commands if command.startswith(text)]
        return matches
    

    """It is called before each command is executed in the command-line interpreter."""
    def precmd(self, line):
        modified_line = line.lower()  # Convert the command to lowercase
        return modified_line
    
    
    """It is called after each command is executed in the command-line interpreter."""
    def postcmd(self, stop, line):
        if line == 'quit':
            print("Exiting the command loop. Goodbye!")
        return stop

    
    """It is called once before the command loop starts in a command-line interpreter."""
    def preloop(self):
        print("Welcome to MyCmd! Starting the command loop.")

    """ It is called once after the command loop finishes in a command-line interpreter."""
    def postloop(self):
        print("Exiting MyCmd. Goodbye!")


    """cmdqueue"""
    def do_execute(self, line):
        print("Executing:", line)

    def do_enqueue(self, line):
        self.cmdqueue.append(line)
        print("Enqueued command:", line)

if __name__ == '__main__': # the if __name__ == '__main__': construct is used to ensure that the code block underneath it is only executed if the script is being run directly and not being imported as a module.
    my_cmd = MyCmd()
    #my_cmd.intro = "Welcome to MyCmd! Enter 'hello' to greet or 'quit' to exit."
    #my_cmd.onecmd("hello")
    my_cmd.cmdloop(intro="Welcome to MyCmd! Enter 'hello' to greet or 'quit' to exit.")  # Start the command loop