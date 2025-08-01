import streamlit as st
import time
import random

st.set_page_config(page_title="Chemistry Ion Detective Game", page_icon="🧪", layout="wide")

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'streak' not in st.session_state:
    st.session_state.streak = 0
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'current_mystery' not in st.session_state:
    st.session_state.current_mystery = None
if 'lives' not in st.session_state:
    st.session_state.lives = 3

# Game data
ions_data = {
    'Copper (Cu²⁺)': [
        {
            'color': 'Blue Gelatinous',
            'reagent': 'Ammonia',
            'condition': 'In drops, precipitate soluble In excess',
            'description': 'Forms beautiful blue precipitate soluble in excess',
            'emoji': '💙'
        },
        {
            'color': 'Blue Gelatinous',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, precipitate insoluble In excess',
            'description': 'Forms blue gelatinous precipitate insoluble in excess',
            'emoji': '💙'
        }
    ],
    'Aluminium (Al³⁺)': [
        {
            'color': 'White Gelatinous',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, soluble In excess',
            'description': 'White gelatinous precipitate dissolves in excess',
            'emoji': '🤍'
        },
        {
            'color': 'White Gelatinous',
            'reagent': 'Ammonia',
            'condition': 'In drops, insoluble In excess',
            'description': 'White gelatinous precipitate insoluble in excess',
            'emoji': '🤍'
        }
    ],
    'Lead (Pb²⁺)': [
        {
            'color': 'White',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, soluble In excess',
            'description': 'White precipitate dissolves in excess',
            'emoji': '🤍'
        },
        {
            'color': 'White',
            'reagent': 'Ammonia',
            'condition': 'In drops, insoluble In excess',
            'description': 'White precipitate insoluble in excess',
            'emoji': '🤍'
        }
    ],
    'Calcium (Ca²⁺)': [
        {
            'color': 'White',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, Insoluble In excess',
            'description': 'White precipitate insoluble in excess',
            'emoji': '🤍'
        },
        {
            'color': 'no precipitate',
            'reagent': 'Ammonia',
            'condition': 'In drops and In excess',
            'description': 'no precipitate in drops and in excess',
            'emoji': '🤍'
        }
    ],
    'Iron II (Fe²⁺)': [
        {
            'color': 'Green',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, Insoluble In excess',
            'description': 'Dirty Green precipitate insoluble in excess',
            'emoji': '💚'
        },
        {
            'color': 'Green',
            'reagent': 'Ammonia',
            'condition': 'In drops,then In excess',
            'description': 'Green precipitate Insoluble in excess',
            'emoji': '💚'
        }
    ],
    'Iron III (Fe³⁺)': [
        {
            'color': 'Brown',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, Insoluble In excess',
            'description': 'Brown precipitate insoluble in excess',
            'emoji': '🤎'
        },
        {
            'color': 'Brown',
            'reagent': 'Ammonia',
            'condition': 'In drops insoluble In excess',
            'description': 'Brown precipitate Insoluble in excess',
            'emoji': '🤎'
        }
    ],
    'Zinc (Zn²⁺)': [
        {
            'color': 'White Gelatinous',
            'reagent': 'Ammonia',
            'condition': 'In drops, soluble In excess',
            'description': 'White gelatinous precipitate dissolves in excess',
            'emoji': '🤍'
        },
        {
            'color': 'White Gelatinous',
            'reagent': 'Sodium hydroxide',
            'condition': 'In drops, soluble In excess',
            'description': 'White gelatinous precipitate dissolves in excess',
            'emoji': '🤍'
        }
    ],
}

def create_mystery():
    """Create a new mystery ion challenge"""
    ion = random.choice(list(ions_data.keys()))
    clue = random.choice(ions_data[ion])
    return {
        'ion': ion,
        'clues': f"🧪 **Lab Results:** {clue['emoji']} {clue['color']} precipitate with {clue['reagent']} ({clue['condition']})",
        'correct_answers': [ion]  # You can add aliases here if needed
    }

def show_animated_result(is_correct, points=0):
    """Display animated result feedback"""
    if is_correct:
        st.success(f"🎉 CORRECT! +{points} points! ⭐⭐⭐")
        st.balloons()
    else:
        st.error(f"❌ Wrong! 💔💔💔 Life lost!")

# Header with game stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("🏆 Score", st.session_state.score)
with col2:
    st.metric("📊 Level", st.session_state.level)
with col3:
    st.metric("🔥 Streak", st.session_state.streak)
with col4:
    st.metric("❤️ Lives", st.session_state.lives)

