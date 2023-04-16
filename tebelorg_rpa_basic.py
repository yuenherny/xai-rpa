from xai_components.base import Component, InArg, xai_component


@xai_component
class RpaUrl(Component):
    """Opens the browser with specified URL.

    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)

    ##### inPorts:
    - url: The URL to be accessed in the browser.
        Default: None

    ##### outPorts:
    - None
    """
    url: InArg[str]

    def __init__(self):
        self.url = InArg.empty()
        self.done = False

    def execute(self, ctx) -> None:
        url = self.url.value
        print(f"Opening {url} on browser...")

        import rpa as r
        r.url(webpage_url=url)
        print(f"Browser opened with URL {url}.")

        self.done = False


@xai_component
class RpaClick(Component):
    """Click on an element.

    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)
    - [Element Identifier](https://github.com/tebelorg/RPA-Python#element-identifiers)

    ##### inPorts:
    - element: Path to visual example of an element to be clicked (images), or web element identifier
        (XPath selector, CSS selector, id, name, class, title, aria-label, text(), href).
        Default: None

    ##### outPorts:
    - None
    """
    element: InArg[str]

    def __init__(self):
        self.element = InArg.empty()
        self.done = False

    def execute(self, ctx) -> None:
        element = self.element.value
        print(f"Clicking element {element}...")

        import rpa as r
        try:
            r.click(element_identifier=element)
            print(f"Clicked element {element}.")
        except Exception as error:
            print(f"{error}")

        self.done = False


@xai_component
class RpaRclick(Component):
    """Right click on an element.

    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)
    - [Element Identifier](https://github.com/tebelorg/RPA-Python#element-identifiers)

    ##### inPorts:
    - element: Path to visual example of an element to be clicked (images), or web element identifier
        (XPath selector, CSS selector, id, name, class, title, aria-label, text(), href).
        Default: None

    ##### outPorts:
    - None
    """
    element: InArg[str]

    def __init__(self):
        self.element = InArg.empty()
        self.done = False

    def execute(self, ctx) -> None:
        element = self.element.value
        print(f"Right clicking element {element}...")

        import rpa as r
        try:
            r.rclick(element_identifier=element)
            print(f"Right clicked element {element}.")
        except Exception as error:
            print(f"{error}")

        self.done = False


@xai_component
class RpaDclick(Component):
    """Double click on an element.

    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)
    - [Element Identifier](https://github.com/tebelorg/RPA-Python#element-identifiers)

    ##### inPorts:
    - element: Path to visual example of an element to be clicked (images), or web element identifier
        (XPath selector, CSS selector, id, name, class, title, aria-label, text(), href).
        Default: None

    ##### outPorts:
    - None
    """
    element: InArg[str]

    def __init__(self):
        self.element = InArg.empty()
        self.done = False

    def execute(self, ctx) -> None:
        element = self.element.value
        print(f"Double clicking element {element}...")

        import rpa as r
        try:
            r.dclick(element_identifier=element)
            print(f"Double clicked element {element}.")
        except Exception as error:
            print(f"{error}")

        self.done = False


@xai_component
class RpaHover(Component):
    """Hover on an element.

    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)
    - [Element Identifier](https://github.com/tebelorg/RPA-Python#element-identifiers)

    ##### inPorts:
    - element: Path to visual example of an element to be clicked (images), or web element identifier
        (XPath selector, CSS selector, id, name, class, title, aria-label, text(), href).
        Default: None

    ##### outPorts:
    - None
    """
    element: InArg[str]

    def __init__(self):
        self.element = InArg.empty()
        self.done = False

    def execute(self, ctx) -> None:
        element = self.element.value
        print(f"Hovering on element {element}...")

        import rpa as r
        try:
            r.hover(element_identifier=element)
            print(f"Hovered on element {element}.")
        except Exception as error:
            print(f"{error}")

        self.done = False
