function filter(array, func) {
    const filtered = [];
    for (let i = 0; i < array.length; i += 1) {
        if (func(array[i], i)) {
            filtered.push(array[i]);
        }
    }
    return filtered;
}

function map(array, func) {
    const maped = [];
    for (let i = 0; i < array.length; i += 1) {
        maped.push(func(array[i], i));
    }
    return maped;
}

function makeSearch(searchQuery, postIndexes, posts) {
    if (postIndexes.length !== posts.length) {
        return;
    }

    const queryData = processPost({
        id: -1,
        text: searchQuery,
    });

    const postsResults = [];
    for (let index = 0; index < postIndexes.length; index++) {
        const post = postIndexes[index];
        const cossine = cos(post.indexes, queryData.indexes);
        if (cossine > 0) {
            postsResults.push({
                artist: posts[index].artist,
                title: posts[index].title,
                text: posts[index].text,
                cos: cossine,
                indexes: post.indexes,
            });
        }
    }

    const sorted = postsResults.sort((a, b) => {
        const cosA = cos(a.indexes, queryData.indexes);
        const cosB = cos(b.indexes, queryData.indexes);
        if (cosA < cosB) {
            return 1;
        } else if (cosA > cosB) {
            return -1;
        }
        return 0;
    });

    return sorted;
}