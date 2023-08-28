const articleList = document.getElementById('article-list');

fetch('http://127.0.0.1:8000/reddit/tech')
    .then(response => response.json())
    .then(articles => {
        articles.forEach(article => {
            const listItem = document.createElement('li');
            listItem.className = 'article-card';
            
            listItem.innerHTML = `
                <h2 class="article-title"><a href="${article.thread_link}" target="_blank">${article.title}</a></h2>
                <p class="article-author">Author: ${article.author}</p>
                <p class="article-creation-date">Creation Date: ${new Date(article.creation_date * 1000).toLocaleString()}</p>
                <p class="article-link"><a href="${article.link}" target="_blank">Read Article</a></p>
            `;
            
            articleList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error fetching articles:', error));
