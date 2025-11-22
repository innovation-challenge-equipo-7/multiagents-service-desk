export default function Button({ children, onClick, className = "" }) {
return (
<button
onClick={onClick}
className={`px-4 py-2 rounded-md font-medium transition border border-gray-400 dark:border-gray-600 ${className}`}
>
{children}
</button>
);
}