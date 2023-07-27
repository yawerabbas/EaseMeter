import streamlit as st
import pandas as pd
import os

cities = [
    "Select a city",
    "Bhubaneswar",
    "Pune",
    "Jaipur",
    "Surat",
    "Kochi",
    "Ahmedabad",
    "Jabalpur",
    "Visakhapatnam",
    "Solapur",
    "Davanagere",
    "Indore",
    "NDMC",
    "Coimbatore",
    "Kakinada",
    "Belagavi",
    "Udaipur",
    "Guwahati",
    "Chennai",
    "Ludhiana",
    "Bhopal",
    "Noida"
]   

def calculate_total_score():
    global total_score  # Access the global total_score variable
    total_score = (
        accessibility_transportation_1 + accessibility_transportation_2 + accessibility_transportation_3 +
        housing_infrastructure_1 + housing_infrastructure_2 +
        healthcare_education_1 + healthcare_education_2 +
        safety_security_1 + safety_security_2 +
        citizen_governance_1 + citizen_governance_2 +
        environmental_sustainability_1 + environmental_sustainability_2 +
        technology_digital_services_1 + technology_digital_services_2 +
        inclusivity_social_services_1 + inclusivity_social_services_2 +
        quality_of_life_1 + quality_of_life_2 +
        natural_disaster_1 + natural_disaster_2 +
        government_services_1 + government_services_2 +
        community_safety_1 + community_safety_2 +
        cultural_recreational_1 + cultural_recreational_2 +
        employment_economic_1 + employment_economic_2 +
        quality_affordability_housing_1 + quality_affordability_housing_2 +
        public_health_healthcare_1 + public_health_healthcare_2 +
        financial_inclusion_banking_1 + financial_inclusion_banking_2 +
        public_spaces_community_1 + public_spaces_community_2 +
        traffic_management_commute_1 + traffic_management_commute_2 +
        water_quality_services_1 + water_quality_services_2
    )
    return total_score

def save_to_csv(data):
    # Check if the CSV file exists or not
    try:
        existing_data = pd.read_csv('database.csv')
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    # Append the new data to the existing data
    updated_data = pd.concat([existing_data, pd.DataFrame(data)])

    # Save the updated data to the CSV file
    updated_data.to_csv('database.csv', index=False)
