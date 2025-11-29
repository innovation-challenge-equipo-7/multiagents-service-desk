// Handles communication with the Chat Azure Function
export const sendMessageToApi = async (message) => {
try {
const response = await fetch("/api/chat", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify({ message }),
});
return await response.json();
} catch (error) {
console.error("Chat API error:", error);
return { error: "Network error" };
}
};
