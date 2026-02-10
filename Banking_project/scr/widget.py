from scr.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_date):
    date_base = input_date.split()
    names_date = ' '.join(date_base[:-1])
    numbers_date = date_base[-1]
    if 'Счет' in names_date:
        mask_ = get_mask_account(numbers_date)
    else:
        mask_ = get_mask_card_number(numbers_date)
    return names_date+ ' ' + mask_

def get_date(date):
    worker_date = date.split('T')
    year, month, day = worker_date[0].split('-')
    return f'{day}.{month}.{year}'


