class SceneElement(object):
    """Base class for elements of a scene"""
    def __init__(self, 
                 name: str,
                 description: str):
        self.name = name
        self.description = description

    @property
    def name(self) -> str:
        return self.__name
        
    @property
    def description(self) -> str:
        return self.__description

    @name.setter
    def name(self, name: str):
        assert type(name) is str
        self.__name = name

    @description.setter
    def description(self, description: str):
        assert type(description) is str
        self.__description = description

# History demo, useful for undo functionality
# class A( object ):
#     @property
#     def val( self ):
#         return self.history[ -1 ]

#     @val.setter
#     def val( self, value ):
#         self.history.append( value )

#     def __init__( self, val ):
#         self.history = [ ]
#         self.val = val