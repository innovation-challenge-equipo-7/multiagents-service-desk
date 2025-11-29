// Chat message bubble component
export default function ChatBubble({ text, from }) {
const isUser = from === "user";
return (
 <div
      className={`w-full flex mb-3 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`
          max-w-[70%] px-4 py-3 rounded-2xl shadow-md
          text-white leading-relaxed
          transition-all duration-200
          ${isUser ? "bg-blue-600 rounded-br-sm" : "bg-gray-700 rounded-bl-sm"}
        `}
      >
        {text}
      </div>
    </div>
  );
}
