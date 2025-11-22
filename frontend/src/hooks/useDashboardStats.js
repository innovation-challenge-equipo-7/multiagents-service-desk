import { useEffect, useState } from "react";
import { getDashboardStats } from "../api/dashboardApi";


// Dashboard statistics hook
export const useDashboardStats = () => {
const [stats, setStats] = useState(null);


useEffect(() => {
getDashboardStats().then(setStats);
}, []);


return stats;
};