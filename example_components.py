from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component

@xai_component
class HelloComponentLibrary(Component):
    input_str: InArg[str]

    def __init__(self):

        self.done = False
        self.input_str = InArg.empty()

    def execute(self, ctx) -> None:
        input_str = self.input_str.value
        print("Hello, " + str(input_str))
        self.done = True
