from agency_swarm.agents import Agent


class JobPostingAgent(Agent):
    def __init__(self):
        super().__init__(
            name="JobPostingAgent",
            description="Posts job descriptions on Facebook using the Facebook Page Posting API.",
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
