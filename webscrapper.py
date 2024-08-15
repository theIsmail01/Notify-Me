import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

load_dotenv()


subject = "Hello"
message = "This is a test email sent from Python."
from_addr = os.getenv("FROM_ADDR")
to_addr = os.getenv("TO_ADDR")
smtp_server = "smtp.office365.com"
smtp_port = 587
username = os.getenv("USERNAME")
password = os.getenv("EMAIL_PASSWORD")


def scrape_github_repos():
    try:
        url = f"https://github.com/SimplifyJobs/New-Grad-Positions"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        repos = soup.find_all("markdown-accessiblity-table")[0].find_all("tbody")[0].find_all("tr")

        
        new_repos = [repo for repo in repos if repo not in seen_already]

        if not new_repos:
            print('No new job postings')

        for repo in new_repos:
            seen_already.add(repo)
            send_email("IMPORTANT: NEW JOB POSTING, APPLY ASAP", message, from_addr, to_addr, smtp_server, smtp_port, username, password, repo)
            time.sleep(5)
    except:
        print('Error scraping GitHub repos')


def send_email(subject, message, from_addr, to_addr, smtp_server, smtp_port, username, password, repo):
    try:
        data = {
            'companyName': repo.find_all("td")[0].text,
            'position': repo.find_all("td")[1].text,
            'location': repo.find_all("td")[2].text,
            'url': repo.find_all("td")[3].find('a').get('href') if repo.find_all("td")[3].find('a') else 'No URL'
        }

        message = f"""
        Hello,

        We're excited to announce a new job opening for the position of {data['position']} at {data['companyName']}.

        You can apply for the job here: {data['url']}

        Best,
        Ismail
        """

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr

        server = smtplib.SMTP(smtp_server, smtp_port)

        status_code, response = server.ehlo()
        print(f"[*] Echoing: {status_code}, {response}")

        status_code, response = server.starttls()
        print(f"[*] Starting TLS: {status_code}, {response}")

        status_code, response = server.login(username, password)
        print(f"[*] Logging in: {status_code}, {response}")
        server.send_message(msg)
        server.quit()
    except:
        print('Error sending email')


def initial_load():
    try:
        url = f"https://github.com/SimplifyJobs/New-Grad-Positions"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        repos = soup.find_all("markdown-accessiblity-table")[0].find_all("tbody")[0].find_all("tr")

        for repo in repos:
            seen_already.add(repo)
        
        print('Initial load successful')
    except:
        print('Error initial load')


def test_email():
    try:
        send_email("Testing", message, from_addr, to_addr, smtp_server, smtp_port, username, password, list(seen_already)[0])
        print('Successfully sent test email')
    except:
        print('Error sending test email')


if __name__ == "__main__":
    seen_already = set()

    initial_load()
    test_email()

    while True:
        scrape_github_repos()
        print('Sleeping for 5 minutes')
        time.sleep(300)
        print('Waking up')