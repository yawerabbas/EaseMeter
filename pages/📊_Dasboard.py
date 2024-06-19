import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    # Load the data from the CSV file
    data = pd.read_csv('database.csv')
    return data

def main():
    st.title('Smart City Dashboard')

    # Load data
    data = load_data()
    import pandas as pd

    # Read the CSV file into a DataFrame
    df = pd.read_csv('database.csv')

    # Create a list of new column names
    new_columns = [
        'Accessibility Transportation',
        'Housing Infrastructure',
        'Healthcare Education',
        'Safety Security',
        'Citizen Governance',
        'Environmental Sustainability',
        'Technology Digital Services',
        'Inclusivity Social Services',
        'Quality of Life',
        'Natural Disaster',
        'Government Services',
        'Community Safety',
        'Cultural Recreational',
        'Employment Economic',
        'Quality Affordability Housing',
        'Public Health Healthcare',
        'Financial Inclusion Banking',
        'Public Spaces Community',
        'Traffic Management Commute',
        'Water Quality Services'
    ]

    # Create a list of column names to sum
    column_groups = [
        ['Accessibility_Transportation_1', 'Accessibility_Transportation_2', 'Accessibility_Transportation_3'],
        ['Housing_Infrastructure_1', 'Housing_Infrastructure_2'],
        ['Healthcare_Education_1', 'Healthcare_Education_2'],
        ['Safety_Security_1', 'Safety_Security_2'],
        ['Citizen_Governance_1', 'Citizen_Governance_2'],
        ['Environmental_Sustainability_1', 'Environmental_Sustainability_2'],
        ['Technology_Digital_Services_1', 'Technology_Digital_Services_2'],
        ['Inclusivity_Social_Services_1', 'Inclusivity_Social_Services_2'],
        ['Quality_of_Life_1', 'Quality_of_Life_2'],
        ['Natural_Disaster_1', 'Natural_Disaster_2'],
        ['Government_Services_1', 'Government_Services_2'],
        ['Community_Safety_1', 'Community_Safety_2'],
        ['Cultural_Recreational_1', 'Cultural_Recreational_2'],
        ['Employment_Economic_1', 'Employment_Economic_2'],
        ['Quality_Affordability_Housing_1', 'Quality_Affordability_Housing_2'],
        ['Public_Health_Healthcare_1', 'Public_Health_Healthcare_2'],
        ['Financial_Inclusion_Banking_1', 'Financial_Inclusion_Banking_2'],
        ['Public_Spaces_Community_1', 'Public_Spaces_Community_2'],
        ['Traffic_Management_Commute_1', 'Traffic_Management_Commute_2'],
        ['Water_Quality_Services_1', 'Water_Quality_Services_2']
    ]

    # Create a new DataFrame with the summed columns
    new_df = pd.DataFrame(columns=new_columns)
    for i, group in enumerate(column_groups):
        new_df[new_columns[i]] = df[group].sum(axis=1)

    # Add other columns to the new DataFrame
    new_df['Name'] = df['Name']
    new_df['Age'] = df['Age']
    new_df['Sex'] = df['Sex']
    new_df['Smart City'] = df['Smart City']
    new_df['Ease of Index'] = df['Ease of Index']

    data = new_df
    
    st.sidebar.subheader('View Data')
    view_option = st.sidebar.selectbox('Select View Option', ['Summary', 'Detailed'])
    if view_option == 'Summary':
        st.write('### Summary of Scores')
        st.dataframe(data.head())

    elif view_option == 'Detailed':
        st.write('### Detailed View')
        selected_columns = st.sidebar.multiselect('Select Columns to Display', list(data.columns))
        if selected_columns:
            st.dataframe(data[selected_columns].head())

    # Plot scores for each category
    st.write('### Scores for Each Category')
    category_scores = new_df[new_columns].sum().reset_index()
    category_scores.columns = ['Category', 'Score']
    category_scores = category_scores.sort_values(by='Score', ascending=False)
    st.dataframe(category_scores)

    # Plotting scores for each category
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(category_scores['Category'], category_scores['Score'])
    ax1.set_xticklabels(category_scores['Category'], rotation=45, ha='right')
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Score')
    ax1.set_title('Scores for Each Category')
    st.pyplot(fig1)


    # Plot Ease of Index
    st.write('### Ease of Index')
    data['Ease of Index'] = data['Ease of Index'].astype(float)
    avg_ease_of_index = data['Ease of Index'].mean()
    st.write(f'Average Ease of Index: {avg_ease_of_index:.2f}')
    st.bar_chart(data[['Name', 'Ease of Index']].set_index('Name'))

    # Plot Age distribution
    st.write('### Age Distribution')
    fig2 = plt.figure(figsize=(8, 6))
    sns.histplot(data['Age'], bins=20, kde=True)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution')
    st.pyplot(fig2)

    # Plot heatmap of correlations between score categories
    st.write('### Correlation Heatmap')
    corr_matrix = data[category_scores.Category].corr()
    fig3 = plt.figure(figsize=(20, 16))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Correlation Heatmap')
    st.pyplot(fig3)

    # Scatter plot of two score categories
    st.write('### Scatter Plot of Two Score Categories')
    x_column = st.selectbox('Select X-axis category', category_scores.Category)
    y_column = st.selectbox('Select Y-axis category', category_scores.Category)
    fig4 = plt.figure(figsize=(8, 6))
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter Plot: {x_column} vs {y_column}')
    st.pyplot(fig4)

    # Box plot of score categories
    st.write('### Box Plot of Score Categories')
    selected_boxplot_columns = st.multiselect('Select Columns for Box Plot', list(category_scores.Category))
    if selected_boxplot_columns:
        fig_box, ax_box = plt.subplots(figsize=(10, 8))
        sns.boxplot(data=data[selected_boxplot_columns], palette='Set2', ax=ax_box)
        ax_box.set_xlabel('Categories')
        ax_box.set_ylabel('Score')
        st.pyplot(fig_box)

if __name__ == '__main__':
    main()
