from semantic_kernel.agents import GroupChatManager, StringResult, BooleanResult, MessageResult
from semantic_kernel.contents import ChatMessageContent, ChatHistory

class ScrumGroupChatManager(GroupChatManager):
    async def select_next_agent(self, chat_history: ChatHistory, participant_descriptions: dict[str, str]) -> StringResult:
        last = chat_history.messages[-1]

        if last.role == "user":
            return StringResult(result="ProductOwner", reason="Start with PO to generate SRS.")
        elif last.name == "ProductOwner":
            return StringResult(result="BusinessAnalyst", reason="BA should create user stories next.")
        elif last.name == "BusinessAnalyst":
            return StringResult(result="SolutionArchitect", reason="SA should review design next.")
        elif last.name == "SolutionArchitect":
            return StringResult(result="QATester", reason="QA should write test cases last.")
        elif last.name == "QATester":
            return StringResult(result="QATester", reason="QA finalizes output.")
        else:
            return StringResult(result="ProductOwner", reason="Fallback to PO.")

    async def should_terminate(self, chat_history: ChatHistory) -> BooleanResult:
        for msg in reversed(chat_history.messages):
            if msg.name == "QATester" and "Test cases complete" in msg.content:
                return BooleanResult(result=True, reason="QA confirmed done.")
        return BooleanResult(result=False, reason="Still in progress.")

    async def should_request_user_input(self, chat_history: ChatHistory) -> BooleanResult:
        return BooleanResult(result=False, reason="No human input needed.")

    async def filter_results(self, chat_history: ChatHistory) -> MessageResult:
        output = "# 📋 Scrum AI Team Deliverables\n\n"
        for msg in chat_history.messages:
            output += f"## {msg.name}\n{msg.content}\n\n"
        return MessageResult(
            result=ChatMessageContent(role="assistant", content=output),
            reason="All deliverables collated."
        )
