export default function Card({ children }) {
return (
<div className="p-4 rounded-lg shadow bg-white dark:bg-gray-200">
{children}
</div>
);
}