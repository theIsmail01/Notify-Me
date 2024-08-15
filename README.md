# GitHub Job Scraper

This is a Python script that scrapes job postings from a GitHub repository and sends an email notification for new postings. The script is deployed on an Amazon EC2 instance and runs continuously, checking for new job postings every 5 minutes.

## Features

- Scrapes job postings from a GitHub repository
- Sends an email notification for new job postings
- Uses environment variables for sensitive information
- Deployed on an Amazon EC2 instance

## Dependencies

- Python 3
- BeautifulSoup
- requests
- smtplib
- python-dotenv

## Setup

1. Clone this repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Install the dependencies:

```bash
pip install python-dotenv beautifulsoup4 requests smtplib
```

3. Create a .env file in the root directory of the project, and add your email credentials and the email addresses you want to send to and receive from:

```bash
FROM_ADDR=your-email@example.com
TO_ADDR=receiver-email@example.com
USERNAME=your-email@example.com
EMAIL_PASSWORD=your-email-password
```

4. Deployment

The script is deployed on an Amazon EC2 instance. It runs continuously, checking for new job postings every 5 minutes.

## Usage

### Run the Script
```bash
python webscrapper.py
```
The script will initially load the current job postings, send a test email, and then start checking for new job postings every 5 minutes.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
