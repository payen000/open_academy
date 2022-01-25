import logging
import xmlrpc.client


def get_sessions(models, database, uid, password):
    ids = models.execute_kw(database, uid, password, 'session', 'search', [[[1, '=', 1]]])
    sessions = models.execute_kw(
        database, uid, password, 'session', 'read',
        [ids], {'fields': ['name', 'number_of_seats', ]}
    )

    return sessions


def main():
    logging.basicConfig(filename='session.log', filemode='w', level=logging.INFO)
    host = 'localhost'
    port = 8069
    database = 'odoo_test'
    user = 'payen'
    password = 'payen'
    url = 'http://%s:%d/xmlrpc/' % (host, port)

    uid = xmlrpc.client.ServerProxy(url + 'common').login(database, user, password)
    models = xmlrpc.client.ServerProxy('{}2/object'.format(url))

    models.execute_kw(
        database, uid, password, 'session', 'create',
        [{
            'name': 'Session xmlrpc',
            'start_date': '2022-01-24',
            'stop_date': '2022-01-29',
            'active': 'TRUE',
            'duration': 7.5,
            'number_of_seats': 30,
            'course_id': 1,
        }])

    sessions = get_sessions(models, database, uid, password)

    for session in sessions:
        msg = '{} ------ seats: {}'.format(session["name"], session['number_of_seats'])
        logging.info(msg)


if __name__ == '__main__':
    main()
