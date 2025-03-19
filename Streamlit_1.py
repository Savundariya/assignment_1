import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

connection = mysql.connector.connect(
  host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "9k73eECEy7JzczW.root",
  password = "zwbywNn80SwY93CX",
  database = "Project_IMDB",
  ssl_ca = r"C:\Users\Dell\VS_code\Project1/isrgrootx1.pem",
  ssl_verify_cert = True,
  ssl_verify_identity = True
)

choice = st.sidebar.selectbox('Navigation',['Home','Visualization','filtering functions'])

if choice == 'Home':
    st.title('Welcome to Streamlit!')

if choice == 'filtering functions':
    st.title("IMDb Movie Filter")

    # Connect to TiDB
    cursor = connection.cursor(buffered=True)

    # Fetch all movie data
    query = "SELECT * FROM Project_IMDB.final_IMDB_Movie_List;"
    cursor.execute(query)
    all_movies = cursor.fetchall()

    # Convert to DataFrame
    df = pd.DataFrame(all_movies, columns=["Title", "Duration(in_mins)","Rating","Votes","Genre"])

    # Filter Options
    st.markdown("# Filter by Duration (Hours)")
    duration_filter = st.radio("", ["< 120 mins", "120–180 mins", "> 180 mins"])

    if duration_filter == "< 120 mins":
        filtered_df = df[df["Duration(in_mins)"] < 120]
    elif duration_filter == "120–180 mins":
        filtered_df = df[(df["Duration(in_mins)"] >= 120) & (df["Duration"] <= 180)]
    else:
        filtered_df = df[df["Duration(in_mins)"] > 180]

    # Display Results
    st.write(f"Showing {len(filtered_df)} movies for selection: {duration_filter}")
    st.dataframe(filtered_df[["Title", "Duration(in_mins)","Rating","Votes","Genre"]])

    st.markdown("# Filter by Genre")
    genre_filter = st.radio("",["Action", "Comedy", "Crime", "Fantasy", "Romance"])

    if genre_filter == "Action":
        filtered_df2 = df[df["Genre"]=="Action"]
    elif genre_filter == "Comedy":
        filtered_df2 = df[df["Genre"]=="Comedy"]
    elif genre_filter == "Crime":
        filtered_df2 = df[df["Genre"]=="Crime"]
    elif genre_filter == "Fantasy":
        filtered_df2 = df[df["Genre"]=="Fantasy"]
    else:
        filtered_df2 = df[df["Genre"]=="Romance"]
    
    st.write(f"Showing {len(filtered_df2)} movies for selection: {genre_filter}")
    st.dataframe(filtered_df2[["Title", "Duration(in_mins)","Rating","Votes","Genre"]])

    st.markdown("# Filter by IMDb Rating")

    # Dropdown for selecting filter type (>, <, =)
    filter_type = st.selectbox("Select Filter Type:", [">", "<", "="])

    # Slider to select the rating threshold
    rating_threshold = st.slider("Select IMDb Rating:", 1.0, 10.0, 8.0, step=0.1)

    st.success(f"Filtering movies where IMDb rating is {filter_type} {rating_threshold}")

    # Modify SQL query to apply the filter
    query = f"SELECT * FROM Project_IMDB.final_IMDB_Movie_List WHERE rating {filter_type} %s;"
    cursor.execute(query, (rating_threshold,))
    filtered_movies = cursor.fetchall()

    # Convert to DataFrame for display
    st.write(f"Showing {len(filtered_movies)} movies where IMDb rating {filter_type} {rating_threshold}.")
    df = pd.DataFrame(filtered_movies, columns=["Title", "Duration(in_mins)","Rating","Votes","Genre"])
    st.dataframe(df)


    st.markdown("# Filter by Voting")

    # Slider for selecting the vote count threshold
    vote_threshold = st.number_input("Select Minimum Vote Count:", min_value=0, max_value=700000, step=1000)

    st.success(f"Filtering movies with at least {vote_threshold} votes.")

    # Modify SQL query to fetch data
    query = "SELECT * FROM Project_IMDB.final_IMDB_Movie_List;"
    cursor.execute(query)
    all_movies = cursor.fetchall()

    # Convert to DataFrame
    df = pd.DataFrame(all_movies, columns=["Title", "Duration(in_mins)","Rating","Votes","Genre"])

    # Apply filtering
    filtered_df = df[df["Votes"] >= vote_threshold]

    # Display Results
    st.write(f"Showing {len(filtered_df)} movies with at least {vote_threshold} votes.")
    st.dataframe(filtered_df[["Title", "Duration(in_mins)","Rating","Votes","Genre"]])

    # Close Connection
    cursor.close()
    connection.close()

