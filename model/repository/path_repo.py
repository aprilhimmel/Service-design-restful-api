from model.models.apis import Api
from model.models.user import User


class PathRepo:
    def existing_user(self, usernam):
        user = User.query.filter_by(username=usernam).first()
        if user is None:
            return False
        elif user.username == usernam:
            return True
        else:
            return False
