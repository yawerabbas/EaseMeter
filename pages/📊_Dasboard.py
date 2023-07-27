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

    st.write('### Summary of Scores')
    st.dataframe(data.head())

    # Plot scores for each category
    st.write('### Scores for Each Category')
    category_columns = [col for col in data.columns if col.endswith('_1') or col.endswith('_2')]
    category_scores = data[category_columns].sum()
    category_scores = category_scores.reset_index()
    category_scores.columns = ['Category', 'Score']
    category_scores = category_scores.sort_values(by='Score', ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(category_scores['Category'], category_scores['Score'])
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Category')
    plt.ylabel('Score')
    plt.title('Scores for Each Category')
    st.pyplot()

    # Plot Ease of Index
    st.write('### Ease of Index')
    data['Ease of Index'] = data['Ease of Index'].astype(float)
    avg_ease_of_index = data['Ease of Index'].mean()
    st.write(f'Average Ease of Index: {avg_ease_of_index:.2f}')
    st.bar_chart(data[['Name', 'Ease of Index']].set_index('Name'))

    # Plot Age distribution
    st.write('### Age Distribution')
    plt.figure(figsize=(8, 6))
    sns.histplot(data['Age'], bins=20, kde=True)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution')
    st.pyplot()

    # Plot heatmap of correlations between score categories
    st.write('### Correlation Heatmap')
    corr_matrix = data[category_columns].corr()
    plt.figure(figsize=(20, 16))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Correlation Heatmap')
    st.pyplot()

    # Scatter plot of two score categories
    st.write('### Scatter Plot of Two Score Categories')
    x_column = st.selectbox('Select X-axis category', category_columns)
    y_column = st.selectbox('Select Y-axis category', category_columns)
    plt.figure(figsize=(8, 6))
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter Plot: {x_column} vs {y_column}')
    st.pyplot()

    # Box plot of score categories
    st.write('### Box Plot of Score Categories')
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=data[category_columns], orient='h')
    plt.xlabel('Score')
    plt.ylabel('Categories')
    plt.title('Box Plot of Score Categories')
    st.pyplot()

if __name__ == '__main__':
    main()
