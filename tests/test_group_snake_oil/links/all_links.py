HOME_PAGE_URL = 'https://openweathermap.org/'
GUIDE_PAGE_URL = 'https://openweathermap.org/guide'
DASHBOARD_PAGE_URL = 'https://openweathermap.org/weather-dashboard'
FAQ_URL = 'https://openweathermap.org/faq'

# URLs of all pages placed at header
ALL_PAGES_URLs = ['https://openweathermap.org/',
                  'https://openweathermap.org/guide',
                  'https://openweathermap.org/api',
                  'https://openweathermap.org/weather-dashboard',
                  'https://openweathermap.org/price',
                  'https://openweathermap.org/our-initiatives',
                  'https://openweathermap.org/examples',
                  'https://home.openweathermap.org/users/sign_in',
                  'https://openweathermap.org/faq',
                  'https://openweathermap.org/appid',
                  'https://home.openweathermap.org/questions']

# Dashboard 'How to Start' block
# The list of URLs where user expected to be redirected to, when user is signed in
EXPEXTED_URLS_SIGNED_IN_LIST = \
    ['https://home.openweathermap.org/', 'https://home.openweathermap.org/',
     'https://home.openweathermap.org/dashboard/events?campaign_id=weather_dashboard_website',
     'https://home.openweathermap.org/dashboard/events?campaign_id=weather_dashboard_website',
     'https://home.openweathermap.org/dashboard/triggers/create?campaign_id=weather_dashboard_website',
     'https://openweathermap.org/weather-dashboard/dashboard-documentation#setup',
     'https://openweathermap.org/weather-dashboard/dashboard-documentation',
     'https://home.openweathermap.org/dashboard/events?campaign_id=weather_dashboard_website']

# The list of URLs where user expected to be redirected to, when user is NOT signed in
EXPECTED_URLS_SIGNED_OUT_LIST = \
    ['https://home.openweathermap.org/users/sign_up?campaign_id=weather_dashboard_website',
     'https://home.openweathermap.org/users/sign_in?campaign_id=weather_dashboard_website',
     'https://home.openweathermap.org/users/sign_in',
     'https://home.openweathermap.org/users/sign_in',
     'https://home.openweathermap.org/users/sign_in',
     'https://openweathermap.org/weather-dashboard/dashboard-documentation#setup',
     'https://openweathermap.org/weather-dashboard/dashboard-documentation',
     'https://home.openweathermap.org/users/sign_in']


class StudentInitiativePageLinks:
    STUDENT_INITIATIVE_PAGE_URL = "https://openweathermap.org/our-initiatives/student-initiative"
    PRICING_PAGE_URL_FOR_DEVELOPER_PLAN = "https://openweathermap.org/price"
    PRICING_PAGE_URL_FOR_MEDIUM_PLAN = "https://openweathermap.org/price#history"
