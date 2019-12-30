#defining two pages, company history and company employees
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

def get_page(url: str) -> dict