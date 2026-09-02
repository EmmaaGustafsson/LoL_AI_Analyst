import streamlit as st
import pandas as pd
import joblib

from pathlib import Path


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="League of Legends AI Analyst",
    page_icon="🎮",
    layout="wide"
)


# --------------------------------------------------
# Load trained model and scaler
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Title and project description
# --------------------------------------------------

st.title("🎮 League of Legends AI Analyst")

st.write(
    """
    Can we predict the winner of a League of Legends match
    using only information available after 10 minutes?
    """
)

st.info(
    "Enter the game state at 10 minutes to see the model's prediction."
)


# --------------------------------------------------
# Input sections
# --------------------------------------------------

st.header("📊 Match information at 10 minutes")


# --------------------------------------------------
# Economy
# --------------------------------------------------

st.subheader("💰 Economy")

col1, col2, col3 = st.columns(3)

with col1:
    gold_diff = st.number_input(
    "Gold Difference",
    min_value=-12500,
    max_value=12500,
    value=0,
    step=100
)

with col2:
    exp_diff = st.number_input(
    "Experience Difference",
    min_value=-10500,
    max_value=10500,
    value=0,
    step=100
)

with col3:
    champ_level_diff = st.number_input(
    "Champion Level Difference",
    min_value=-3.4,
    max_value=3.4,
    value=0.0,
    step=0.1
)


# --------------------------------------------------
# Combat
# --------------------------------------------------

st.subheader("⚔️ Combat")

col1, col2, col3 = st.columns(3)

with col1:
    kills = st.number_input(
        "Kills",
        min_value=0,
        max_value=32,
        value=0,
        step=1
    )

with col2:
    deaths = st.number_input(
        "Deaths",
        min_value=0,
        max_value=21,
        value=0,
        step=1
    )

with col3:
    assists = st.number_input(
        "Assists",
        min_value=0,
        max_value=48,
        value=0,
        step=1
    )


# --------------------------------------------------
# Early objectives
# --------------------------------------------------

st.subheader("🏆 Early Objectives")

col1, col2 = st.columns(2)