def survey_section():
     # Initialize all survey parameters with a value of 0
    global accessibility_transportation_1
    global accessibility_transportation_2
    global accessibility_transportation_3 
    global housing_infrastructure_1 
    global housing_infrastructure_2 
    global healthcare_education_1 
    global healthcare_education_2 
    global safety_security_1 
    global safety_security_2 
    global citizen_governance_1 
    global citizen_governance_2 
    global environmental_sustainability_1 
    global environmental_sustainability_2 
    global technology_digital_services_1 
    global technology_digital_services_2 
    global inclusivity_social_services_1 
    global inclusivity_social_services_2 
    global quality_of_life_1 
    global quality_of_life_2 
    global natural_disaster_1 
    global natural_disaster_2 
    global government_services_1 
    global government_services_2 
    global community_safety_1 
    global community_safety_2 
    global cultural_recreational_1 
    global cultural_recreational_2 
    global employment_economic_1 
    global employment_economic_2 
    global quality_affordability_housing_1 
    global quality_affordability_housing_2 
    global public_health_healthcare_1
    global public_health_healthcare_2
    global financial_inclusion_banking_1 
    global financial_inclusion_banking_2 
    global public_spaces_community_1 
    global public_spaces_community_2 
    global traffic_management_commute_1 
    global traffic_management_commute_2 
    global water_quality_services_1 
    global water_quality_services_2 
    st.subheader("Survey")
    # Get user information
    name = st.text_input("Name", "")
    age = st.number_input("Age", min_value=0, max_value=150, value=25)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    smart_city = st.selectbox("Select Smart City:", cities)
    # Check if a city is selected or not
    if smart_city == "Select a city":
        st.error("Please select a city from the drop-down menu.")
        return

    # Additional Questions
    st.subheader("Accessibility and Transportation:")
    # Add more questions here using appropriate widgets
    accessibility_transportation_1 = st.slider("How satisfied are you with the accessibility of public transportation options in City?", 0, 10, 0)
    accessibility_transportation_2 = st.slider("Rate the ease of getting around the city by different modes of transport (bus, metro, auto-rickshaw, etc.)", 0, 10, 0)
    accessibility_transportation_3 = st.slider("Do you feel the city is pedestrian-friendly and has adequate sidewalks and pedestrian crossings?", 0, 10, 0)
     # Check if all sliders in the subsection have been interacted with
    if accessibility_transportation_1 == 0 and accessibility_transportation_2 == 0 and accessibility_transportation_3 == 0:
        st.warning("Please answer all questions in the Accessibility and Transportation section.")
        return
    

    st.subheader("Housing and Infrastructure:")
    # Add more questions here using appropriate widgets
    housing_infrastructure_1 = st.slider("Rate the quality of housing infrastructure and availability of basic amenities like water, electricity, and sanitation.", 0, 10, 0)
    housing_infrastructure_2 = st.slider("How satisfied are you with the condition of roads, public spaces, and urban infrastructure in your neighborhood?", 0, 10, 0)
    if housing_infrastructure_1 == 0 and housing_infrastructure_2 == 0:
        st.warning("Please answer all questions in the Housing and Infrastructure section.")
        return

    st.subheader("Healthcare and Education:")
    # Add more questions here using appropriate widgets
    healthcare_education_1 = st.slider("Rate the availability and quality of healthcare facilities in City.", 0, 10, 0)
    healthcare_education_2 = st.slider("How satisfied are you with the standard of education and access to educational institutions in the city?", 0, 10, 0)
    if healthcare_education_1 == 0 and healthcare_education_2 == 0:
        st.warning("Please answer all questions in the Healthcare and Education section.")
        return

    st.subheader("Safety and Security:")
    # Add more questions here using appropriate widgets
    safety_security_1 = st.slider("How safe do you feel in City during the day and at night?", 0, 10, 0)
    safety_security_2 = st.slider("Rate the effectiveness of law enforcement and emergency services in the city.", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if safety_security_1 == 0 and safety_security_2 == 0:
        st.warning("Please answer all questions in the Safety and Security section.")
        return
    
    st.subheader("Citizen Engagement and Governance:")
    # Add more questions here using appropriate widgets
    citizen_governance_1 = st.slider("How informed do you feel about the city's policies, programs, and initiatives?", 0, 10, 0)
    citizen_governance_2 = st.slider("How much is your participation in any citizen engagement activities or community events in City?",0 ,10 , 0)
    # Check if all sliders in the subsection have been interacted with
    if citizen_governance_1 ==0 and citizen_governance_2 == 0:
        st.warning("Please answer all questions in the Citizen Engagement and Governance section.")
        return

    st.subheader("Environmental Sustainability:")
    # Add more questions here using appropriate widgets
    environmental_sustainability_1 = st.slider("Rate the efforts made by the city to promote environmental sustainability and green initiatives.", 0, 10, 0)
    environmental_sustainability_2 = st.slider("Are you satisfied with waste management practices and green spaces in City?", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if environmental_sustainability_1 == 0 and environmental_sustainability_2 == 0:
        st.warning("Please answer all questions in the Environmental Sustainability section.")
        return



    st.subheader("Technology and Digital Services:")
    # Add more questions here using appropriate widgets
    technology_digital_services_1 = st.slider("Rate the availability and accessibility of digital services for accessing public information and city services.", 0, 10, 0)
    technology_digital_services_2 = st.slider("How well-connected do you feel with the city's digital infrastructure, such as public Wi-Fi and online services?", 0, 10, 0)
     # Check if all sliders in the subsection have been interacted with
    if technology_digital_services_1 == 0 and technology_digital_services_2 == 0:
        st.warning("Please answer all questions in the Technology and Digital Services section.")
        return


    st.subheader("Inclusivity and Social Services:")
    # Add more questions here using appropriate widgets
    inclusivity_social_services_1 = st.slider("How much you feel that City is inclusive and provides equal opportunities for all residents?",0,10,0)
    inclusivity_social_services_2 = st.slider("Rate the availability of social services and support systems for marginalized communities.", 0, 10, 0)
     # Check if all sliders in the subsection have been interacted with
    if not inclusivity_social_services_1 and inclusivity_social_services_2 == 0:
        st.warning("Please answer all questions in the Inclusivity and Social Services section.")
        return


    st.subheader("Quality of Life:")
    # Add more questions here using appropriate widgets
    quality_of_life_1 = st.slider("Overall, how satisfied are you with your quality of life in City as a resident?", 0, 10, 0)
    quality_of_life_2 = st.slider("On a scale of 1-10, how satisfied are you with the overall cleanliness and sanitation in your neighborhood?", 0,10,0)
    # Check if all sliders in the subsection have been interacted with
    if quality_of_life_1 == 0 and quality_of_life_2:
        st.warning("Please answer all questions in the Quality of Life section.")
        return


    st.subheader("Natural Disaster Management:")
    # Add more questions here using appropriate widgets
    natural_disaster_1 = st.slider("How confident are you in the city's preparedness and response to natural disasters (floods, earthquakes, etc.)?", 0, 10, 0)
    natural_disaster_2 = st.slider("Rate the effectiveness of early warning systems and evacuation procedures during emergencies.", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if natural_disaster_1 == 0 and natural_disaster_2 == 0:
        st.warning("Please answer all questions in the Natural Disaster Management section.")
        return


    st.subheader("Government Services and Bureaucracy:")
    # Add more questions here using appropriate widgets
    government_services_1 = st.slider("How easy is it to access and navigate government services (online and offline) for various administrative tasks?", 0, 10, 0)
    government_services_2 = st.slider("Rate your experience with government officials and the efficiency of bureaucratic processes.", 0, 10, 0)
    if government_services_1 == 0 and government_services_2 == 0:
        st.warning("Please answer all questions in the Government Services and Bureaucracy section.")
        return



    st.subheader("Community Safety and Neighborhood Cohesion:")
    # Add more questions here using appropriate widgets
    community_safety_1 = st.slider("How safe do you feel in your neighborhood in terms of crime and security?", 0, 10, 0)
    community_safety_2 = st.slider("Rate the sense of community and neighborly relations in your area.", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if community_safety_1 == 0 and community_safety_2 == 0:
        st.warning("Please answer all questions in the Community Safety and Neighborhood Cohesion section.")
        return


    st.subheader("Cultural and Recreational Facilities:")
    # Add more questions here using appropriate widgets
    cultural_recreational_1 = st.slider("How satisfied are you with the availability of cultural centers, libraries, parks, and recreational facilities in City?", 0, 10, 0)
    cultural_recreational_2 = st.slider("Rate the city's efforts in promoting cultural events and community gatherings.", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if cultural_recreational_1 == 0 and cultural_recreational_2 == 0:
        st.warning("Please answer all questions in the Cultural and Recreational Facilities section.")
        return


    st.subheader("Employment and Economic Opportunities:")
    # Add more questions here using appropriate widgets
    employment_economic_1 = st.slider("Rate the availability of job opportunities and the ease of finding employment in City.", 0, 10, 0)
    employment_economic_2 = st.slider("How satisfied are you with the city's support for entrepreneurship and business growth?", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if employment_economic_1 == 0 and employment_economic_2 == 0:
        st.warning("Please answer all questions in the Employment and Economic Opportunities section.")
        return



    st.subheader("Quality and Affordability of Housing:")
    # Add more questions here using appropriate widgets
    quality_affordability_housing_1 = st.slider("Rate the affordability and availability of housing options in City.", 0, 10, 0)
    quality_affordability_housing_2 = st.slider("How satisfied are you with the quality of housing and residential neighborhoods in the city?", 0, 10, 0)
    if quality_affordability_housing_1 == 0 and quality_affordability_housing_2 == 0:
        st.warning("Please answer all questions in the Quality and Affordability of Housing section.")
        return


    st.subheader("Public Health and Healthcare Services:")
    # Add more questions here using appropriate widgets
    public_health_healthcare_1 = st.slider("Rate the accessibility and quality of healthcare services, including clinics and hospitals.", 0, 10, 0)
    public_health_healthcare_2 = st.slider("How satisfied are you with the city's initiatives for public health and disease prevention?", 0, 10, 0)
     # Check if all sliders in the subsection have been interacted with
    if public_health_healthcare_1 == 0 and public_health_healthcare_2 == 0:
        st.warning("Please answer all questions in the Public Health and Healthcare Services section.")
        return


    st.subheader("Financial Inclusion and Banking Services:")
    # Add more questions here using appropriate widgets
    financial_inclusion_banking_1 = st.slider("Rate the availability of banking services and financial inclusion initiatives in City.", 0, 10, 0)
    financial_inclusion_banking_2 = st.slider("How easy is it to access banking facilities and conduct financial transactions?", 0, 10, 0)
    # Check if all sliders in the subsection have been interacted with
    if financial_inclusion_banking_1 == 0 and financial_inclusion_banking_2 == 0:
        st.warning("Please answer all questions in the Financial Inclusion and Banking Services section.")
        return


    st.subheader("Public Spaces and Community Facilities:")
    # Add more questions here using appropriate widgets
    public_spaces_community_1 = st.slider("Rate the availability and maintenance of public spaces, community centers, and recreational areas in the city.", 0, 10, 0)
    public_spaces_community_2 = st.slider("How satisfied are you with the cleanliness and accessibility of these spaces?", 0, 10, 0)
    if public_spaces_community_1 == 0 and public_spaces_community_2 == 0:
        st.warning("Please answer all questions in the Public Spaces and Community Facilities section.")
        return



    st.subheader("Traffic Management and Commute Time:")
    # Add more questions here using appropriate widgets
    traffic_management_commute_1 = st.slider("How satisfied are you with the traffic management and commute time within the city?", 0, 10, 0)
    traffic_management_commute_2 = st.slider("Rate the effectiveness of traffic flow and congestion reduction measures.", 0, 10, 0)
    if traffic_management_commute_1 == 0 and traffic_management_commute_2 == 0:
        st.warning("Please answer all questions in the Traffic Management and Commute Time section.")
        return

    st.subheader("Water Quality and Services:")
    # Add more questions here using appropriate widgets
    water_quality_services_1 = st.slider("How satisfied are you with the quality of Water supplied/present in the city?", 0, 10, 0)
    water_quality_services_2 = st.slider("Are you getting sufficient water for your daily uses?", 0, 10, 0)
    if water_quality_services_1 == 0 and water_quality_services_2 == 0:
        st.warning("Please answer all questions in the Water Quality and Services section.")
        return
    
    # Show the "Save" button in the survey section
    if st.button("Save"):
        # Combine all data into one dictionary
        slider_value = {
            "Accessibility and Transportation_1": [accessibility_transportation_1],
            "Accessibility and Transportation_2": [accessibility_transportation_2],
            "Accessibility and Transportation_3": [accessibility_transportation_3],
            "Housing Infrastructure_1": [housing_infrastructure_1],
            "Housing Infrastructure_2": [housing_infrastructure_2],
            "Healthcare and Education_1": [healthcare_education_1],
            "Healthcare and Education_2": [healthcare_education_2],
            "Safety and Security_1": [safety_security_1],
            "Safety and Security_2": [safety_security_2],
            "Citizen Engagement and Governance_1": [citizen_governance_1],
            "Citizen Engagement and Governance_2": [citizen_governance_2],
            "Environmental Sustainability_1": [environmental_sustainability_1],
            "Environmental Sustainability_2": [environmental_sustainability_2],
            "Technology and Digital services_1": [technology_digital_services_1],
            "Technology and Digital services_2": [technology_digital_services_2],
            "Inclusivity and Social Services_1": [inclusivity_social_services_1],
            "Inclusivity and Social Services_2": [inclusivity_social_services_2],
            "Quality of Life_1": [quality_of_life_1],
            "Quality of Life_2": [quality_of_life_2],
            "Natural Disaster Management_1": [natural_disaster_1],
            "Natural Disaster Management_2": [natural_disaster_2],
            "Government services and Bureaucracy_1": [government_services_1],
            "Government services and Bureaucracy_2": [government_services_2],
            "Community safety and Neighbourhood Cohesion_1": [community_safety_1],
            "Community safety and Neighbourhood Cohesion_2": [community_safety_2],
            "Cultural and Recreational facilities_1": [cultural_recreational_1],
            "Cultural and Recreational facilities_2": [cultural_recreational_2],
            "Employment and Economic opportunities_1": [employment_economic_1],
            "Employment and Economic opportunities_2": [employment_economic_2],
            "Quality and Affordability of Housing_1": [quality_affordability_housing_1],
            "Quality and Affordability of Housing_2": [quality_affordability_housing_2],
            "Public Health and Healthcare services_1": [public_health_healthcare_1],
            "Public Health and Healthcare services_2": [public_health_healthcare_2],
            "Financial Inclusion and Banking Services_1": [financial_inclusion_banking_1],
            "Financial Inclusion and Banking Services_2": [financial_inclusion_banking_2],
            "Public spaces and community facilities_1": [public_spaces_community_1],
            "Public spaces and community facilities_2": [public_spaces_community_2],
            "Traffic Management and commute time_1": [traffic_management_commute_1],
            "Traffic Management and commute time_2": [traffic_management_commute_2],
            "Water Quality and Services_1": [water_quality_services_1],
            "Water Quality and Services_2": [water_quality_services_2]}
        # Calculate the sum and count for each subsection
        sum_values = {}
        count_values = {}
        for slider, value in slider_value.items():
            subsection = slider.split("_")[0]  # Extract the subsection name
            sum_values[subsection] = sum_values.get(subsection, 0) + value[0]
            count_values[subsection] = count_values.get(subsection, 0) + 1
        scores = {}
        for sub_cat , value in sum_values.items() :
            scores[sub_cat] = value/count_values[sub_cat]
        
        categories = {
        "Economic (05)": {
            "Employment and Economic opportunities": 5,
        },
        "Institutional (25)": {
            "Citizen Engagement and Governance": 6.25,
            "Technology and Digital services": 6.25,
            "Government services and Bureaucracy": 6.25,
            "Financial Inclusion and Banking Services": 6.25,
        },
        "Physical (45)": {
            "Accessibility and Transportation": 6.428571429,
            "Housing Infrastructure": 6.428571429,
            "Environmental Sustainability": 6.428571429,
            "Quality and Affordability of Housing": 6.428571429,
            "Public spaces and community facilities": 6.428571429,
            "Water Quality and Services": 6.428571429,
            "Traffic Management and commute time": 6.428571429,
        },
        "Social (25)": {
            "Healthcare and Education": 3.125,
            "Safety and Security": 3.125,
            "Inclusivity and Social Services": 3.125,
            "Quality of life": 3.125,
            "Natural Disaster Management": 3.125,
            "Community safety and Neighbourhood Cohesion": 3.125,
            "Cultural and Recreational facilities": 3.125,
            "Public Health and Healthcare services": 3.125,
        }}
        # Calculate the weighted score for each subcategory
        weighted_scores = {}
        for pillar, subcategories in categories.items():
            temp = 0
            for subcategory, weight in subcategories.items():
                actual_score = scores.get(subcategory, 0)
                temp += actual_score * weight/10
            weighted_scores[pillar] = temp                
        
        # Calculate the total weighted score
        total_weighted_score = round(sum(weighted_scores.values()),2)
        data = {
            "Name": [name],
            "Age": [age],
            "Sex": [sex],
            "Smart City": [smart_city],
            "Accessibility_Transportation_1": [accessibility_transportation_1],
            "Accessibility_Transportation_2": [accessibility_transportation_2],
            "Accessibility_Transportation_3": [accessibility_transportation_3],
            "Housing_Infrastructure_1": [housing_infrastructure_1],
            "Housing_Infrastructure_2": [housing_infrastructure_2],
            "Healthcare_Education_1": [healthcare_education_1],
            "Healthcare_Education_2": [healthcare_education_2],
            "Safety_Security_1": [safety_security_1],
            "Safety_Security_2": [safety_security_2],
            "Citizen_Governance_1": [citizen_governance_1],
            "Citizen_Governance_2": [citizen_governance_2],
            "Environmental_Sustainability_1": [environmental_sustainability_1],
            "Environmental_Sustainability_2": [environmental_sustainability_2],
            "Technology_Digital_Services_1": [technology_digital_services_1],
            "Technology_Digital_Services_2": [technology_digital_services_2],
            "Inclusivity_Social_Services_1": [inclusivity_social_services_1],
            "Inclusivity_Social_Services_2": [inclusivity_social_services_2],
            "Quality_of_Life_1": [quality_of_life_1],
            "Quality_of_Life_2": [quality_of_life_2],
            "Natural_Disaster_1": [natural_disaster_1],
            "Natural_Disaster_2": [natural_disaster_2],
            "Government_Services_1": [government_services_1],
            "Government_Services_2": [government_services_2],
            "Community_Safety_1": [community_safety_1],
            "Community_Safety_2": [community_safety_2],
            "Cultural_Recreational_1": [cultural_recreational_1],
            "Cultural_Recreational_2": [cultural_recreational_2],
            "Employment_Economic_1": [employment_economic_1],
            "Employment_Economic_2": [employment_economic_2],
            "Quality_Affordability_Housing_1": [quality_affordability_housing_1],
            "Quality_Affordability_Housing_2": [quality_affordability_housing_2],
            "Public_Health_Healthcare_1": [public_health_healthcare_1],
            "Public_Health_Healthcare_2": [public_health_healthcare_2],
            "Financial_Inclusion_Banking_1": [financial_inclusion_banking_1],
            "Financial_Inclusion_Banking_2": [financial_inclusion_banking_2],
            "Public_Spaces_Community_1": [public_spaces_community_1],
            "Public_Spaces_Community_2": [public_spaces_community_2],
            "Traffic_Management_Commute_1": [traffic_management_commute_1],
            "Traffic_Management_Commute_2": [traffic_management_commute_2],
            "Water_Quality_Services_1": [water_quality_services_1],
            "Water_Quality_Services_2": [water_quality_services_2],
            "Ease of Index" : total_weighted_score
        }
        
        # Save the data to the CSV file
        save_to_csv(data)
        st.write("Data saved successfully! Thank you for your contribution to the survey.")
        
        
        slider_value = {
            "Accessibility and Transportation_1": [accessibility_transportation_1],
            "Accessibility and Transportation_2": [accessibility_transportation_2],
            "Accessibility and Transportation_3": [accessibility_transportation_3],
            "Housing Infrastructure_1": [housing_infrastructure_1],
            "Housing Infrastructure_2": [housing_infrastructure_2],
            "Healthcare and Education_1": [healthcare_education_1],
            "Healthcare and Education_2": [healthcare_education_2],
            "Safety and Security_1": [safety_security_1],
            "Safety and Security_2": [safety_security_2],
            "Citizen Engagement and Governance_1": [citizen_governance_1],
            "Citizen Engagement and Governance_2": [citizen_governance_2],
            "Environmental Sustainability_1": [environmental_sustainability_1],
            "Environmental Sustainability_2": [environmental_sustainability_2],
            "Technology and Digital services_1": [technology_digital_services_1],
            "Technology and Digital services_2": [technology_digital_services_2],
            "Inclusivity and Social Services_1": [inclusivity_social_services_1],
            "Inclusivity and Social Services_2": [inclusivity_social_services_2],
            "Quality of Life_1": [quality_of_life_1],
            "Quality of Life_2": [quality_of_life_2],
            "Natural Disaster Management_1": [natural_disaster_1],
            "Natural Disaster Management_2": [natural_disaster_2],
            "Government services and Bureaucracy_1": [government_services_1],
            "Government services and Bureaucracy_2": [government_services_2],
            "Community safety and Neighbourhood Cohesion_1": [community_safety_1],
            "Community safety and Neighbourhood Cohesion_2": [community_safety_2],
            "Cultural and Recreational facilities_1": [cultural_recreational_1],
            "Cultural and Recreational facilities_2": [cultural_recreational_2],
            "Employment and Economic opportunities_1": [employment_economic_1],
            "Employment and Economic opportunities_2": [employment_economic_2],
            "Quality and Affordability of Housing_1": [quality_affordability_housing_1],
            "Quality and Affordability of Housing_2": [quality_affordability_housing_2],
            "Public Health and Healthcare services_1": [public_health_healthcare_1],
            "Public Health and Healthcare services_2": [public_health_healthcare_2],
            "Financial Inclusion and Banking Services_1": [financial_inclusion_banking_1],
            "Financial Inclusion and Banking Services_2": [financial_inclusion_banking_2],
            "Public spaces and community facilities_1": [public_spaces_community_1],
            "Public spaces and community facilities_2": [public_spaces_community_2],
            "Traffic Management and commute time_1": [traffic_management_commute_1],
            "Traffic Management and commute time_2": [traffic_management_commute_2],
            "Water Quality and Services_1": [water_quality_services_1],
            "Water Quality and Services_2": [water_quality_services_2]}
        # Calculate the sum and count for each subsection
        sum_values = {}
        count_values = {}
        for slider, value in slider_value.items():
            subsection = slider.split("_")[0]  # Extract the subsection name
            sum_values[subsection] = sum_values.get(subsection, 0) + value[0]
            count_values[subsection] = count_values.get(subsection, 0) + 1
        scores = {}
        for sub_cat , value in sum_values.items() :
            scores[sub_cat] = value/count_values[sub_cat]
        
        categories = {
        "Economic (05)": {
            "Employment and Economic opportunities": 5,
        },
        "Institutional (25)": {
            "Citizen Engagement and Governance": 6.25,
            "Technology and Digital services": 6.25,
            "Government services and Bureaucracy": 6.25,
            "Financial Inclusion and Banking Services": 6.25,
        },
        "Physical (45)": {
            "Accessibility and Transportation": 6.428571429,
            "Housing Infrastructure": 6.428571429,
            "Environmental Sustainability": 6.428571429,
            "Quality and Affordability of Housing": 6.428571429,
            "Public spaces and community facilities": 6.428571429,
            "Water Quality and Services": 6.428571429,
            "Traffic Management and commute time": 6.428571429,
        },
        "Social (25)": {
            "Healthcare and Education": 3.125,
            "Safety and Security": 3.125,
            "Inclusivity and Social Services": 3.125,
            "Quality of life": 3.125,
            "Natural Disaster Management": 3.125,
            "Community safety and Neighbourhood Cohesion": 3.125,
            "Cultural and Recreational facilities": 3.125,
            "Public Health and Healthcare services": 3.125,
        }}
        # Calculate the weighted score for each subcategory
        weighted_scores = {}
        for pillar, subcategories in categories.items():
            temp = 0
            for subcategory, weight in subcategories.items():
                actual_score = scores.get(subcategory, 0)
                temp += actual_score * weight/10
            weighted_scores[pillar] = temp                
        
        # Calculate the total weighted score
        total_weighted_score = round(sum(weighted_scores.values()),2)


        st.write(f"Total Score ---> {total_weighted_score}/100 !!")
        st.progress(total_weighted_score / 100.0)


            
        
def dashboard_section():
    st.subheader("Dashboard")
    # Add code for displaying the dashboard and visualizations here
    # Replace the following line with appropriate visualizations based on the data collected in the CSV file
    st.write("Visualization coming soon!")

def main():
    st.title("Survey 📈")

    # Add radio buttons to switch between survey and dashboard sections
    survey_section()

if __name__ == "__main__":
    main()
