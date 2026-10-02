import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="FitBuddy - AI Fitness Planner", 
    page_icon="🏋️️‍♂️", 
    layout="wide"
)

# Custom Light Theme CSS Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #dee2e6;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ff4b4b;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #6c757d;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e03e3e;
        color: white;
    }
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div {
        background-color: #ffffff;
        color: #212529;
        border-color: #ced4da;
    }
    [data-testid="stMetricValue"] {
        color: #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-title">🏋️‍♂️ FitBuddy: AI Fitness Plan Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your personal AI-powered workout and diet companion.</p>', unsafe_allow_html=True)

st.divider()

# --- SIDEBAR INPUTS ---
st.sidebar.header("👤 Personal Profile")

name = st.sidebar.text_input("Your Name", value="")
gender = st.sidebar.selectbox("Gender", ["Select Gender", "Male", "Female", "Other"], index=0)
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=10, step=1)

st.sidebar.header("📏 Body Metrics")
height = st.sidebar.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=100.0, step=0.5)
weight = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=30.0, step=0.5)

st.sidebar.header("🎯 Goals & Preferences")
goal = st.sidebar.selectbox("Fitness Goal", ["Select Goal", "Weight Loss", "Muscle Gain", "General Fitness"], index=0)
activity_level = st.sidebar.selectbox("Activity Level", ["Select Activity Level", "Sedentary", "Lightly Active", "Very Active"], index=0)
diet_pref = st.sidebar.selectbox("Diet Preference", ["Select Diet Preference", "Vegetarian", "Non-Vegetarian", "Vegan"], index=0)

# --- MAIN CONTENT AREA ---
col1, col2 = st.columns([1, 2])

with col1:
    st.info("💡 **Tips for Best Results:**\n\nPlease fill out your profile details on the sidebar so FitBuddy can tailor your customized routine properly!")

with col2:
    st.write("")
    st.write("")
    generate_btn = st.button("🚀 Generate My Custom Fitness Plan")

if generate_btn:
    # Validation check for dropdown selections
    if not name or gender == "Select Gender" or goal == "Select Goal" or activity_level == "Select Activity Level" or diet_pref == "Select Diet Preference":
        st.error("⚠️ Please fill in your name and select all your dropdown options properly on the sidebar before generating!")
    else:
        st.success(f"🎉 Success! Here is the personalized plan for **{name}** ({gender}, {age} yrs):")
        
        # Quick metrics display
        m1, m2, m3 = st.columns(3)
        m1.metric("Target Goal", goal)
        m2.metric("Diet Preference", diet_pref)
        m3.metric("Activity Level", activity_level)
        
        st.divider()
        
        # Two-column layout for Workout and Diet
        col_w, col_d = st.columns(2)
        
        with col_w:
            st.subheader("🏋️‍♂️ Weekly Workout Routine")
            st.markdown(f"""
            - **Monday / Thursday:** Cardio & Core (30 mins Running/Cycling + Planks tailored for **{goal.lower()}**)
            - **Tuesday / Friday:** Strength Training (Bodyweight squats, Push-ups, Dumbbell rows)
            - **Wednesday / Saturday:** Active Recovery & Yoga/Stretching
            - **Sunday:** Rest Day & Muscle Repair
            """)
            
        with col_d:
            st.subheader("🥗 Customized Diet Chart")
            if diet_pref == "Vegetarian":
                st.markdown("""
                - **Breakfast:** Oats with nuts and fruit + Protein Smoothie
                - **Lunch:** Brown rice, Lentils (Dal), Mixed vegetable curry, and Salad
                - **Snacks:** Roasted Chana or Green Tea with Almonds
                - **Dinner:** Paneer / Tofu with sautéed vegetables and Roti
                """)
            elif diet_pref == "Non-Vegetarian":
                st.markdown("""
                - **Breakfast:** 3 Egg whites + Whole wheat toast + Fruit
                - **Lunch:** Grilled Chicken breast, Quinoa/Brown rice, and Green veggies
                - **Snacks:** Boiled eggs or Protein Shake
                - **Dinner:** Baked Fish or Chicken salad with soup
                """)
            else: # Vegan
                st.markdown("""
                - **Breakfast:** Chia pudding with almond milk and berries
                - **Lunch:** Chickpea salad with veggies and avocado
                - **Snacks:** Mixed seeds and Green Tea
                - **Dinner:** Lentil soup with tofu and steamed broccoli
                """)

        st.divider()
        
        # --- 7-DAY FEEDBACK & DRAWBACK ANALYSIS ---
        st.subheader("📊 7-Day Progress & Drawback Check-in")
        st.write("Finished your first week of workouts? Let us review how it went and identify any bottlenecks or drawbacks.")
        
        with st.form("feedback_form"):
            energy_level = st.select_slider(
                "How were your energy levels throughout the week?",
                options=["Very Low 📉", "Low", "Moderate ⚡", "High", "Peak Performance 🔥"],
                value="Moderate ⚡"
            )
            
            drawbacks = st.multiselect(
                "Did you face any of these drawbacks or challenges?",
                [
                    "All Good / Smooth Sailing 🎉",
                    "Muscle soreness was too intense",
                    "Diet plan felt too restrictive or hard to follow",
                    "Not enough time to complete the workouts",
                    "Experienced fatigue or lack of sleep",
                    "Hungry too often between meals"
                ]
            )
            
            user_notes = st.text_area("Any specific feedback or changes you'd like to make?")
            
            submit_feedback = st.form_submit_button("Submit Week 1 Feedback")
            
            if submit_feedback:
                st.success("✅ Feedback recorded! Here is your AI Coach adjustment for Week 2:")
                
                if "All Good / Smooth Sailing 🎉" in drawbacks:
                    st.info("🌟 Fantastic! Everything is going smoothly. Keep up the exact same momentum for Week 2!")
                elif drawbacks:
                    st.warning("⚠️ **Identified Drawbacks & Adjustments:**")
                    for d in drawbacks:
                        if "soreness" in d.lower():
                            st.write(f"- *{d}:* **Adjustment:** Increase rest days or switch Wednesday/Saturday to lighter stretching.")
                        elif "diet" in d.lower() or "hungry" in d.lower():
                            st.write(f"- *{d}:* **Adjustment:** Add a healthy afternoon mid-snack to boost daily calories and curb cravings.")
                        elif "time" in d.lower():
                            st.write(f"- *{d}:* **Adjustment:** Compress workouts into high-intensity 20-minute HIIT circuits.")
                        else:
                            st.write(f"- *{d}:* **Adjustment:** Prioritize 7-8 hours of sleep and hydration.")
                else:
                    st.info("🌟 Feedback submitted successfully! Keep up the great work.")