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
    <form
      onSubmit={handleSubmit}
      className="flex items-center gap-3 p-4 border-t border-gray-700 bg-neutral-900"
    >
      <input
        type="text"
        placeholder="Escribe un mensaje..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="flex-1 px-4 py-2 rounded-xl bg-neutral-800 border border-gray-600 text-white
                   focus:outline-none focus:border-blue-500 transition"
      />

      <button
        className="px-5 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-medium transition"
      >
        Enviar
      </button>
    </form>
  );
}
