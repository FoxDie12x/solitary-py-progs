import re
from datetime import date


class Horoscope:
    """Gives the astrological sign for a given date of birth"""
    __FROM = 'from'
    __TO = 'to'
    
    __astro_signs = {
    'aries': {'from': '03-20', 'to': '04-19'}, 
    'taurus': {'from': '04-19', 'to': '05-20'}, 
    'gemini': {'from': '05-20', 'to': '06-20'}, 
    'cancer': {'from': '06-20', 'to': '07-22'}, 
    'leo': {'from': '07-22', 'to': '08-22'}, 
    'virgo': {'from': '08-22', 'to': '09-22'}, 
    'libra': {'from': '09-22', 'to': '10-22'}, 
    'scorpio': {'from': '10-22', 'to': '11-21'}, 
    'sagittarius': {'from': '11-21', 'to': '12-21'}, 
    'capricorn': {'from': '12-21', 'to': '01-20'}, 
    'aquarius': {'from': '01-20', 'to': '02-19'}, 
    'pisces': {'from': '02-19', 'to': '03-20'}
    }

    
    def __init__(self, birthDate: str):
        if not self.__is_valid_birthdate(birthDate):
            raise Exception("Invalid date given!")
        self.__birthDate = birthDate
        
    
    def set_birthdate(self, birthDate: str):
        if not self.__is_valid_birthdate(birthDate):
            raise Exception("Invalid date given!")
        self.__birthDate = birthDate


    def get_birthdate(self) -> str:
        return self.__birthDate
        
        
    def get_horoscope(self) -> str:
        # Get data from user's date of birth
        p_year = re.compile(r"^[\d]{4}")
        p_month = re.compile(r"(?<=-)[\d]+(?=-)")
        p_day = re.compile(r"(?<=-)[\d]+$")
        
        year_match = p_year.search(self.__birthDate)
        month_match = p_month.search(self.__birthDate)
        day_match = p_day.search(self.__birthDate)
        

        bYear = int(year_match.group())
        bMonth = int(month_match.group())
        bDay = int(day_match.group())    
        date_birthDate = date(bYear, bMonth, bDay)
        
        
        for sign in self.__astro_signs:
            p_astro_month = re.compile(r"^[\d]{2}")
            p_astro_day = re.compile(r"[\d]{2}$")
            
            p_astro_month_start = int(p_astro_month.search(self.__astro_signs[sign][self.__FROM]).group())
            p_astro_month_end = int(p_astro_month.search(self.__astro_signs[sign][self.__TO]).group())
            p_astro_day_start = int(p_astro_day.search(self.__astro_signs[sign][self.__FROM]).group())
            p_astro_day_end = int(p_astro_day.search(self.__astro_signs[sign][self.__TO]).group())

            
            from_date = ''
            to_date = ''
            if p_astro_month_end > p_astro_month_start:
                from_date = date(bYear, p_astro_month_start, p_astro_day_start)
                to_date = date(bYear, p_astro_month_end, p_astro_day_end)
            else:
                from_date = date(bYear, p_astro_month_start, p_astro_day_start)
                to_date = date(bYear + 1, p_astro_month_end, p_astro_day_end)
                      
            horoscope = ''
            if (date_birthDate >= from_date and date_birthDate < to_date): 
                horoscope = sign            
                return horoscope
        
        
        
    def __is_valid_birthdate(self, birthDate: str) -> bool:
        """ Checks via regular expression whether the birth date is of
        format yyyy-mm-dd. 
            YYYY can not be less than 0, 
            MM must be between 1-12 (inclusive), 
            DD must be 01-31 (inclusive) """
            
        if re.search(r"^[\d]{4}", birthDate) == None or re.search(r"(?<=-)[\d]+(?=-)", birthDate) == None or re.search(r"(?<=-)[\d]+$", birthDate) == None:
            return False            
            
        return True;
