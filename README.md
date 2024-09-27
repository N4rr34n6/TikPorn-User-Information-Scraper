# TikPorn User Information Scraper

This Python script allows you to retrieve user information from [TikPorn](https://tik.porn) by providing a username. It extracts details such as nickname, bio, number of videos, likes, views, followers, and whether the user is verified. The script also downloads the user's profile picture if available.

## Features

- Extracts the following user information from TikPorn:
  - **Nickname**
  - **Title**
  - **Verified Status**
  - **Number of Videos**
  - **Likes**
  - **Views**
  - **Followers**
  - **Bio**
- Downloads the user's profile picture.
- Formats and displays the extracted information in a readable format.

## Requirements

- Python 3.x
- Required Libraries:
  - `requests`
  - `re`
  - `argparse`
  - `html`

To install the required libraries, you can use:

```bash
pip3 install requests
```

## Usage

To use the script, run it from the command line and pass the TikPorn username (without `@`) as an argument.

```bash
python3 TikPorn.py <username>
```

## Functions

### `get_user_info(identifier)`

- Scrapes and returns the following user information:
  - Nickname
  - Title
  - Profile picture URL
  - Number of videos, likes, views, followers
  - Bio
  - Verified status

### `download_profile_pic(profile_pic_url, nickname)`

- Downloads the profile picture to the current directory, using the nickname as part of the filename.

### `format_user_info(info)`

- Formats the user information into a readable string for console output.

## Error Handling

If the username is invalid or the user is not found, the script will return:
- "No information found for user `<username>`."

If the profile picture cannot be downloaded, it will return:
- "Could not download the profile picture."

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes!

## Disclaimer

This script is for educational purposes only. Please ensure you comply with TikPorn's terms of service and policies.
