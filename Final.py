# DZ 5 - 1:  В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import logging
from sys import argv

__all__ = ['check_date']

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def if_leap(year: int) -> bool:
    """Проверка, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def check_date(str_date: str) -> bool:
    """Проверка, является ли дата валидной."""
    try:
        day, mon, year = map(int, str_date.split('.'))
    except ValueError:
        logger.error(f"Неверный формат даты: {str_date}")
        return False

    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999):
        logger.error(f"Неверные значения даты: {str_date}")
        return False

    if mon in (4, 6, 9, 11) and day > 30:
        logger.error(f"Неверное количество дней для месяца {mon}: {str_date}")
        return False

    if mon == 2:
        if if_leap(year) and day > 29:
            logger.error(f"Неверное количество дней для февраля в високосном году: {str_date}")
            return False
        if not if_leap(year) and day > 28:
            logger.error(f"Неверное количество дней для февраля в невисокосном году: {str_date}")
            return False

    logger.info(f"Дата {str_date} является валидной.")
    return True

if __name__ == '__main__':
    if len(argv) < 2:
        logger.error("Не передана дата для проверки.")
    else:
        date_to_check = argv[1]
        logger.info(f"Проверка даты: {date_to_check}")
        print(check_date(date_to_check))

# Теперь код можно запускать из командной строки, передавая дату в качестве параметра: python script.py "31.02.2020"