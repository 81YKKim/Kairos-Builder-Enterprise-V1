from builder.sprint.sprint_manager import SprintManager


class BuilderWorkflow:
    def __init__(self, sprint_manager: SprintManager | None = None) -> None:
        self.sprint_manager = sprint_manager or SprintManager()

    def plan_commit(self, commit_type: str, scope: str, message: str) -> dict:
        commit_message = self.sprint_manager.build_commit_message(
            commit_type,
            scope,
            message,
        )

        return {
            "sprint": self.sprint_manager.sprint_label(),
            "commit_message": commit_message,
            "steps": [
                "run_tests",
                "git_add",
                "git_commit",
                "git_push",
            ],
        }

    def verify_plan(self) -> list[str]:
        return [
            "pytest",
            "git status",
        ]
