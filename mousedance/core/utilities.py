
from typing import Type
from typing import TypeVar
from typing import Generic
from typing import Iterator
from typing import Optional
from typing import get_args

T = TypeVar("T")

class SingleGeneric(Generic[T]):
    __generic_type: T = None
    
    @classmethod
    @property
    def generic_type(cls) -> Type[T]:
        if cls.__generic_type is None:
            __orig_bases__ = \
                getattr(cls, "__orig_bases__")
            
            cls.__generic_type = \
                get_args(__orig_bases__[0])[0]
            
        return cls.__generic_type

class Singleton(SingleGeneric[T]):
    __instance: T = None

    def __new__(cls, *positional_arguments, **keyword_arguments):
        if cls.has_instance():
            return cls.get_instance()
        
        else:
            instance = cls.generic_type(
                *positional_arguments, 
                **keyword_arguments
            )

            cls.set_instance(
                instance = instance
            )

            return instance

    @classmethod
    def validate_instance(cls, instance: T) -> None:
        if not isinstance(instance, cls.generic_type):
            raise TypeError(
                f"an instance should be type of {cls.generic_type}, " + \
                f"not a type of {instance.__class__}."
            )
        
    @classmethod
    def get_instance(cls) -> T:
        return cls.__instance

    @classmethod
    def set_instance(cls, instance: T) -> None:
        cls.validate_instance(
            instance = instance
        )

        if cls.__instance is not None:
            raise ValueError(
                "as an instance is already assigned, " + 
                "use 'update_instance' instead."
            )
        
        else:
            cls.__instance = instance

    @classmethod
    def has_instance(cls) -> bool:
        return cls.get_instance() is not None
    
    @classmethod
    def delete_instance(cls) -> None:
        cls.__instance = None
    
    @classmethod
    def update_instance(cls, instance: T) -> None:
        cls.delete_instance()
        return cls.set_instance(instance = instance)

class Cache(SingleGeneric[T]):
    instance: Optional[T] = None
    
    def __init__(self, instance: T = None):
        self.instance = instance

class FactoryRelationship(object):

    @classmethod
    def get_subtypes(cls, base: Type[T]) -> Iterator[Type[T]]:
        for subtype in base.__subclasses__():
            yield from cls.get_subtypes(subtype)
            yield subtype

class Factory(SingleGeneric[T]):

    def __new__(cls, name: str, *positional_arguments, **keyword_arguments) -> T:
        # set generic type `T` for the class `Factory`.
        generic_type: Type[T] = cls.generic_type

        for subclass in FactoryRelationship.get_subtypes(generic_type):
            if subclass.__name__.lower() == name.lower():
                return subclass(*positional_arguments, **keyword_arguments)