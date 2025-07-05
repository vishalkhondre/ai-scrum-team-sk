import asyncio

from semantic_kernel.agents import GroupChatOrchestration
from semantic_kernel.agents.runtime import InProcessRuntime

from agents.product_owner import create_product_owner_agent
from agents.business_analyst import create_business_analyst_agent
from agents.solution_architect import create_solution_architect_agent
from agents.qa_agent import create_qa_agent

from manager.scrum_group_chat_manager import ScrumGroupChatManager

async def main():
    agents = [
        create_product_owner_agent(),
        create_business_analyst_agent(),
        create_solution_architect_agent(),
        create_qa_agent(),
    ]

    orchestration = GroupChatOrchestration(
        members=agents,
        manager=ScrumGroupChatManager(max_rounds=15),
        agent_response_callback=lambda m: print(f"\n**{m.name}**\n{m.content}\n")
    )

    runtime = InProcessRuntime()
    runtime.start()

    task = (
        "We need a system that lets customers order groceries online, "
        "select same-day delivery, pay by credit card or wallet, "
        "and use promo codes. The system must support secure user registration and order tracking."
    )

    result = await orchestration.invoke(
        task=task,
        runtime=runtime,
    )

    final_output = await result.get()

    print("\n=== FINAL SCRUM PACKAGE ===\n")
    print(final_output)

    with open("scrum_output.md", "w", encoding="utf-8") as f:
        f.write(str(final_output.content))

    print("\n✅ Deliverables saved to scrum_output.md\n")

    await runtime.stop_when_idle()

if __name__ == "__main__":
    asyncio.run(main())
