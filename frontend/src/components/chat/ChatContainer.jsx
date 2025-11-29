import { useEffect, useRef } from "react";
import ChatBubble from "./ChatBubble";
import LoadingIndicator from "./LoadingIndicator";

export default function ChatContainer({ messages, loading }) {
  const scrollRef = useRef(null);

  // Auto-scroll al final cuando llegan mensajes
  useEffect(() => {
    if (!scrollRef.current) return;
    scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
  }, [messages, loading]);

  return (
    <div
      ref={scrollRef}
      className="flex flex-col gap-3 p-4 overflow-y-auto flex-1"
    >
      {messages.map((m, index) => (
        <ChatBubble key={index} text={m.text} from={m.from} />
      ))}

      {loading && <LoadingIndicator />}
    </div>
  );
}
