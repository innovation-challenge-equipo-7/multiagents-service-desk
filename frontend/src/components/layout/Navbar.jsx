import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="h-16 bg-neutral-800 text-white flex items-center px-6 justify-between">
      <h1 className="text-xl font-bold">AI Support Desk</h1>

      <div className="flex gap-6">
        <Link to="/" className="hover:text-blue-400">Chat</Link>
        <Link to="/dashboard" className="hover:text-blue-400">
          Dashboard
        </Link>
      </div>
    </nav>
  );
};


export default Navbar;
