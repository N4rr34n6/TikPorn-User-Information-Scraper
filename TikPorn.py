import requests
import re
import os
import argparse
import html

def get_user_info(identifier):
    # Remove the '@' symbol if present
    identifier = identifier.lstrip('@')
    url = f"https://tik.porn/{identifier}"

    # Set headers to mimic a web browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Make a GET request to the user's profile page
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        
        # Define regex patterns for extracting user information
        patterns = {
            'nickname': r'<h2 class="ProfileHeader_title__K80CD">(.*?)</h2>',
            'title': r'<h1 class="Breadcrumbs_name__Pac93"><span>(.*?)</span>',
            'profile_pic': r'<div class="ProfileHeader_image__9EwAC.*?src="(.*?)"',
            'videos': r'<div class="ProfileHeader_statsColumn__u4djy"><div>(\d+(\.\d+)?(?:k)?)</div><div>Videos</div></div>',
            'likes': r'<div class="ProfileHeader_statsColumn__u4djy"><div>(\d+(\.\d+)?(?:k)?)</div><div>Likes</div></div>',
            'views': r'<div class="ProfileHeader_statsColumn__u4djy"><div>(\d+(\.\d+)?(?:k)?)</div><div>Views</div></div>',
            'followers': r'<div class="ProfileHeader_statsColumn__u4djy"><div>(\d+(\.\d+)?(?:k)?)</div><div>Followers</div></div>',
            'bio': r'<p><span class="ProfileHeader_biography__TnM8t">(.*?)</span></p>',  # Flexible to capture any content
            'verified': r'<svg xmlns="http://www.w3.org/2000/svg".*?class="Breadcrumbs_verifiedBadge__hHgv4">'
        }

        info = {}
        for key, pattern in patterns.items():
            # Search for each pattern in the HTML content
            match = re.search(pattern, html_content, re.DOTALL)  # re.DOTALL allows matching across new lines
            if match and len(match.groups()) > 0:
                info[key] = html.unescape(match.group(1)).strip()  # Decode HTML entities and strip whitespace
            else:
                info[key] = f"No {key} found"  # Fallback message if not found

        # Check if the account is verified
        info['verified'] = 'Yes' if re.search(patterns['verified'], html_content) else 'No'

        return info  # Return the collected user info

    else:
        return None  # Return None if the page could not be accessed

def download_profile_pic(profile_pic_url, nickname):
    # Download the user's profile picture if a valid URL is provided
    if profile_pic_url and profile_pic_url.startswith('http'):
        response = requests.get(profile_pic_url)
        if response.status_code == 200:
            profile_pic_path = f"{nickname}_profile_pic.jpg"
            with open(profile_pic_path, "wb") as f:
                f.write(response.content)  # Write the image content to a file
            print(f"Profile picture downloaded: {profile_pic_path}")
        else:
            print("Could not download the profile picture.")
    else:
        print("No valid profile picture found.")

def format_user_info(info):
    # Format the user info into a readable string
    return (
        f"**Nickname:** {info['nickname']}\n"
        f"**Title:** {info['title']}\n"
        f"**Verified:** {info['verified']}\n"
        f"**Videos:** {info['videos']}\n"
        f"**Likes:** {info['likes']}\n"
        f"**Views:** {info['views']}\n"
        f"**Followers:** {info['followers']}\n"
        f"**Bio:** {info['bio']}\n"
        f"**Profile Pic:** {info['profile_pic']}"
    )

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Get TikPorn user information.')
    parser.add_argument('username', type=str, help='TikPorn username (without @)')
    args = parser.parse_args()

    user_info = get_user_info(args.username)

    if user_info:
        print(f"User information for {args.username}:")
        print(format_user_info(user_info))  # Print the formatted user info
        download_profile_pic(user_info['profile_pic'], user_info['nickname'])  # Download the profile picture
    else:
        print(f"No information found for user {args.username}.")

if __name__ == "__main__":
    main()  # Execute the main function
