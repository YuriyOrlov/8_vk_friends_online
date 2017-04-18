import vk
import getpass
from args_parser import TerminalArgumentsParser


def get_user_password():
    return getpass.getpass(prompt='\nPlease, enter password> ', stream=None)


def get_online_friends(login, password, app_id):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )

    api = vk.API(session)
    return api.users.get(user_ids=api.friends.getOnline(), fields='first_name, last_name', name_case='nom')


def output_friends_to_console(friends_online):
    print('\nNumber of friends online - {}\n'.format(len(friends_online)))
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'],
                             friend['last_name']))


if __name__ == '__main__':
    parser = TerminalArgumentsParser()
    args = parser.parse_args()
    app_id = args.app_id
    login = args.login
    password = get_user_password()
    friends_online = get_online_friends(login, password, app_id)
    output_friends_to_console(friends_online)
