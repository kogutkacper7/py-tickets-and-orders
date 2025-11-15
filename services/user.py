from django.contrib.auth import get_user_model


User = get_user_model()


def create_user(username: str,
                password: str,
                email: str = None,
                first_name: str = None,
                last_name: str = None
                ) -> User:

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email or "",
        first_name=first_name or "",
        last_name=last_name or "",
    )
    return user


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)


def update_user(user_id: int,
                password: str = None,
                **user_data
                ) -> None:
    user = get_user(user_id)

    for field in ["first_name", "last_name", "email"]:
        if field not in user_data or user_data[field] is None:
            user_data[field] = ""

    if password:
        user.set_password(password)

    for field, value in user_data.items():
        setattr(user, field, value)

    user.save()
