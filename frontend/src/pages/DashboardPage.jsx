import { useDashboardStats } from "../hooks/useDashboardStats";
import StatsSidebar from "../components/dashboard/StatsSidebar";
import Card from "../components/ui/Card";

export default function DashboardPage() {
  const stats = useDashboardStats();

  return (
    <div className="flex h-full">
      <StatsSidebar stats={stats} />

      <div className="p-4 flex-1 grid grid-cols-2 gap-4">
        <Card><h2>Section 1</h2></Card>
        <Card><h2>Section 2</h2></Card>
      </div>
    </div>
  );
}
