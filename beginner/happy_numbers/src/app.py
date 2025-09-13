import streamlit as st
from happy_numbers import is_happy

# Page configuration
st.set_page_config(
    page_title="Happy Numbers Checker",
    page_icon="😊",
    layout="centered"
)

# Header
st.title(":laughing: Happy Numbers Checker")
st.markdown("**See if your number is happy!** A happy number is one that eventually reaches 1 when you repeatedly sum the squares of its digits.")

# Sidebar for additional info
with st.sidebar:
    st.header("ℹ️ About Happy Numbers")
    st.markdown("""
    A happy number is defined by this process:
    1. Start with any positive integer
    2. Replace it with the sum of squares of its digits
    3. Repeat until you get 1 (happy) or enter a cycle (unhappy)
    
    **Examples:**
    - 19 → 1² + 9² = 82 → 8² + 2² = 68 → ... → 1 ✅
    - 2 → 2² = 4 → 4² = 16 → 1² + 6² = 37 → ... → cycle ❌
    """)

# Main input
col1, col2 = st.columns([2, 1])
with col1:
    number = st.number_input(
        "Enter a number to check:",
        min_value=1,
        max_value=999999,
        value=19,
        step=1
            )

with col2:
    if st.button("🔍 Check Number", type="primary", use_container_width=True):
        pass

# Check if number is happy
if number:
    # Add some visual feedback
    with st.spinner("Calculating..."):
        result = is_happy(number)
    
    # Display result with beautiful formatting
    if result:
        st.success("🎉 **This number is HAPPY!** 🎉")
        st.balloons()
        st.markdown(f"**{number}** will eventually reach 1 when you sum the squares of its digits!")
    else:
        st.error(":cry: **This number is NOT happy**")
        st.markdown(f"**{number}** will get stuck in a cycle and never reach 1.")
    
    # Show the process for educational purposes
    if st.checkbox("Show the calculation process"):
        st.subheader("📊 Calculation Process")
        process_text = f"Starting with {number}:"
        st.write(process_text)
        
        # Show the process
        seen = set()
        current = number
        step = 1
        
        while current != 1 and current not in seen:
            seen.add(current)
            digits = [int(d) for d in str(current)]
            squares = [d**2 for d in digits]
            next_num = sum(squares)
            
            st.write(f"Step {step}: {current} → {digits} → {squares} → {next_num}")
            current = next_num
            step += 1
        
        if current == 1:
            st.write(f"Step {step}: {current} → **HAPPY!** 🎉")
        else:
            st.write(f"Step {step}: {current} → **Cycle detected!** 🔄")

# Footer
st.markdown("---")
