import argparse
import textwrap


class TerminalArgumentsParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(TerminalArgumentsParser, self).__init__(*args, **kwargs)
        self.prog = 'Who is Online VK?'
        self.formatter_class = argparse.RawDescriptionHelpFormatter
        self.description = textwrap.dedent('''\
                      You can check are your friends are Online in VK or not. \n
                      -----------------------------------------------------------------
                      This program had been tested on Python 3.5.2.
                      ''')
        self.add_argument('--app_id', nargs='?',
                          help='Paste your app ID after this key,\
                              e.g --app_id 1234567)',
                          type=int, default=None, required=True)
        self.add_argument('--login', nargs='?',
                          help='Enter your login name,\
                              e.g --login vasya)',
                          type=str, default=None, required=True)
