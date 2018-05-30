import django
import os
import random
import string


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()


if __name__ == "__main__":
    from conf.models import Statistics

    chars = string.ascii_uppercase + string.digits
    string = ''.join(random.choice(chars) for _ in range(random.randint(1, 10)))
    q = Statistics(sig=random.randint(0, 1000), col=random.uniform(0, 1000), rest=string)
    q.save()

    printed = ''
    for row in Statistics.objects.all():
        printed += "%s %s %s %s %s\n" % (row.pk, row.sig, row.col, row.rest, row.datetime_send)

    print(printed)

    with open('save.txt', 'w') as f:
        f.write(printed)
