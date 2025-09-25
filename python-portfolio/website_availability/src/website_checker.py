import streamlit as st
import requests


# Function to format URL to include "https://www."
def format_url(url):
    # Remove http:// or https:// if present
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]

    # Remove www. if present
    if url.startswith('www.'):
        url = url[len('www.'):]

    # Prepend https://www. to ensure consistency
    formatted_url = 'https://www.' + url
    return formatted_url


# Function to check website availability
def check_site_availability(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, timeout=5, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


# Streamlit UI
def main():
    # Page config
    st.set_page_config(
        page_title="🌐 Site Monitor Pro",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Main header
    st.title("🌐 Site Monitor Pro")
    st.subheader("🚀 Monitor your favorite websites in real-time!")
    
    # Session state initialization
    if 'urls' not in st.session_state:
        st.session_state.urls = []
    if 'checking' not in st.session_state:
        st.session_state.checking = False

    # Stats dashboard
    if st.session_state.urls:
        st.subheader("📊 Dashboard Stats")
        col1, col2, col3, col4 = st.columns(4)
        total_urls = len(st.session_state.urls)
        checked_urls = sum(1 for i in range(total_urls) if f"status_{i}" in st.session_state)
        up_sites = sum(1 for i in range(total_urls) if st.session_state.get(f"status_{i}") == True)
        down_sites = checked_urls - up_sites
        
        with col1:
            st.metric("Total Sites", total_urls)
        with col2:
            st.metric("Checked", checked_urls)
        with col3:
            st.metric("🟢 Online", up_sites)
        with col4:
            st.metric("🔴 Offline", down_sites)
        
        st.divider()

    # URL input form
    with st.form("url_form", clear_on_submit=True):
        st.subheader("📝 Add New Website")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            new_url = st.text_input(
                "Enter website URL:", 
                placeholder="e.g., google.com, github.com, stackoverflow.com",
                help="Enter any website URL - we'll format it properly!"
            )
        
        with col2:
            st.write("")  # spacing
            add_clicked = st.form_submit_button("🎯 Add Site", use_container_width=True)
        
        if add_clicked and new_url:
            formatted_url = format_url(new_url)
            if formatted_url not in st.session_state.urls:
                st.session_state.urls.append(formatted_url)
                st.success(f"🎉 Added **{formatted_url}** to monitoring list!")
                st.balloons()
            else:
                st.warning(f"⚠️ **{formatted_url}** is already in your list!")

    # Action buttons
    if st.session_state.urls:
        st.subheader("🎮 Control Panel")
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            if st.button("🔍 Check All Sites", type="primary", use_container_width=True):
                st.session_state.checking = True
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for idx, url in enumerate(st.session_state.urls):
                    status_text.text(f"Checking {url}...")
                    progress_bar.progress((idx + 1) / len(st.session_state.urls))
                    st.session_state[f"status_{idx}"] = check_site_availability(url)
                
                status_text.text("✅ All sites checked!")
                st.session_state.checking = False
                st.success("🎊 Health check complete!")
                
        with col2:
            if st.button("🔄 Refresh All", use_container_width=True):
                # Clear all status and recheck
                for idx in range(len(st.session_state.urls)):
                    if f"status_{idx}" in st.session_state:
                        del st.session_state[f"status_{idx}"]
                st.info("🔄 Status cleared! Click 'Check All Sites' to refresh.")
                
        with col3:
            if st.button("🗑️ Clear List", use_container_width=True):
                st.session_state.urls.clear()
                # Clear all status data
                for key in list(st.session_state.keys()):
                    if key.startswith("status_"):
                        del st.session_state[key]
                st.info("🧹 List cleared!")

    # Display websites
    if st.session_state.urls:
        st.subheader("🌐 Website Status")
        
        for idx, url in enumerate(st.session_state.urls):
            col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
            
            with col1:
                st.write(f"**{url}**")
            
            with col2:
                if f"status_{idx}" in st.session_state:
                    if st.session_state[f"status_{idx}"]:
                        st.success("🟢 UP")
                    else:
                        st.error("🔴 DOWN")
                else:
                    st.info("⭕ Not checked")
            
            with col3:
                if st.button("🔍", key=f"check_{idx}", help="Check this site only"):
                    with st.spinner(f"Checking {url}..."):
                        st.session_state[f"status_{idx}"] = check_site_availability(url)
                    st.rerun()
            
            with col4:
                if st.button("🗑️", key=f"remove_{idx}", help="Remove this site"):
                    st.session_state.urls.pop(idx)
                    # Clean up status
                    if f"status_{idx}" in st.session_state:
                        del st.session_state[f"status_{idx}"]
                    st.rerun()
    
    else:
        # Empty state
        st.divider()
        st.info("🌟 Ready to Monitor Some Websites?")
        st.write("Add your first website above to get started!")
        st.write("Popular sites to try: `google.com`, `github.com`, `stackoverflow.com`")

if __name__ == "__main__":
    main()