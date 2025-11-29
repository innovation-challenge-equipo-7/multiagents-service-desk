export default function EscalationTable({ data }) {
return (
<table className="w-full text-left border">
<thead>
<tr>
<th className="border p-2">ID</th>
<th className="border p-2">Status</th>
</tr>
</thead>
<tbody>
{data?.map((row) => (
<tr key={row.id}>
<td className="border p-2">{row.id}</td>
<td className="border p-2">{row.status}</td>
</tr>
))}
</tbody>
</table>
);
}