import { useEffect, useState } from "react";
import StatCard from "./StatCard";
import {
  getSummary,
  getActiveUsers,
  getDistribution,
  getTimeline
} from "../api/analyticsApi";
import DistributionChart from "./DistributionChart";
import TimelineChart from "./TimelineChart";

function Dashboard() {
  const [totalEvents, setTotalEvents] = useState(0);
  const [activeUsers, setActiveUsers] = useState(0);
  const [distribution, setDistribution] = useState([]);
  const [timeline, setTimeline] = useState([]);

  useEffect(() => {

    fetchAnalytics();

    const interval = setInterval(
        fetchAnalytics,
        5000
    );

    return () =>
        clearInterval(interval);

   }, []);

  

  const fetchAnalytics = async () => {
    try {
      const summaryResponse = await getSummary();
      const activeUsersResponse = await getActiveUsers();
      const distributionResponse = await getDistribution();
      const timelineResponse = await getTimeline();
      setTotalEvents(
        summaryResponse.data.total_events
      );

      setActiveUsers(
        activeUsersResponse.data.active_users
      );
      
      setDistribution(
        distributionResponse.data
      );
      setTimeline(
        timelineResponse.data
        );
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="dashboard">

        <h1 className="dashboard-title">
        Distributed Log Dashboard
        </h1>

        <div className="cards-container">

        <StatCard
            title="Total Events"
            value={totalEvents}
        />

        <StatCard
            title="Active Users"
            value={activeUsers}
        />

        </div>

        <DistributionChart
        data={distribution}
        />

        <TimelineChart
         data={timeline}
        />

    </div>
    );

 
 
}

export default Dashboard;