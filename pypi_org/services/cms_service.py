# this is a cms service
# defining two pages, company history and company employees

fake_db = {
    "/company/history":{
        "page_title": "Company History",
        "page_details": "Details about the Company History ..."
    },
    "/company/employees":{
        "page_title": "Out Team",
        "page_details": "Details about company employees ..."
    },
}

def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    url = "/"+url.lstrip("/")

    page = fake_db.get(url, {})
    return page