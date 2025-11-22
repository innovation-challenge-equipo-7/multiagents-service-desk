export default function StatsSidebar({ stats }) {
return (
<aside className="p-4 bg-gray-100 dark:bg-gray-400 h-full w-64">
<h2 className="text-xl font-bold mb-3">Dashboard Stats</h2>
{stats ? (
<ul>
<li>Total: {stats.total}</li>
<li>Resolved: {stats.resolved}</li>
</ul>
) : (
<p>Loading...</p>
)}
</aside>
);
}