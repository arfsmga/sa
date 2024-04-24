import asyncio

from websockets import serve  # type: ignore


async def handler(websocket) -> None:
    """WebSocketのmain処理。"""
    while True:
        msg = await websocket.recv()
        print("msg received")
        print(f"{msg}")  # 現状は受信したメッセージをprintするだけ


async def start_server() -> None:
    """WebSocket待ち受けを開始する."""
    print("Start")
    await serve(
        handler,
        "172.24.50.245",
        5500,
    )


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_server())
    asyncio.get_event_loop().run_forever()
