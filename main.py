from agency_swarm import Agency
from JobPostingAgent import JobPostingAgent
from JobDescriptionAgent import JobDescriptionAgent
from ManagerAgent import ManagerAgent
from agency_swarm.util.oai import set_openai_key
import os
from dotenv import load_dotenv

load_dotenv()

manager_agent = ManagerAgent()
job_description_agent = JobDescriptionAgent()
job_posting_agent = JobPostingAgent()

agency = Agency([manager_agent, [manager_agent, job_description_agent],
                 [manager_agent, job_posting_agent]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio(height=500)