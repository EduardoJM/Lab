function findContainer(el) {
    if (el.classList.contains('music-result-container')) {
        return el;
    }
    if (el.parentElement !== null) {
        return findContainer(el.parentElement);
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function() {
    function musicResultClick(e) {
        const container = findContainer(e.target);
        container.querySelector('.music-lyrics').classList.toggle('visible');
    }

    const input = document.getElementById('search-field');
    const resultsElement = document.getElementById('results');

    let posts = [];
    let output = [];
    createIndexes((thePosts, theOutput) => {
        posts = thePosts.posts;
        output = theOutput;

        input.addEventListener('keyup', () => {
            const results = makeSearch(input.value, output, posts);
            let outputHtml = '';
            for (let i = 0; i < results.length; i += 1) {
                const html = '' +
                    '<div class="music-result-container">' +
                        '<div class="music-result">' +
                            '<div class="icon">' +
                                'A' +
                            '</div>' +
                            '<div class="infos">' + 
                                `<h3 class="title">${results[i].title}</h3>` +
                                `<h5 class="artist">${results[i].artist}</h5>` +
                            '</div>' +
                        '</div>' +
                        '<div class="music-lyrics">' +
                            results[i].text +
                        '</div>' +
                    '</div>';
                outputHtml += html;
            }
            
            let musicResultsDOM = resultsElement.querySelectorAll('.music-result');
            for (let i = 0; i < musicResultsDOM.length; i++) {
                musicResultsDOM[i].removeEventListener('click', musicResultClick);
            }

            resultsElement.innerHTML = outputHtml;

            musicResultsDOM = resultsElement.querySelectorAll('.music-result');
            for (let i = 0; i < musicResultsDOM.length; i++) {
                musicResultsDOM[i].addEventListener('click', musicResultClick);
            }
        });
    });
});