import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

function DistributionChart({ data }) {
  return (
    <div className="chart-card">

      <h2>Event Distribution</h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <BarChart data={data}>
          <XAxis dataKey="event_type" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#38bdf8" />
          
        </BarChart>
      </ResponsiveContainer>

    </div>
  );
}

export default DistributionChart;