import { useState, useContext } from "react";
import { Link } from "react-router-dom";
import { FiX, FiHome, FiMessageCircle, FiBarChart2 } from "react-icons/fi";
import { ThemeContext } from "../../context/ThemeContext";

const Navbar = () => {
  const [open, setOpen] = useState(false);
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <>
      {/* NAVBAR */}
      <nav className="h-16 bg-neutral-800 dark:bg-neutral-900 text-white flex items-center px-6 justify-between">

        {/* Título que abre el menú */}
        <h1
          className="text-xl font-bold cursor-pointer select-none"
          onClick={() => setOpen(true)}
          role="button"
          aria-label="Abrir menú"
          aria-expanded={open}
        >
          AI Support Desk
        </h1>

        {/* Right section: theme + links */}
        <div className="flex items-center gap-4">

          {/* Toggle Theme Button */}
          <button
            onClick={toggleTheme}
            className="px-3 py-1 bg-gray-600 rounded hover:bg-gray-500 transition"
          >
            {theme === "light" ? "🌙 Dark" : "☀ Light"}
          </button>

          {/* Links visibles solo en desktop */}
          <div className="hidden md:flex gap-6">
            <Link to="/" className="hover:text-blue-400">Chat</Link>
            <Link to="/dashboard" className="hover:text-blue-400">Dashboard</Link>
          </div>

        </div>
      </nav>

      {/* SIDEBAR */}
      {open && (
        <div
          className="fixed inset-0 bg-black bg-opacity-40 z-40"
          onClick={() => setOpen(false)}
        >
          <aside
            className="w-64 h-full bg-gray-900 text-gray-200 p-6 flex flex-col border-r border-gray-700
                       shadow-xl z-50 transform transition-transform duration-300 translate-x-0"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Header */}
            <div className="flex justify-between items-center mb-8">
              <h2 className="text-xl font-semibold">Menu</h2>
              <button onClick={() => setOpen(false)}>
                <FiX size={24} />
              </button>
            </div>

            {/* Links */}
            <nav className="flex flex-col gap-3">

              <Link
                to="/dashboard"
                onClick={() => setOpen(false)}
                className="hover:bg-gray-800 px-3 py-2 rounded-lg flex items-center gap-3"
              >
                <FiBarChart2 size={20} />
                Dashboard
              </Link>

              <Link
                to="/chat"
                onClick={() => setOpen(false)}
                className="hover:bg-gray-800 px-3 py-2 rounded-lg flex items-center gap-3"
              >
                <FiMessageCircle size={20} />
                Chat
              </Link>

              <Link
                to="/"
                onClick={() => setOpen(false)}
                className="hover:bg-gray-800 px-3 py-2 rounded-lg flex items-center gap-3"
              >
                <FiHome size={20} />
                Home
              </Link>

            </nav>

            {/* Footer */}
            <div className="mt-auto text-xs text-gray-500">
              © 2025 Safe Desk AI
            </div>
          </aside>
        </div>
      )}
    </>
  );
};

export default Navbar;
