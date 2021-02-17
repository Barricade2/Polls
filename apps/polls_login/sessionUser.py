
class User():

    def __init__(self, request):
        self.session = request.session
        user = self.session.get('skey')
        if 'skey' not in request.session:
            user = self.session['skey'] = {}
        self.user = user

    def add(self, product, qty):
        """
        Adding and updating the users session data
        """
        user_id = str(user.id)

        if user_id in self.user:
            self.user[user_id]['qty'] = qty
        else:
            self.user[user_id] = {'id': str(user.id)}

        self.save()

# TODO: refactor something!
