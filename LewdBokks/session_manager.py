

user_session = {'user_id':[]}

    
def add_user(userid):
    return user_session['user_id'].append(userid)

    
def remove_user(userid):
    return user_session['user_id'].remove(userid)
    
    
def check_if_present(userid):
    if user_session['user_id'].index(userid)