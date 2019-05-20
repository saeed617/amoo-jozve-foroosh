import random
import string


UNUSABLE = []


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_username_generator(instance, new_username=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_username is not None:
        username = new_username
    else:
        username = random_string_generator(size=8)

    if username in UNUSABLE:
        new_username = "{username}-{randstr}".format(
            username=username,
            randstr=random_string_generator(size=2)
        )
        return unique_username_generator(instance, new_username=new_username)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(username=username).exists()
    if qs_exists:
        new_username = "{username}_{randstr}".format(
                    username=username,
                    randstr=random_string_generator(size=2)
                )
        return unique_username_generator(instance, new_username=new_username)

    return username
