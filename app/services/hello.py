"""Hello world service."""

from datetime import datetime, timezone

from app.schemas.hello import HelloResponse


class HelloService:
    """Hello world service class."""

    @staticmethod
    async def get_hello_world() -> HelloResponse:
        """
        Get hello world message.

        Returns:
            HelloResponse: Hello world response with timestamp
        """
        return HelloResponse(
            message="Hello, World!",
            status="success",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
