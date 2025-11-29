import { useState } from "react";
import { sendMessageToApi } from "../services/chatApi";


// Custom chat hook
export const useChat = () => {
const [messages, setMessages] = useState([]);
const [loading, setLoading] = useState(false);


const sendMessage = async (text) => {
setMessages((prev) => [...prev, { from: "user", text }]);
setLoading(true);


const reply = await sendMessageToApi(text);
setLoading(false);


if (reply.error) {
setMessages((prev) => [...prev, { from: "bot", text: reply.error }]);
} else {
setMessages((prev) => [...prev, { from: "bot", text: reply.reply }]);
}
};


return { messages, loading, sendMessage };
};