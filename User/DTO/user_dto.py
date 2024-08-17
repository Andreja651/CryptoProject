class UserDTO:
    def __init__(self, user_id, username, email, created_at):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_at = created_at

    @staticmethod
    def from_model(user):
        return UserDTO(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
        )

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
