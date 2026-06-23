import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const getSummary = () =>
  API.get("/analytics/summary");

export const getDistribution = () =>
  API.get("/analytics/distribution");

export const getActiveUsers = () =>
  API.get("/analytics/active-users");

export const getTimeline = () =>
  API.get("/analytics/timeline");