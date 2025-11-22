import { useState } from "react";


export default function ChatInput({ onSend }) {
const [text, setText] = useState("");


const handleSubmit = (e) => {
e.preventDefault();
if (!text.trim()) return;
onSend(text);
setText("");
};

return (
<form onSubmit={handleSubmit} className="flex gap-2 p-4">
<input
type="text"
placeholder="Type a message..."
value={text}
onChange={(e) => setText(e.target.value)}
className="flex-1 px-3 py-2 border rounded"
/>
<button className="px-4 py-2 bg-blue-600 text-white rounded">
Send
</button>
</form>
);
}