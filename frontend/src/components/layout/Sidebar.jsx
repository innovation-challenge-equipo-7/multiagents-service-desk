import { FiHome, FiMessageCircle, FiBarChart2 } from "react-icons/fi";

export default function Sidebar() {
  return (
    <aside className="w-48 h-full bg-gray-800 text-white p-4 space-y-4">
      <div className="flex items-center gap-2">
        <FiHome /> <span>Home</span>
      </div>

      <div className="flex items-center gap-2">
        <FiMessageCircle /> <span>Mensajes</span>
      </div>

      <div className="flex items-center gap-2">
        <FiBarChart2 /> <span>Dashboard</span>
      </div>
    </aside>
  );
}
