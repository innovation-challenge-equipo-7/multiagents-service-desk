// src/components/layout/Sidebar.jsx

import React from "react";
import { FiHome, FiMessageCircle, FiBarChart2 } from "react-icons/fi";

const Sidebar = () => {
  return (
    <aside className="w-64 h-screen bg-gray-900 text-gray-200 p-6 flex flex-col border-r border-gray-700">
      {/* Logo */}
      <h1 className="text-xl font-bold mb-10">Safe Desk Admin</h1>

      {/* Menu Section */}
      <nav className="flex flex-col gap-4">
        <a
          href="/dashboard"
          className="flex items-center gap-3 text-gray-300 hover:text-white hover:bg-gray-800 p-3 rounded-lg transition"
        >
          <FiBarChart2 size={20} />
          Dashboard
        </a>

        <a
          href="/chat"
          className="flex items-center gap-3 text-gray-300 hover:text-white hover:bg-gray-800 p-3 rounded-lg transition"
        >
          <FiMessageCircle size={20} />
          Chat
        </a>

        <a
          href="/"
          className="flex items-center gap-3 text-gray-300 hover:text-white hover:bg-gray-800 p-3 rounded-lg transition"
        >
          <FiHome size={20} />
          Home
        </a>
      </nav>

      {/* Footer Section */}
      <div className="mt-auto text-sm text-gray-500">
        © 2025 Safe Desk AI
      </div>
    </aside>
  );
};

export default Sidebar;
