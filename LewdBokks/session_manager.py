

class UserSessionManager:
    user_session = {'user_id':[]}

    @staticmethod
    def add_user(userid):
        return user_session['user_id'].append(userid)

    @staticmethod
    def remove_user(userid):
        return user_session['user_id'].remove(userid)
    
    @staticmethod
    def check_if_present(userid):
        if user_session['user_id'].index(userid)