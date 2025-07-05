import os
from dotenv import load_dotenv

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
model = os.getenv("MODEL_NAME")

def create_business_analyst_agent():
    return ChatCompletionAgent(
        name="BusinessAnalyst",
        description="Breaks the SRS into detailed user stories with acceptance criteria in Given/When/Then format.",
        instructions=(
            "You are a professional Business Analyst. "
            "You take a System Requirements Specification (SRS) and break it down into Agile user stories. "
            "For each story, write acceptance criteria in Given/When/Then format. "
            "Ensure the stories are clear, small, and testable."
        ),
        service=AzureChatCompletion(
            deployment_name=model,
            api_key=api_key,
            base_url=endpoint
        )
    )
