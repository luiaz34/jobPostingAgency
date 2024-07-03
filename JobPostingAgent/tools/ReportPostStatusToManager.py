from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class ReportPostStatusToManager(BaseTool):
    """
    This tool reports the status of each job description post back to the ManagerAgent.
    It takes a list of post statuses as input and sends them to the ManagerAgent via a specified endpoint.
    """

    post_statuses: list = Field(
        ..., description="A list of post statuses to be reported to the ManagerAgent."
    )
    manager_endpoint: str = Field(
        default="https://manager.example.com/report-status",
        description="The endpoint URL of the ManagerAgent where the post statuses will be sent."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method sends the list of post statuses to the ManagerAgent via the specified endpoint.
        """
        try:
            # Prepare the payload to be sent to the ManagerAgent
            payload = {
                "post_statuses": self.post_statuses
            }

            # Send the post statuses to the ManagerAgent via the specified endpoint
            response = requests.post(self.manager_endpoint, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            return "Post statuses reported to the ManagerAgent successfully."
        except requests.RequestException as e:
            return f"Failed to report post statuses to the ManagerAgent: {str(e)}"