from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analytics_service import AnalyticsService

app = FastAPI()

analytics = AnalyticsService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analytics/summary")
def analytics_summary():

    return analytics.get_summary()

@app.get("/analytics/distribution")
def analytics_distribution():

    return analytics.get_event_distribution()

@app.get("/analytics/distribution")
def analytics_distribution():

    return analytics.get_event_distribution()


@app.get("/analytics/active-users")
def analytics_active_users():

    return analytics.get_active_users()


@app.get("/analytics/timeline")
def analytics_timeline():

    return analytics.get_timeline()