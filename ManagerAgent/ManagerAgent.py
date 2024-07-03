from agency_swarm.agents import Agent


class ManagerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ManagerAgent",
            description="Receives requests from the user, coordinates between agents, and ensures the smooth functioning of the agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
