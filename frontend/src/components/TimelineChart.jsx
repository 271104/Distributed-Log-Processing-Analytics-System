import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

function TimelineChart({ data }) {
  return (
    <div className="chart-card">
      <h2>Event Timeline</h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >
        <LineChart data={data}>
          <XAxis
            dataKey="minute"
            stroke="#cbd5e1"
          />

          <YAxis
            stroke="#cbd5e1"
          />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="count"
            stroke="#38bdf8"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default TimelineChart;