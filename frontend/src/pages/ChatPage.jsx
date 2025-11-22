import ChatContainer from "../components/chat/ChatContainer";
import ChatInput from "../components/chat/ChatInput";
import { useChat } from "../hooks/useChat";

export default function ChatPage() {
  const { messages, loading, sendMessage } = useChat();

  return (
    <div className="flex flex-col h-full">
      <ChatContainer messages={messages} loading={loading} />
      <ChatInput onSend={sendMessage} />
    </div>
  );
}
