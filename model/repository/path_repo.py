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

    def check_user_id(self, user):
        user = User.query.filter_by(username=user).first()
        user_id = user.id
        return user_id

    def existing_api(self, apin, user_id):
        api = Api.query.filter_by(api_name=apin).first()
        if api is None:
            return False
        elif api.api_name == apin and api.user_id == user_id:
            return True
        else:
            return False
