import streamlit as st
import pandas as pd
import os
def guideline_page():
    # Set subheader for the guideline page
    st.subheader("📋 Overview for Survey")

    # Provide guidelines and instructions for users to fill the survey
    st.write("👋 Thank you for participating in our Ease of Living Index survey. Your feedback is valuable to us!")
    st.write("Please take a few minutes to answer the following questions based on your experiences and opinions.")

    # Quick tips with emojis
    st.write("""
    👤 Personal Information: Name, age, sex, and city selection.

    🚍 Accessibility and Transportation: Public transportation options and ease of getting around.

    🏠 Housing and Infrastructure: Quality of housing and basic amenities.

    💊 Healthcare and Education: Availability and quality of healthcare and education.

    🔐 Safety and Security: Feeling of safety and law enforcement effectiveness.

    👥 Citizen Engagement and Governance: Information about city policies and citizen engagement.

    🌱 Environmental Sustainability: Efforts in promoting green initiatives and waste management.

    💻 Technology and Digital Services: Accessibility of digital services for public information.

    🌈 Inclusivity and Social Services: City inclusivity and support for marginalized communities.

    🌟 Quality of Life: Overall satisfaction with life and neighborhood cleanliness.

    🌪️ Natural Disaster Management: City's preparedness and early warning systems.

    🏛️ Government Services and Bureaucracy: Ease of accessing government services and experience with officials.""")
    
    st.subheader("📝 Guidelines for Ease of Living Index Survey:")
    st.write(""" 
            

            👉 Please provide your responses honestly and thoughtfully for a comprehensive evaluation.
            
            👉 Use the sliders 🎚️  to rate each aspect on a scale of 0 to 10, where 0 represents the lowest satisfaction and 10 indicates the highest satisfaction.
            
            👉 Before proceeding to the next subsection, make sure to rate all the questions in the current subsection.

            👉 Use the sliders to rate each aspect on a scale of 0 to 10, where 0 represents the lowest satisfaction and 10 indicates the highest satisfaction.

            👉 If you encounter any unanswered questions, indicated by a ⚠️ warning , kindly address them before moving forward.

            👉 Your valuable inputs will help improve the quality of life in your city 🏁.

            👉 At the end of the survey, click on the "Save" 💾 button to submit your responses.

            Thank you for participating in the Ease of Living Index Survey! 😊   
            """)

def main():
    st.title("Ease of Living Index Survey📈 and Dashboard📊")
    guideline_page()

if __name__ == "__main__":
    main()
