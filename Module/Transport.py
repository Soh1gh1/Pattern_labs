from dataclasses import dataclass

@dataclass
class TransportInfo:
    """Info about Transport.
    Args:
        Transport_id (int): ID of Transport.
        Limit1 (int): Limit of passengers in Transport.
        limit2 (int): Weight limit.
    """
    Transport_id: int
    Limit1: int
    limit2: float