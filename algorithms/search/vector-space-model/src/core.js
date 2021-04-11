const { stripHtml } = stringStripHtml;

function processPost(post) {
    const { id, text } = post;
    const escapedText = stripHtml(text);
    const words = escapedText.result.toLowerCase().split(' ');
    const resultIndex = {};
    words.forEach((w) => {
        if (Object.prototype.hasOwnProperty.call(resultIndex, w)) {
            resultIndex[w] += 1;
        } else {
            resultIndex[w] = 1;
        }
    });
    return {
        id,
        indexes: resultIndex
    }
}

function dotProduct(doc1, doc2) {
    const keys1 = Object.keys(doc1);
    const keys2 = Object.keys(doc2);
    const sameKeys = keys1.filter((k) => keys2.includes(k));
    if (sameKeys.length === 0) {
        return 0;
    } else {
        const partials = sameKeys.map((k) => {
            const value1 = doc1[k];
            const value2 = doc2[k];
            return value1 * value2;
        });
        let result = 0;
        partials.forEach((partial) => result += partial);
        return result;
    }
}

function norm(data) {
    const keys = Object.keys(data);
    const partials = keys.map((k) => data[k] * data[k]);
    let value = 0;
    partials.forEach((partial) => value += partial);
    return Math.sqrt(value);
}

function cos(doc1, doc2) {
    const dot = dotProduct(doc1, doc2);
    if (dot === 0) {
        return 0;
    }
    const norm1 = norm(doc1);
    const norm2 = norm(doc2);
    return dot / (norm1 * norm2);
}