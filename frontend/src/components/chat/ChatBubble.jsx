// Chat message bubble component
export default function ChatBubble({ text, from }) {
const isUser = from === "user";
return (
<div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
<div
className={`max-w-xs px-4 py-2 rounded-lg text-white ${
isUser ? "bg-blue-500" : "bg-gray-600"
}`}
>
{text}
</div>
</div>
);
}
