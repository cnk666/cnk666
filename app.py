from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 模拟一个电影数据库
movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan"},
    {"id": 2, "title": "The Shawshank Redemption", "director": "Frank Darabont"},
]

# 主页，显示电影列表
@app.route('/')
def index():
    return render_template('index.html', movies=movies)

# 电影详情页
@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return render_template('movie_detail.html', movie=movie)
    else:
        return "Movie not found", 404

# 添加电影页面
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        director = request.form.get('director')
        if title and director:
            new_movie = {"id": len(movies) + 1, "title": title, "director": director}
            movies.append(new_movie)
            return jsonify({"message": "Movie added successfully", "movie": new_movie})
        else:
            return jsonify({"error": "Title and director are required"}), 400

    return render_template('add_movie.html')

if __name__ == '__main__':
    app.run(debug=True)
