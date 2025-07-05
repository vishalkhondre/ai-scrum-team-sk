# 🤝 AI Scrum Team with Semantic Kernel 🚀

This repo demonstrates how to build an **AI-first Scrum Team** using the [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel) **Group Chat Orchestration** pattern.

## 📌 Use Case

Simulate a collaborative Scrum team that turns raw requirements into production-ready Agile artifacts:
- **Product Owner Agent:** Generates System Requirements Specification (SRS).
- **Business Analyst Agent:** Breaks SRS into detailed User Stories & Acceptance Criteria.
- **Solution Architect Agent:** Designs Solution Architecture, identifies technical dependencies.
- **QA Agent:** Writes Test Scenarios and Test Cases in Gherkin syntax.

Input: ✏️ *“As a customer, I want to order groceries online for same-day delivery...”*  
Output: ✅ SRS ➜ User Stories ➜ Solution Design ➜ Test Cases.

---

## 🗂️ Repo Structure

| Folder | Purpose |
| ------ | ------- |
| `agents/` | Defines each Scrum role agent and its instructions. |
| `manager/` | Contains the `ScrumGroupChatManager` class to control conversation flow, turn-taking, and termination. |
| `runtime/` | Orchestrates the agents with Semantic Kernel GroupChatOrchestration. |
| `examples/` | Includes example raw requirements for testing. |
| `.env.example` | Sample for environment variables. |
| `requirements.txt` | Python dependencies. |

---

## ⚙️ How It Works

✅ **1.** Load raw requirements from file or input.  
✅ **2.** Pass to the group chat orchestration.  
✅ **3.** Agents collaborate:  
   1️⃣ PO ➜ 2️⃣ BA ➜ 3️⃣ SA ➜ 4️⃣ QA  
✅ **4.** The manager coordinates turns & stops when the final deliverables are ready.  
✅ **5.** Final results are printed and saved.

---

## 🏃‍♂️ Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-org/ai-scrum-team-sk.git
   cd ai-scrum-team-sk
