from builder.sprint.sprint_runner import SprintRunner
from builder.cli.command_router import CommandRouter


def test_sprint_runner_can_run():
    result = SprintRunner().run(34)

    assert result == "Sprint #000034 run completed"


def test_command_router_supports_sprint_run():
    result = CommandRouter().handle("sprint run 34")

    assert result == "Sprint #000034 run completed"
