from agency_swarm.tools import BaseTool
from pydantic import Field
import requests

class SendFormattedJobDescriptions(BaseTool):
    """
    This tool sends the formatted job descriptions to the ManagerAgent for further actions.
    It takes a list of formatted job descriptions as input and sends them to the ManagerAgent.
    """

    formatted_descriptions: list = Field(
        ..., description="A list of formatted job descriptions to be sent to the ManagerAgent."
    )
    manager_agent_url: str = Field(
        ..., description="The URL of the ManagerAgent endpoint to send the formatted job descriptions."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method sends the formatted job descriptions to the ManagerAgent for further actions.
        """
        try:
            # Prepare the payload to be sent to the ManagerAgent
            payload = {
                "formatted_descriptions": self.formatted_descriptions
            }

            # Send a POST request to the ManagerAgent endpoint
            response = requests.post(self.manager_agent_url, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors

            return "Formatted job descriptions sent to the ManagerAgent successfully."
        except requests.RequestException as e:
            return f"Failed to send formatted job descriptions: {str(e)}"