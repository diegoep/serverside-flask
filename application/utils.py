from flask import abort
import pymysql
from config import MYSQL

def find_or_404(model, id, code=404):
    result = model.query.get(id)
    if not result:
        abort(code)
    return result

def select_one_db(query):
    """ Connect to Mysql database """
    MYSQL_STR = 'user=%(user)s password=%(pw)s dbname=%(db)s host=%(host)s port=%(port)s' % MYSQL
    conn = pymysql.connect(MYSQL_STR)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        rows = cursor.fetchone()

    finally:
        cursor.close()
        conn.close()
    return rows

def select_all_db(query):
    """ Connect to Mysql database """
    MYSQL_STR = 'user=%(user)s password=%(pw)s dbname=%(db)s host=%(host)s port=%(port)s' % MYSQL
    conn = pymysql.connect(MYSQL_STR)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        rows = cursor.fetchall()

    finally:
        cursor.close()
        conn.close()
    return rows

def delete_from_db(query):
    """ Connect to Mysql database """
    MYSQL_STR = 'user=%(user)s password=%(pw)s dbname=%(db)s host=%(host)s port=%(port)s' % MYSQL
    conn = pymysql.connect(MYSQL_STR)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        conn.commit()
        return True
    except:
        return False

    finally:
        cursor.close()
        conn.close()

def list_of_first(mylist):
  return [ seq[0] for seq in mylist ]

def create_dictionary(values, keys):
  dictionary = {}
  for i in range(len(values)):
    dictionary[keys[i]] = values[i]
  return dictionary

def create_dictionary_list(values, keys):
    response = []
    for row in values:
        dictionary = {}
        for index in range(0,len(keys)):
            dictionary[keys[index]] = row[index]
        response.append(dictionary)
    return response

def get_group_codes(groupstrlist):
    codes = []
    tree = hierarquia(groupstrlist)
    for k0, v0 in tree.items():
        codes.append(abs(hash(k0)) % (10 ** 8))
        for k1, v1 in v0.items():
            codes.append(abs(hash(k0 + k1)) % (10 ** 8))
    return codes

def hierarquia(strtreelist):
    tree = {}
    for item in strtreelist:
        itemarr = item.split("/")
        if itemarr[0] not in tree:
            tree[itemarr[0]] = {}
        tree[itemarr[0]].update(hierarquia(itemarr[1:]))
    return tree