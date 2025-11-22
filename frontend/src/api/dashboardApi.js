// Fetches dashboard escalation queue mock (replace with Azure Function later)
export const getDashboardStats = async () => {
try {
const res = await fetch("/api/dashboard/stats");
return await res.json();
} catch (err) {
console.error("Dashboard API error:", err);
return { error: "Network error" };
}
};
