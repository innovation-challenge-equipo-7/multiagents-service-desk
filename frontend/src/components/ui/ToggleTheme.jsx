import ToggleTheme from "../ui/ToggleTheme";


export default function Navbar() {
return (
<nav className="w-full p-4  dark:bg-gray-300 flex justify-between">
<h1 className="font-bold">AI Support Dashboard</h1>
<ToggleTheme />
</nav>
);
}