st.title("🧪 Chemistry Ion Detective Game 🕵️‍♂️")
st.markdown("**Identify the mystery ion to earn points and advance levels!**")

# Progress bar with animated colors
progress = (st.session_state.score % 100) / 100
st.progress(progress, f"Progress to Level {st.session_state.level + 1}")

# Visual feedback for streak
if st.session_state.streak > 0:
    streak_emojis = "🔥" * min(st.session_state.streak, 10)
    st.markdown(f"**Streak Bonus:** {streak_emojis}")

# Visual feedback for lives
if st.session_state.lives <= 1:
    st.warning("⚠️ Low on lives! Be careful!")
elif st.session_state.lives == 2:
    st.info("💛 You have 2 lives remaining")

# Sidebar with ion reference
with st.sidebar:
    st.markdown("### 🔬 Ion Reference Guide")
    for ion, clues in ions_data.items():
        for clue in clues:
            with st.expander(f"{clue['emoji']} {ion} ({clue['reagent']})"):
                st.write(f"**Color:** {clue['color']}")
                st.write(f"**Reagent:** {clue['reagent']}")
                st.write(f"**Condition:** {clue['condition']}")
                st.write(f"**Description:** {clue['description']}")

    st.markdown("### 🎮 Game Tips")
    st.markdown("- Higher levels = more points per correct answer")
    st.markdown("- Streaks multiply your score")
    st.markdown("- Use the reference guide to study")
    st.markdown("- Take your time - accuracy matters!")

# Main game logic
if not st.session_state.game_started:
    st.markdown("### 🎮 Welcome Detective!")
    st.markdown("**How to Play:**")
    st.markdown("- 🔍 Analyze lab results to identify mystery ions")
    st.markdown("- 🎯 Correct answers earn points and increase your streak")
    st.markdown("- 📈 Reach 100 points to advance to the next level")
    st.markdown("- ❤️ You have 3 lives - don't waste them!")
    
    if st.button("🚀 Start Investigation!", type="primary"):
        st.session_state.game_started = True
        st.session_state.current_mystery = create_mystery()
        st.rerun()

else:
    if st.session_state.lives <= 0:
        st.error("🎮 Game Over! You've run out of lives!")
        st.markdown(f"**Final Score:** {st.session_state.score}")
        st.markdown(f"**Level Reached:** {st.session_state.level}")
        
        if st.button("🔄 Play Again"):
            # Reset game
            st.session_state.score = 0
            st.session_state.level = 1
            st.session_state.streak = 0
            st.session_state.lives = 3
            st.session_state.current_mystery = create_mystery()
            st.rerun()
    
    else:
        if st.session_state.current_mystery is None:
            st.session_state.current_mystery = create_mystery()
        
        mystery = st.session_state.current_mystery
        
        # Display mystery with animation
        st.markdown("### 🔍 Mystery Ion Analysis")
        mystery_container = st.container()
        with mystery_container:
            st.markdown(mystery['clues'])
        
        # Answer options
        st.markdown("### 🎯 Your Identification:")
        answer = st.selectbox(
            "Which ion matches these lab results?",
            options=list(ions_data.keys()),
            key=f"answer_{st.session_state.score}"
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔬 Submit Analysis", type="primary"):
                if answer in mystery['correct_answers']:
                    # Correct answer
                    points = 10 + (st.session_state.level * 5) + (st.session_state.streak * 2)
                    st.session_state.score += points
                    st.session_state.streak += 1
                    
                    show_animated_result(True, points)
                    
                    # Level up check
                    if st.session_state.score >= st.session_state.level * 100:
                        st.session_state.level += 1
                        st.balloons()
                        st.success(f"🎉 LEVEL UP! Welcome to Level {st.session_state.level}!")
                        st.snow()  # Additional celebration effect
                    
                    # Generate new mystery
                    st.session_state.current_mystery = create_mystery()
                    st.rerun()
                    
                else:
                    # Wrong answer
                    st.session_state.lives -= 1
                    st.session_state.streak = 0
                    
                    show_animated_result(False)
                    
                    # Show correct answer
                    correct_ion = mystery['correct_answers'][0]  # Fixed: use correct_answers instead of correct_answer
                    st.info(f"💡 The correct answer was: **{correct_ion}**")
                    
                    # Generate new mystery
                    st.session_state.current_mystery = create_mystery()
                    st.rerun()
        
        with col2:
            if st.button("🔄 New Mystery"):
                st.session_state.current_mystery = create_mystery()
                st.rerun()

