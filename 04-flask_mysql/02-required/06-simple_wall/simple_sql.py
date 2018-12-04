from mysqlconnection import connectToMySQL

SCHEMA = ("simple_wall")

def get_msg(user_id):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT users.first_name, users.last_name, messages.id, messages.created_at, messages.content FROM users JOIN messages ON messages.from_id = users.id WHERE messages.user_id = %(user_id)s;"
    data = {
        "user_id" : user_id
    }
    messages = mysql.query_db(query, data)
    return messages

def get_msg_ownership(id, msg_id):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT user_id FROM messages WHERE id = %(msg_id)s;"
    data = {
        "msg_id" : msg_id
    }
    owner = mysql.query_db(query, data)
    # print(owner)
    # print(user_id)
    # print(owner[0]['from_id'])
    print (id == int(owner[0]['user_id']))
    if (id == int(owner[0]['user_id'])):
        return True
    else:
        return False    
    

def get_others(exclude):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT first_name, last_name, id FROM users WHERE id != %(exclude_id)s;"
    data = {
        "exclude_id" : exclude
    }
    user_list = mysql.query_db(query, data)
    
    return user_list 

def get_total_msg(user_id):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT * FROM messages WHERE user_id = %(user_id)s;"
    data = {
        "user_id" : user_id
    }
    total_msg = mysql.query_db(query, data)
    print(len(total_msg))
    return len(total_msg)

def get_sent(user):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT id FROM messages WHERE from_id = %(from_id)s;"
    data = {
        "from_id" : user
    }
    num_sent = mysql.query_db(query, data)
    
    return(len(num_sent))

def remove_msg(id):
    mysql = connectToMySQL(SCHEMA)
    query = "DELETE FROM messages WHERE id = %(id)s;"
    data = {
        "id" : id
    }
    mysql.query_db(query, data)

def send_msg(user_id, from_id, content):
    mysql = connectToMySQL(SCHEMA)
    query = "INSERT INTO messages (user_id, from_id, content, created_at, updated_at) VALUES (%(user_id)s, %(from_id)s, %(content)s, NOW(), NOW());"
    data = {
        "user_id" : user_id,
        "from_id" : from_id,
        "content" : content
    }
    mysql.query_db(query,data)
