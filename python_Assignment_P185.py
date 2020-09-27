class GI:
    name = "Input name"
    rank = "Input rank "
    serial_number = 0
    company = "Input company "

class Infantry(GI):
    obstacle_course_time = "hh:mm:ss"
    sentry_duty = "YYYY:MM:DD hh:mm:ss"


class Officer(GI):
    company_readiness_ranking = 0
    company_budget_deficit = "${:,.2f}".format()
    
    
    
