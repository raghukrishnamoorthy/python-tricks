name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert'
}

def greeting(user_id):
    return 'Hi %s!' % name_for_userid.get(user_id, 'Stranger')

print(greeting(457))