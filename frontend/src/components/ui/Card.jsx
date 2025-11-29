export default function Card({ children }) {
  return (
    <div className="p-4 rounded-lg shadow  dark:bg-gray-200 dark:text-black">
      {children}
    </div>
  );
}
