from datetime import datetime, timezone
from django.contrib.sessions.models import Session


def clean_session():
    all_session = Session.objects.all()
    now = datetime.now(timezone.utc)
    for i in all_session:
        if (now - i.expire_date).total_seconds() > 172800:
            i.delete()





