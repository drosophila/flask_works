# this is a cms service for help
# defining two pages, company history and company employees

fake_db = {
    "/help/faq":{
        "page_title": "Ferquently Asked Questions",
        "page_details": "Details about FAQ ..."
    },
    "/help/payments":{
        "page_title": "Payment methods",
        "page_details": "Details Payment Methods ..."
    },
}

def get_topic(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    url = "/"+url.lstrip("/")

    page = fake_db.get(url, {})
    return page