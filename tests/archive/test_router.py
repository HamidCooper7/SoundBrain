from brain.orchestration.models import Plan
from brain.orchestration.state import State
from brain.orchestration.router import Router


router = Router()


plans = [

    Plan(
        use_rag=True,
        use_memory=True,
        use_audio=False,
        use_vision=False,
        use_reasoning=False,
        use_tools=False,
        use_recommendation=False,
        use_report=False,
        selected_agents=[],
        selected_tools=[],
    ),

    Plan(
        use_rag=True,
        use_memory=True,
        use_audio=True,
        use_vision=False,
        use_reasoning=False,
        use_tools=False,
        use_recommendation=False,
        use_report=False,
        selected_agents=[],
        selected_tools=[],
    ),

    Plan(
        use_rag=True,
        use_memory=True,
        use_audio=True,
        use_vision=True,
        use_reasoning=True,
        use_tools=True,
        use_recommendation=True,
        use_report=True,
        selected_agents=[],
        selected_tools=[],
    ),

]


for plan in plans:

    print("=" * 80)

    print(router.route(plan))