with col1:
    is_first_blood = st.selectbox(
        "First Blood",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

with col2:
    is_first_tower = st.selectbox(
        "First Tower",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )


# --------------------------------------------------
# Drakes
# --------------------------------------------------

st.subheader("🐉 Dragons")

col1, col2, col3, col4 = st.columns(4)

with col1:
    killed_fire_drake = st.number_input(
    "Infernal Drake",
    min_value=0,
    max_value=1,
    value=0,
    step=1
)

with col2:
    killed_water_drake = st.number_input(
        "Ocean Drake",
        min_value=0,
        max_value=1,
        value=0,
        step=1
    )

with col3:
    killed_air_drake = st.number_input(
        "Cloud Drake",
        min_value=0,
        max_value=1,
        value=0,
        step=1
    )

with col4:
    killed_earth_drake = st.number_input(
        "Mountain Drake",
        min_value=0,
        max_value=1,
        value=0,
        step=1
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    lost_fire_drake = st.number_input(
        "Infernal Drakes Lost",
        min_value=0,
        max_value=1,
        value=0
)

with col2:
    lost_water_drake = st.number_input(
        "Ocean Drakes Lost",
        min_value=0,
        max_value=1,
        value=0
)

with col3:
    lost_air_drake = st.number_input(
        "Cloud Drakes Lost",
        min_value=0,
        max_value=1,
        value=0
)

with col4:
    lost_earth_drake = st.number_input(
        "Mountain Drakes Lost",
        min_value=0,
        max_value=1,
        value=0
)

# --------------------------------------------------
# Major objectives
# --------------------------------------------------

st.subheader("🎯 Rift Herald")

col1, col2 = st.columns(2)
with col1:
    killed_rift_herald = st.number_input(
        "Rift Heralds Killed",
        min_value=0,
        max_value=1,
        value=0
)

with col2:
    lost_rift_herald = st.number_input(
        "Rift Heralds Lost",
        min_value=0,
        max_value=1,
        value=0
)

# --------------------------------------------------
# Vision
# --------------------------------------------------

st.subheader("👁️ Vision")

col1, col2, col3 = st.columns(3)

with col1:
    wards_placed = st.number_input(
        "Wards Placed",
        min_value=0,
        value=0,
        step=1
    )

with col2:
    wards_destroyed = st.number_input(
        "Wards Destroyed",
        min_value=0,
        value=0,
        step=1
    )

with col3:
    wards_lost = st.number_input(
        "Wards Lost",
        min_value=0,
        value=0,
        step=1
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

analyze = st.button(
    "🔮 Analyze Match",
    use_container_width=True
)


if analyze:

    # --------------------------------------------------
    # Create input data
    # --------------------------------------------------

    input_data = {
        "goldDiff": gold_diff,
        "expDiff": exp_diff,
        "champLevelDiff": champ_level_diff,

        "isFirstTower": is_first_tower,
        "isFirstBlood": is_first_blood,

        "killedFireDrake": killed_fire_drake,
        "killedWaterDrake": killed_water_drake,
        "killedAirDrake": killed_air_drake,
        "killedEarthDrake": killed_earth_drake,
        "killedElderDrake": 0,

        "lostFireDrake": lost_fire_drake,
        "lostWaterDrake": lost_water_drake,
        "lostAirDrake": lost_air_drake,
        "lostEarthDrake": lost_earth_drake,
        "lostElderDrake": 0,

        "killedBaronNashor": 0,
        "lostBaronNashor": 0,

        "killedRiftHerald": killed_rift_herald,
        "lostRiftHerald": lost_rift_herald,

        # Cannot realistically occur at 10 minutes
        "destroyedTopInhibitor": 0,
        "destroyedMidInhibitor": 0,
        "destroyedBotInhibitor": 0,

        "lostTopInhibitor": 0,
        "lostMidInhibitor": 0,
        "lostBotInhibitor": 0,

        "destroyedTopNexusTurret": 0,
        "destroyedMidNexusTurret": 0,
        "destroyedBotNexusTurret": 0,

        "lostTopNexusTurret": 0,
        "lostMidNexusTurret": 0,
        "lostBotNexusTurret": 0,

        "destroyedTopBaseTurret": 0,
        "destroyedMidBaseTurret": 0,
        "destroyedBotBaseTurret": 0,

        "lostTopBaseTurret": 0,
        "lostMidBaseTurret": 0,
        "lostBotBaseTurret": 0,

        "destroyedTopInnerTurret": 0,
        "destroyedMidInnerTurret": 0,
        "destroyedBotInnerTurret": 0,

        "lostTopInnerTurret": 0,
        "lostMidInnerTurret": 0,
        "lostBotInnerTurret": 0,

        "destroyedTopOuterTurret": 0,
        "destroyedMidOuterTurret": 0,
        "destroyedBotOuterTurret": 0,

        "lostTopOuterTurret": 0,
        "lostMidOuterTurret": 0,
        "lostBotOuterTurret": 0,

        "kills": kills,
        "deaths": deaths,
        "assists": assists,

        "wardsPlaced": wards_placed,
        "wardsDestroyed": wards_destroyed,
        "wardsLost": wards_lost
    }


    # --------------------------------------------------
    # Convert input to DataFrame
    # --------------------------------------------------

    input_df = pd.DataFrame([input_data])


    # --------------------------------------------------
    # Check feature order
    # --------------------------------------------------

    expected_features = pd.read_csv(
        BASE_DIR / "data" / "processed" / "X_train.csv",
        nrows=0
    ).columns.tolist()

    if input_df.columns.tolist() != expected_features:

        st.error(
            "Feature order does not match the features used during training."
        )

        st.write("Expected features:")
        st.write(expected_features)

        st.write("Input features:")
        st.write(input_df.columns.tolist())

        st.stop()


    # --------------------------------------------------
    # Make prediction
    # --------------------------------------------------

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0]

    win_probability = probability[1]
    loss_probability = probability[0]


    # --------------------------------------------------
    # Display prediction
    # --------------------------------------------------

    st.header("🔮 Prediction")

    if prediction == 1:

        st.success(
            "🏆 Predicted Winner: WIN"
        )

    else:

        st.error(
            "💀 Predicted Winner: LOSS"
        )


    # --------------------------------------------------
    # Display probabilities
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Win Probability",
            f"{win_probability:.1%}"
        )

    with col2:

        st.metric(
            "Loss Probability",
            f"{loss_probability:.1%}"
        )


    # --------------------------------------------------
    # Analyst interpretation
    # --------------------------------------------------

    if win_probability >= 0.75:

        st.info(
            "The model predicts a strong advantage for this team."
        )

    elif win_probability >= 0.55:

        st.info(
            "The model predicts a moderate advantage for this team."
        )

    elif win_probability > 0.45:

        st.warning(
            "The model predicts the match as relatively even."
        )

    else:

        st.warning(
            "The model predicts an advantage for the opposing team."
        )
# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Prediction is based only on information available "
    "at approximately 10 minutes into the match."
)
