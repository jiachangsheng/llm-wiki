# Multi-turn Conversation Test

## Protocol
使用文件传递消息实现多轮对话。

## Message Files
- User → Agent: `/home/j/wiki/queries/msg-to-agent.txt`
- Agent → User: `/home/j/wiki/queries/msg-from-agent.txt`

## Flow
1. User writes question to msg-to-agent.txt
2. Agent reads, responds to msg-from-agent.txt
3. Repeat as needed
