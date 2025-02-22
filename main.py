from fastapi import FastAPI
from models import MsgPayload
from mangum import Mangum

app = FastAPI()
messages_list: dict[int, MsgPayload] = {}


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello From FastAPI App!"}

@app.get("/dev/health")
def root() -> dict[str, str]:
    return {"message": "Healthy From FastAPI App!"}

# About page route
@app.get("/dev/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}


# Route to add a message
@app.post("/dev/putmessages/{msg_name}")
def add_msg(msg_name: str) -> dict[str, MsgPayload]:
    print(f"Adding message: {msg_name}")
    # Generate an ID for the item based on the highest ID in the messages_list
    msg_id = max(messages_list.keys()) + 1 if messages_list else 0
    messages_list[msg_id] = MsgPayload(msg_id=msg_id, msg_name=msg_name)

    return {"message": messages_list[msg_id]}


# Route to list all messages
@app.get("/dev/messages")
def message_items() -> dict[str, dict[int, MsgPayload]]:
    return {"messages:": messages_list}

handler = Mangum(app)
