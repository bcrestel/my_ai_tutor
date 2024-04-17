import streamlit as st

def main():
    st.title("Word Display App")
    
    # Define a list of words
    word_list = ["Hello", "World", "Streamlit", "Example", "App"]
    
    # Initialize session_state and set word_index to 0 if it doesn't exist
    if 'word_index' not in st.session_state:
        st.session_state.word_index = 0
    
    # Create a text element to display the current word
    word_display = st.empty()
    
    # Create a "Next" button
    next_button = st.button("Next")
    if next_button:
        st.session_state.word_index += 1
        st.session_state.word_index = min(st.session_state.word_index, len(word_list)-1)

    word = word_list[st.session_state.word_index]
    word_display.text(word)
    


if __name__ == "__main__":
    main()
