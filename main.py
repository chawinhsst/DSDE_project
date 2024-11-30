import streamlit as st
import json

# Load sample data
with open("sample_data.json", "r") as f:
    sample_data = json.load(f)

# Sidebar with button navigation
st.sidebar.title("Navigation")
search_button = st.sidebar.button("Search Page")
chart_button = st.sidebar.button("Chart Page")

if search_button:
    selection = "Search"
elif chart_button:
    selection = "Chart"
else:
    selection = "Search"  # Default page

# Search Page
if selection == "Search":
    st.title("Search Academic Papers")
    search_keyword = st.text_input("Enter keyword(s):", "")
    search_button = st.button("Search")

    if search_button and search_keyword:
        st.write(f"Searching for: {search_keyword}")
        results = [
            item for item in sample_data
            if search_keyword.lower() in item["title"].lower() or search_keyword.lower() in item["abstract"].lower()
        ]

        if results:
            st.success(f"Found {len(results)} result(s):")
            for item in results:
                st.markdown(f"**Title**: {item['title']}")
                st.markdown(f"**Abstract**: {item['abstract']}")
                st.markdown("---")
        else:
            st.warning("No results found.")

# Chart Page
elif selection == "Chart":
    st.title("Visualization of Analysis")
    st.write("Charts will be displayed here.")
    st.write("Coming soon!")
