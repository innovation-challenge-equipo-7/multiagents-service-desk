export default function StatusBadge({ status }) {
const colors = {
open: "bg-green-500",
closed: "bg-red-500",
};


return (
<span className={`px-2 py-1 rounded text-white ${colors[status]}`}>{status}</span>
);
}