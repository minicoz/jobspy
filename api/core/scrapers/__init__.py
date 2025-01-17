from ..jobs import *


class StatusException(Exception):
    def __init__(self, status_code: int):
        self.status_code = status_code


class Site(Enum):
    LINKEDIN = "linkedin"
    INDEED = "indeed"
    ZIP_RECRUITER = "zip_recruiter"


class ScraperInput(BaseModel):
    site_type: Site
    search_term: str

    location: str = None
    distance: int = None
    is_remote: bool = False
    job_type: JobType = None
    easy_apply: bool = None  # linkedin

    results_wanted: int = 15


class Scraper:
    def __init__(self, site: Site):
        self.site = site

    def scrape(self, scraper_input: ScraperInput) -> JobResponse:
        ...
