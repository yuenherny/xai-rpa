from xai_components.base import InArg, OutArg, Component, xai_component

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

class RpaMouse(Component):
    """A parent class for mouse actions"""
    element_identifier: InArg[str]
    test_coordinate: InArg[tuple]

    def __init__(self):
        self.element_identifier = InArg.empty()
        self.test_coordinate = InArg.empty()
        self.done = False

@xai_component
class RpaClick(RpaMouse):
    """Left clicks on an element.
    
    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)

    ##### inPorts:
    - element_identifier: The image of the element to be clicked. 
        Requires visual automation to be set to True.
        Default: None
    - test_coordinate: A tuple of coordinates to be clicked.
        Default: None

    ##### outPorts:
    - None
    """
    element_identifier: InArg[str]
    test_coordinate: InArg[tuple]

    def __init__(self):
        self.element_identifier = InArg.empty()
        self.test_coordinate = InArg.empty()
        self.done = False

    def execute(self) -> None:
        element_identifier = self.element_identifier.value
        test_coordinate = self.test_coordinate.value

        import rpa as r
        if element_identifier is not None:
            r.click(element_identifier=element_identifier)
            print("Left clicking element using visual...")
        else:
            r.click(test_coordinate=test_coordinate)
            print("Left clicking element using coordinate...")

        self.done = False

@xai_component
class RpaRightClick(RpaMouse):
    """Right clicks on an element.
    
    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)

    ##### inPorts:
    - element_identifier: The image of the element to be clicked. 
        Requires visual automation to be set to True.
        Default: None
    - test_coordinate: A tuple of coordinates to be clicked.
        Default: None

    ##### outPorts:
    - None
    """
    def execute(self) -> None:
        element_identifier = self.element_identifier.value
        test_coordinate = self.test_coordinate.value

        import rpa as r
        if element_identifier is not None:
            r.rclick(element_identifier=element_identifier)
            print("Right clicking element using visual...")
        else:
            r.rclick(test_coordinate=test_coordinate)
            print("Right clicking element using coordinate...")

        self.done = False

@xai_component
class RpaDoubleClick(RpaMouse):
    """Double left clicks on an element.
    
    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)

    ##### inPorts:
    - element_identifier: The image of the element to be clicked. 
        Requires visual automation to be set to True.
        Default: None
    - test_coordinate: A tuple of coordinates to be clicked.
        Default: None

    ##### outPorts:
    - None
    """
    def execute(self) -> None:
        element_identifier = self.element_identifier.value
        test_coordinate = self.test_coordinate.value

        import rpa as r
        if element_identifier is not None:
            r.dclick(element_identifier=element_identifier)
            print("Double clicking element using visual...")
        else:
            r.dclick(test_coordinate=test_coordinate)
            print("Double clicking element using coordinate...")

        self.done = False

@xai_component
class RpaHover(RpaMouse):
    """Hover on an element.
    
    ### Reference:
    - [RPA-Python Basic Functions](https://github.com/tebelorg/RPA-Python#basic-functions)

    ##### inPorts:
    - element_identifier: The image of the element to hover on. 
        Requires visual automation to be set to True.
        Default: None
    - test_coordinate: A tuple of coordinates to hover on.
        Default: None

    ##### outPorts:
    - None
    """
    def execute(self) -> None:
        element_identifier = self.element_identifier.value
        test_coordinate = self.test_coordinate.value

        import rpa as r
        if element_identifier is not None:
            r.hover(element_identifier=element_identifier)
            print("Hover on element using visual...")
        else:
            r.hover(test_coordinate=test_coordinate)
            print("Hover on element using coordinate...")

        self.done = False
