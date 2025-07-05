import os
from dotenv import load_dotenv

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
model = os.getenv("MODEL_NAME")

def create_product_owner_agent():
    return ChatCompletionAgent(
        name="ProductOwner",
        description="Generates a detailed System Requirements Specification (SRS) from raw requirements.",
        instructions=(
            "You are an experienced Product Owner. "
            "Your job is to transform raw, high-level business requirements into a clear, structured System Requirements Specification (SRS). "
            "The SRS should include a project overview, detailed features, constraints, assumptions, and any business rules."
        ),
        service=AzureChatCompletion(
            deployment_name=model,
            api_key=api_key,
            base_url=endpoint
        )
    )
