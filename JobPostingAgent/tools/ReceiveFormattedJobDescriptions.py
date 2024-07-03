from agency_swarm.tools import BaseTool
from pydantic import Field

class ReceiveFormattedJobDescriptions(BaseTool):
    """
    This tool receives formatted job descriptions from the ManagerAgent.
    It takes a list of formatted job descriptions as input and stores them in an instance variable for further processing.
    """

    formatted_descriptions: list = Field(
        ..., description="A list of formatted job descriptions received from the ManagerAgent."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method stores the formatted job descriptions in an instance variable for further processing.
        """
        try:
            # Store the formatted job descriptions in an instance variable for further processing
            self.stored_descriptions = self.formatted_descriptions

            return "Formatted job descriptions received and stored successfully."
        except Exception as e:
            return f"Failed to receive and store formatted job descriptions: {str(e)}"