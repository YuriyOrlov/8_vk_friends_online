import vk
import getpass
import argparse
import sys
import textwrap


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)

    def check_python_version(self):
        if sys.version_info < (3, 5):
            self.print_help()
            raise SystemExit('\nSorry, this code needs Python 3.5 or higher\n')


def create_parser():
    parser = MyParser(prog='Who is Online VK?', formatter_class=argparse.RawDescriptionHelpFormatter,
                      description=textwrap.dedent('''\
                      You can check are your friends are Online in VK or not. \n
                      -----------------------------------------------------------------
                      This program had been tested on Python 3.5.2.
                      '''))
    parser.add_argument('--app_id', nargs='?',
                        help='Paste your app ID after this key,\
                              e.g --app_id 1234567)',
                        type=str, default=None)
    return parser


def get_user_login():
    return getpass.getpass(prompt='\nPlease, enter username> ', stream=None)


def get_user_password():
    return getpass.getpass(prompt='\nPlease, enter password> ', stream=None)


def get_online_friends(login, password, APP_ID):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )

    api = vk.API(session)
    overall_friends_list = api.friends.get(fields='first_name, last_name, domain', name_case='nom')
    return [friend_online for friend_online in overall_friends_list if friend_online['online'] is 1]


def output_friends_to_console(friends_online):
    print('\nNumber of friends online - {}\n'.format(len(friends_online)))
    for friend in friends_online:
        print('{} {}, account name: {}\n'.format(friend['first_name'],
                                                 friend['last_name'],
                                                 friend['domain']))


if __name__ == '__main__':
    parser = create_parser()
    parser.check_python_version()
    args = parser.parse_args()
    APP_ID = args.app_id if args.app_id else None
    if APP_ID:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password, APP_ID)
        output_friends_to_console(friends_online)
    else:
        sys.stderr.write('Error: {}\n'.format('Enter your application ID'))
