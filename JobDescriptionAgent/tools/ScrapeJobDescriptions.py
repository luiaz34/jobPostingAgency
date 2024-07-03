from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import dotenv
from firecrawl import FirecrawlApp
from bs4 import BeautifulSoup

# Load environment variables from a .env file
dotenv.load_dotenv()

class ScrapeJobDescriptions(BaseTool):
    """
    This tool uses Firecrawl to scrape job descriptions from specified websites.
    It takes a URL as input and returns the raw HTML content of the job descriptions.
    """

    url: str = Field(
        ...,
        description="The URL of the website from which to scrape job descriptions."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method scrapes the job descriptions from the specified URL and returns the raw HTML content.
        """
        try:
            # Initialize the FirecrawlApp with your API key
            app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

            # Scrape the specified URL
            scraped_data = app.scrape_url(self.url)

            # Extract job descriptions from the scraped data
            raw_html_content = scraped_data.get('html', '')

            return raw_html_content
        except Exception as e:
            return f"Failed to scrape job descriptions: {str(e)}"

class ProcessAndFormatJobDescriptions(BaseTool):
    """
    This tool processes and formats the raw HTML content of job descriptions using the Instructor tool.
    It takes the raw HTML content as input and returns a list of formatted job descriptions.
    """

    raw_html_content: str = Field(
        ..., description="The raw HTML content of the job descriptions to be processed and formatted."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method processes and formats the raw HTML content of job descriptions and returns a list of formatted job descriptions.
        """
        try:
            # Parse the raw HTML content using Beautiful Soup
            soup = BeautifulSoup(self.raw_html_content, 'html.parser')

            # Extract text from each job description
            job_descriptions = soup.find_all('div', class_='job-description')
            formatted_descriptions = [description.get_text(strip=True) for description in job_descriptions]

            return formatted_descriptions
        except Exception as e:
            return f"Failed to process and format job descriptions: {str(e)}"
