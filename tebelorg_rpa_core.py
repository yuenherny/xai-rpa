from xai_components.base import Component, InArg, xai_component


@xai_component
class RpaInit(Component):
    """Initiates RPA bot.

    ### Reference:
    - [RPA-Python Core Functions](https://github.com/tebelorg/RPA-Python#core-functions)

    ##### inPorts:
    - visual: Initiate workflow that involves images as bot input.
        Default: False
    - chrome: Whether to use Chrome as default browser.
        Default: True
    - turbo: To run workflow 10x faster. By default, bot runs at human speed.
        Default: False

    ##### outPorts:
    - None
    """
    visual: InArg[bool]
    chrome: InArg[bool]
    turbo: InArg[bool]

    def __init__(self):
        super().__init__()
        self.visual.value = False
        self.chrome.value = True
        self.turbo.value = False

    def execute(self, ctx) -> None:
        visual = self.visual.value
        chrome = self.chrome.value
        turbo = self.turbo.value
        print(f"Visual automation: {visual}, Chrome: {chrome}, Turbo: {turbo}")

        import rpa as r
        r.init(visual_automation=visual, chrome_browser=chrome, turbo_mode=turbo)
        print("Bot initiated.")


@xai_component
class RpaClose(Component):
    """Shutsdown the RPA bot.

    ### Reference:
    - [RPA-Python Core Functions](https://github.com/tebelorg/RPA-Python#core-functions)

    ##### inPorts:
    - None

    ##### outPorts:
    - None
    """

    def execute(self, ctx) -> None:
        print("Closing RPA...")
        import rpa as r
        r.close()


@xai_component
class RpaError(Component):
    """Raises exception on error.

    ### Reference:
    - [RPA-Python Core Functions](https://github.com/tebelorg/RPA-Python#core-functions)

    ##### inPorts:
    - raise_exception: Raise exception on error.
        Default: False

    ##### outPorts:
    - None
    """
    raise_exception: InArg[bool]

    def __init__(self):
        super().__init__()
        self.raise_exception.value = False

    def execute(self, ctx) -> None:

        import rpa as r
        r.error(self.raise_exception.value)
        print("Exception will be raised on error.")


@xai_component
class RpaDebug(Component):
    """Print & log debug info to `rpa_python.log`.

    ### Reference:
    - [RPA-Python Core Functions](https://github.com/tebelorg/RPA-Python#core-functions)

    ##### inPorts:
    - debug_log: Print and log debug info.
        Default: True

    ##### outPorts:
    - None
    """
    debug_log: InArg[bool]

    def __init__(self):
        super().__init__()
        self.debug_log.value = True

    def execute(self, ctx) -> None:

        import rpa as r
        r.debug(self.debug_log.value)
        print("Debug info will be logged to `rpa_python.log`.")
