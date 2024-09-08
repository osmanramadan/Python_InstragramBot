import requests # type: ignore



# Instagram login function
def login_instagram(session, username, password):
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    csrf_token = get_csrf_token(session)

    headers = {
        'X-CSRFToken': csrf_token,
        'Referer': 'https://www.instagram.com/accounts/login/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    login_payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    response = session.post(login_url, data=login_payload, headers=headers)
    if response.status_code == 200 and response.json().get('authenticated'):
        print('Instagram login successful!')
        return True
    else:
        print(f'Instagram login failed: {response.text}')
        return False

# Get CSRF token
def get_csrf_token(session):
    try:
        response = session.get("https://www.instagram.com/")
        return response.cookies.get('csrftoken', '')
    except Exception as e:
        print(f"Error retrieving CSRF token: {e}")
        return ''


# Access Facebook Business (simplified)
def access_facebook_business(session):
    business_url = "https://business.facebook.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = session.get(business_url, headers=headers)
    if response.status_code == 200:
        print('Access to Facebook Business successful!')

        # print(response.text)
    else:
        print(f'Access to Facebook Business failed:?')

# Main execution
if __name__ == "__main__":
    session = requests.Session()
    
    # Replace with your Instagram credentials
    instagram_username = ''
    instagram_password = ''


    # Perform Instagram login
    if login_instagram(session, instagram_username, instagram_password):
        # Perform access to Facebook Business
        access_facebook_business(session)
