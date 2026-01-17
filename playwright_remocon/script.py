from playwright.sync_api import sync_playwright
from datetime import datetime
import os

USERNAME = "frigerio.sergio@gmail.com"
PASSWORD = "7T3J#.w#GQZ?8kZ"

URL = "https://www.remocon-net.remotethermo.com/R2/Plant/Index/10521C70DB5C"

DOWNLOAD_DIR = "/share/remocon_export"
today = datetime.now().strftime("%Y-%m-%d")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ]
    )

    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto(URL, timeout=60000)

    page.fill('#LoginModelForm_Email', USERNAME)
    page.fill('#LoginModelForm_Password', PASSWORD)
    page.click('#loginForm > div:nth-child(6) > div > button')

    page.wait_for_load_state("networkidle")

    page.click('#navMenuItem_Metering')
    page.wait_for_load_state("networkidle")

    popup_selector = '#messageBoxModal .gfm-msgbox-cancel-button'
    try:
        if page.is_visible(popup_selector):
            page.click(popup_selector)
    except:
        pass

    export_btn = '#partial-ctrl-plantmetering button'
    page.wait_for_selector(export_btn, timeout=60000)

    with page.expect_download() as download_info:
        page.evaluate(f"document.querySelector('{export_btn}').click()")

    download = download_info.value

    file_path = os.path.join(DOWNLOAD_DIR, f"remocon_{today}.xlsx")
    download.save_as(file_path)

    browser.close()

print(f"Export completato: {file_path}")
