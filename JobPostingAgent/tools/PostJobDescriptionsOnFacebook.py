from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class PostJobDescriptionsOnFacebook(BaseTool):
    """
    This tool uses the Facebook Page Posting API to post job descriptions on the specified Facebook page.
    It takes a list of formatted job descriptions and the Facebook Page Access Token as input and posts each job description on the Facebook page.
    """

    formatted_descriptions: list = Field(
        ..., description="A list of formatted job descriptions to be posted on the Facebook page."
    )
    page_access_token: str = Field(
        default="EAAOeanJcLZAQBO3Qmcb9lEuMhqQX236ClEXv9Hfc71aziFgrLRD57U3OoPLJ0keRaUYbDI27dBQB69KPLWpFa1e3TPAq2A9EPjm1mzoZBysxEA01bGQNOk8v4ir6r1txfQPGyCzoGLUHwlrVZBZCFEKWIiB1qlzSfCYwZBgAfxatdZCjNQ5ngJHNS2TEz0LGtcW9ZB7nE5WHmtmQZCMcusURcqWZAKNl3BGBD",
        description="The Facebook Page Access Token used to authenticate the API requests."
    )
    page_id: str = Field(
        default="371375712720815",
        description="The ID of the Facebook page where the job descriptions will be posted."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method posts each formatted job description on the specified Facebook page using the Facebook Page Posting API.
        """
        try:
            # Facebook Graph API endpoint for posting to a page
            

            # Ensure that formatted_descriptions contains only strings
            combined_descriptions = "\n\n".join(
                str(description) if isinstance(description, str) else str(description.get('description', ''))
                for description in self.formatted_descriptions
            )

            payload = {
                "access_token": self.page_access_token
            }

            url = f"https://graph.facebook.com/v20.0/{self.page_id}/feed?message={combined_descriptions}"

            response = requests.post(url, data=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            return "All job descriptions posted on the Facebook page successfully."
        except requests.RequestException as e:
            return f"Failed to post job descriptions on the Facebook page: {str(e)}"
