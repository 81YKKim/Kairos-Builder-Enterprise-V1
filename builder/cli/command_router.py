from builder.generator.factory import Factory
from builder.workflow.builder_workflow import BuilderWorkflow


class CommandRouter:
    def __init__(self):
        self.factory = Factory()
        self.workflow = BuilderWorkflow()

    def handle(self, command: str):
        parts = command.strip().split()

        if not parts:
            return None

        if parts[0] in ("exit", "quit"):
            return "exit"

        if parts == ["workflow", "verify"]:
            return "\n".join(self.workflow.verify_plan())

        if len(parts) == 4 and parts[0] == "workflow" and parts[1] == "commit":
            plan = self.workflow.plan_commit("feat", parts[2], parts[3])
            return plan["commit_message"]

        if len(parts) == 3 and parts[0] == "generate":
            generator_type = parts[1]
            name = parts[2]
            gen = self.factory.create(generator_type)
            return gen.generate(name)

        if len(parts) == 2 and parts[0] == "project":
            name = parts[1]
            gen = self.factory.create("project")
            return gen.generate(name)

        return f"Unknown command: {command}"
