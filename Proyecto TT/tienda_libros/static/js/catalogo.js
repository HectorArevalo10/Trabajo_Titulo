// libreria/static/js/catalogo.js

document.addEventListener('DOMContentLoaded', function() {
    const filter = document.getElementById('genre-filter');

    filter.addEventListener('change', function() {
        const genre = filter.value;
        const books = document.querySelectorAll('.book-card');

        books.forEach(book => {
            if (genre === 'all' || book.dataset.genre === genre) {
                book.style.display = 'block';
            } else {
                book.style.display = 'none';
            }
        });
    });
});
