from datetime import datetime


def calculate_fine(issue_date):

    today = datetime.today().date()


    issued = datetime.strptime(
        issue_date,
        "%Y-%m-%d"
    ).date()


    days = (today - issued).days


    allowed_days = 7

    fine_per_day = 5


    if days > allowed_days:

        late_days = days - allowed_days

        return late_days * fine_per_day


    return 0