if choice == 'Visualization':
    st.title("Interactive Visualizations")

    #Genre Distribution
    connection = mysql.connector.connect(
    host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    port = 4000,
    user = "9k73eECEy7JzczW.root",
    password = "zwbywNn80SwY93CX",
    database = "Project_IMDB",
    ssl_ca = r"C:\Users\Dell\VS_code\Project1/isrgrootx1.pem",
    ssl_verify_cert = True,
    ssl_verify_identity = True)
    
    cursor = connection.cursor(buffered=True)

    # Fetch all movie data
    query = "SELECT * FROM Project_IMDB.final_IMDB_Movie_List"
    cursor.execute(query)
    all_movies = cursor.fetchall()

    # Convert to DataFrame
    df = pd.DataFrame(all_movies, columns=["Title", "Duration(in_mins)", "Rating", "Votes", "Genre"])

    ############# Genre Distribution: Plot the count of movies for each genre in a bar chart.################


    # Count the number of movies per genre
    genre_counts = df["Genre"].value_counts()

    # Plot Bar Chart
    st.markdown("# 1. Genre Distribution")
    st.bar_chart(genre_counts)

    ############# Rating Distribution: Display a histogram or boxplot of movie ratings.################
    
    st.markdown("# 2. Rating Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Rating"], bins=10, kde=True, ax=ax)
    ax.set_xlabel("IMDb Rating")
    ax.set_ylabel("Count of Movies")
    st.pyplot(fig)

    ############# Voting Trends by Genre: Visualize average voting counts across different genres.################

    st.markdown("# 3. Voting Trends by Genre")

    # Calculate average votes per genre
    avg_votes_per_genre = df.groupby("Genre")["Votes"].mean().sort_values(ascending=False)

    # Bar Chart
    fig, ax = plt.subplots()
    sns.barplot(x=avg_votes_per_genre.index, y=avg_votes_per_genre.values, ax=ax)
    ax.set_xlabel("Genre")
    ax.set_ylabel("Average Votes")
    plt.xticks(rotation=45)

    # Show plot in Streamlit
    st.pyplot(fig)


    # Voting Trends by Genre
    #st.markdown("# 3. Voting Trends by Genre")
    #avg_votes_per_genre = df.groupby("Genre")["Votes"].mean().sort_values(ascending=False)
    #st.bar_chart(avg_votes_per_genre)


    ############# Ratings by Genre: Use a heatmap to compare average ratings across genres.################

    st.markdown("# 4. Rating Trends by Genre")

    avg_ratings_per_genre = df.groupby("Genre")[["Rating"]].mean()

    #  Create a Heatmap-friendly format (Genres as Rows)
    pivot_df = avg_ratings_per_genre.T  # Transpose for heatmap

    # Heatmap Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(pivot_df, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5, ax=ax)

    ax.set_xlabel("Genre")
    ax.set_ylabel("Average Rating")
    plt.xticks(rotation=45)

    # Show plot in Streamlit
    st.pyplot(fig)

    #############Average Duration by Genre: Show the average movie duration per genre in a horizontal bar chart..##############
    st.markdown("# 5. Average Duration by Genre")

    avg_duration_per_genre = df.groupby("Genre")["Duration(in_mins)"].mean().sort_values(ascending=False)

    # Plot Bar Chart
    st.bar_chart(avg_duration_per_genre,horizontal=True)

    #############Top 10 Movies by Rating and Voting Counts: Identify movies with the highest ratings and significant voting engagement.
    # Section Title
    st.markdown("# 6. Top 10 Movies by Rating & Voting Counts")

    # Filter movies with high ratings and significant votes
    top_movies = df.sort_values(["Rating", "Votes"], ascending=[False, False]).head(10)

    # Display as a Table
    st.dataframe(top_movies[["Title", "Rating", "Votes"]])


    #############Genre-Based Rating Leaders: Highlight the top-rated movie for each genre in a table.
    st.markdown("# 7. Genre-Based Rating Leaders")

    # Get the top-rated movie per genre
    top_movies_per_genre = df.loc[df.groupby("Genre")["Rating"].idxmax()]

    # Sort genres by rating
    top_movies_per_genre = top_movies_per_genre.sort_values("Rating", ascending=False)

    # Display table
    st.dataframe(top_movies_per_genre[["Genre", "Title", "Rating"]])

    ############# Most Popular Genres by Voting: Identify genres with the highest total voting counts in a pie chart.
    st.markdown("# 8. Most Popular Genres by Voting")

    # Group by Genre and sum total votes
    genre_votes = df.groupby("Genre")["Votes"].sum().sort_values(ascending=False)

    # Plot Pie Chart
    fig, ax = plt.subplots()
    ax.pie(genre_votes, labels=genre_votes.index, autopct="%1.1f%%", startangle=140, 
    colors=plt.cm.Paired.colors, wedgeprops={"edgecolor": "black"})

    # Display in Streamlit
    st.pyplot(fig)

    ############# Duration Extremes: Use a table or card display to show the shortest and longest movies.
    st.markdown("# 9. Duration Extremes: Shortest & Longest Movies")

    # Sort by Duration
    df_sorted = df.sort_values(by="Duration(in_mins)", ascending=True)

    # Get shortest and longest movie
    shortest_movie = df_sorted.iloc[0]  # First row (smallest duration)
    longest_movie = df_sorted.iloc[-1]  # Last row (largest duration)

    # Convert to DataFrame for display
    duration_extremes = pd.DataFrame([shortest_movie, longest_movie])

    # Rename index for clarity
    duration_extremes.index = ["Shortest Movie", "Longest Movie"]

    # Display result
    st.dataframe(duration_extremes[["Title", "Genre", "Duration(in_mins)"]])


    ############# Correlation Analysis: Analyze the relationship between ratings and voting counts using a scatter plot.
    st.markdown("# 10. Correlation Analysis")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x="Rating", y="Votes", alpha=0.5, ax=ax)
    ax.set_title("Ratings vs. Voting Counts")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Votes (log scale)")
    ax.set_yscale("log")  # Use log scale for better visualization
    # Show in Streamlit
    st.pyplot(fig)
    


    # Close connection
    cursor.close()
    connection.close()