"""
StudySync -- Find a Study Spot (Ticket 3, Tinker 3B).

Loads study spots, scores profile matches, and explains the top results.
"""

import csv

NOISE_ORDER = {"quiet": 0, "moderate": 1, "loud": 2}


def load_study_spots(csv_path: str) -> list:
    """Load CSV rows and convert distance and seats to numbers."""
    with open(csv_path, newline="", encoding="utf-8") as file:
        spots = list(csv.DictReader(file))

    for spot in spots:
        spot["distance_miles"] = float(spot["distance_miles"])
        spot["seats_available"] = int(spot["seats_available"])

    return spots


def score_study_spot(profile: dict, spot: dict) -> tuple:
    """Award points for noise, distance, and seat availability."""
    score = 0.0
    reasons = []

    if NOISE_ORDER[spot["noise_level"]] <= NOISE_ORDER[profile["max_noise"]]:
        score += 3
        reasons.append(f"noise acceptable: {spot['noise_level']} (+3)")
    else:
        reasons.append(f"too noisy: {spot['noise_level']} (+0)")

    if spot["distance_miles"] <= profile["max_distance"]:
        score += 2
        reasons.append(f"close enough: {spot['distance_miles']:.1f} miles (+2)")
    else:
        reasons.append(f"too far: {spot['distance_miles']:.1f} miles (+0)")

    if spot["seats_available"] >= profile["min_seats"]:
        score += 1
        reasons.append(f"enough seats: {spot['seats_available']} (+1)")
    else:
        reasons.append(f"too few seats: {spot['seats_available']} (+0)")

    return score, reasons


def rank_study_spots(profile: dict, spots: list, k: int = 3) -> list:
    """Score every spot, sort descending, and return the top k."""
    scored = []
    for spot in spots:
        score, reasons = score_study_spot(profile, spot)
        scored.append((spot, score, reasons))

    return sorted(scored, key=lambda result: result[1], reverse=True)[:k]


def format_results(ranked: list) -> None:
    """Print one numbered line with a score and reasons per result."""
    for position, (spot, score, reasons) in enumerate(ranked, start=1):
        print(
            f"{position}. {spot['name']} -- Score: {score:.1f}"
            f" -- Because: {', '.join(reasons)}"
        )


def render_study_spot_tab():
    import streamlit as st

    st.subheader("Find a Study Spot")
    max_noise = st.selectbox("Max noise level", ["quiet", "moderate", "loud"], index=1)
    max_distance = st.slider("Max distance (miles)", 0.0, 3.0, 1.0)
    min_seats = st.number_input("Minimum seats needed", min_value=1, value=4, step=1)

    if st.button("Find spots"):
        profile = {"max_noise": max_noise, "max_distance": max_distance, "min_seats": min_seats}
        try:
            spots = load_study_spots("data/study_spots.csv")
            ranked = rank_study_spots(profile, spots, k=3)
            for spot, score, reasons in ranked:
                st.write(f"**{spot['name']}** -- Score: {score:.1f} -- Because: {', '.join(reasons)}")
        except NotImplementedError:
            st.warning("🚧 Ranking isn't implemented yet -- that's Tinker 3B's ticket.")


if __name__ == "__main__":
    spots = load_study_spots("data/study_spots.csv")
    profile = {"max_noise": "moderate", "max_distance": 1.0, "min_seats": 4}
    ranked = rank_study_spots(profile, spots, k=3)
    format_results(ranked)
