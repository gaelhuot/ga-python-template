"""Shared resources management module."""

from typing import Optional

import httpx


class SharedResources:
    """Container for shared application resources."""

    def __init__(self) -> None:
        self.http_client: Optional[httpx.AsyncClient] = None

    async def initialize(self) -> None:
        """Initialize shared resources."""
        # Initialize HTTP client with proper timeouts and connection pooling
        self.http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(30.0, connect=10.0),
            limits=httpx.Limits(
                max_keepalive_connections=20, max_connections=100
            ),
            follow_redirects=True,
        )

    async def cleanup(self) -> None:
        """Cleanup shared resources."""
        if self.http_client:
            await self.http_client.aclose()
            self.http_client = None


# Global resources instance
resources = SharedResources()
