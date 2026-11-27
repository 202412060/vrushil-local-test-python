"""Paging helper for list endpoints."""


def page(items: list, page_number: int, page_size: int = 20) -> list:
    """Return one page of items. page_number starts at 1."""
    start = (page_number - 1) * page_size
    return items[start:start + page_size]
