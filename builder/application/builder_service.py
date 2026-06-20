from pathlib import Path

from builder.generator.factory import Factory
from builder.workflow.builder_workflow import BuilderWorkflow


class BuilderService:
    def __init__(
        self,
        factory: Factory | None = None,
        workflow: BuilderWorkflow | None = None,
    ) -> None:
        self.factory = factory or Factory()
        self.workflow = workflow or BuilderWorkflow()

    def create_project(self, name: str, output_root: str = "output/projects") -> Path:
        generator = self.factory.create("project")
        return generator.generate(name, output_root)

    def generate(self, generator_type: str, name: str):
        generator = self.factory.create(generator_type)
        return generator.generate(name)

    def workflow_verify(self) -> str:
        return "\n".join(self.workflow.verify_plan())

    def workflow_commit_message(self, scope: str, message: str) -> str:
        plan = self.workflow.plan_commit("feat", scope, message)
        return plan["commit_message"]
