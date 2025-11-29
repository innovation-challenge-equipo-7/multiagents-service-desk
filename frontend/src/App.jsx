import { BrowserRouter, Routes, Route } from "react-router-dom";
import ChatPage from "./pages/ChatPage";
import DashboardPage from "./pages/DashboardPage";
import Navbar from "./components/layout/Navbar";
import { ThemeProvider } from "./context/ThemeContext";
import Sidebar from "./components/layout/Sidebar";

export default function App() {
  return (
    <ThemeProvider>
      <BrowserRouter>
        <Navbar />
        

        {/* Contenido principal con margen para evitar que el Navbar lo tape */}
        <main className="mt-16 h-[calc(100vh-4rem)]">
          <Routes>
            <Route path="/" element={<ChatPage />} />
            <Route path="/dashboard" element={<DashboardPage />} />
          </Routes>
        </main>
      </BrowserRouter>
    </ThemeProvider>
  );
}
