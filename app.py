from flask import Flask, render_template, request
import pandas as pd
import pickle
    

df_movie = pd.read_csv('movie_dataset.csv')

with open('similarity_tfidf_5000.pkl', 'rb') as simi : 
    similarity = pickle.load(simi)

def return_top5_df(indx) : 
    indx_percentage = sorted(list(enumerate(similarity[indx])), key=lambda x : x[1], reverse=True)[:6]
    indexs = [ itm[0] for itm in indx_percentage]
    return df_movie.iloc[indexs, :]

def return_dic(row) : 
    return {
        'indx' : row.name,
        'img_link' : row['poster_path'],
        'wiki_link' : row['wiki_link'],
        'title' : row['original_title'],
        'genres' : row['genres'].replace("|", " | "),
        'story' : row['story'],
        'actors' : " | ".join(row['actors'].split("|")[:5])[:-3]
    }

# top5_df = return_top5_df(df_movie[df_movie['title_y'] == selected_movie ].index[0])
# # st.write(top5_df['poster_path'].values)
# img_pt = top5_df['poster_path'].values
# title = top5_df['title_y'].values
    

app = Flask(__name__)

@app.route("/", methods = ['POST', "GET"])
def See() : 
    if request.method == 'POST' : 
        movie = request.form['movie']
        # print(movie)
        try : 
            top5_df = return_top5_df(df_movie[df_movie['original_title'] == movie ].index[0]).reset_index()
        except : 
            top5_df = return_top5_df(0).reset_index()
        # arr_dic = return_top5_df(df_movie[df_movie['original_title'] == movie].index[0]).apply(return_dic, axis = 1).values
        # print(top5_df.columns) 
        
        
        return render_template(
            'index.html', 
            recomend = df_movie['original_title'].values, 
            zip_value = top5_df[['index', 'poster_path', 'wiki_link', 'original_title', 'genres', 'story', 'actors']].values
            )
    

    
    if request.args.get('indx') : 
        indx = request.args.get('indx')
        # print(indx)
        try : 
            top5_df = return_top5_df(int(indx)).reset_index()
        except : 
            top5_df = return_top5_df(0).reset_index()
        return render_template(
            'index.html', 
            recomend = df_movie['original_title'].values, 
            zip_value = top5_df[['index', 'poster_path', 'wiki_link', 'original_title', 'genres', 'story', 'actors']].values
        )
    
    
    return render_template('index.html', recomend = df_movie['original_title'].values)

if __name__ == "__main__" : 
    app.run(debug=False, host='0.0.0.0')