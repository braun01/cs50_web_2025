from dateutil.relativedelta import relativedelta

def calc_age(end, start):
    return relativedelta(end, start).years