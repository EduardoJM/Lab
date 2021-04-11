function createIndexes(callback, data) {
    if (data) {
        const { posts } = data;
        const output = posts.map((p) => processPost(p));
        callback(data, output);
        return;
    }
    const req = new XMLHttpRequest();
    req.open('GET', './posts/data.json');
    req.onload = function() {
        createIndexes(callback, JSON.parse(this.responseText));
    }
    req.send();
}