function f(x) {
    return Math.exp(x);
}

let zoom = 100;
let translationX = 250;
let translationY = 250;
let resolution = 100;

const canvas = document.getElementById('plot');
const context = canvas.getContext('2d');

function plot() {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    context.clearRect(0, 0, w, h);

    const space = w / resolution;
    let x = 0;
    context.beginPath();
    for (let i = 0; i < resolution; i += 1) {
        const spaceX = (x - translationX) / zoom;
        const spaceY = f(spaceX);
        const y = (spaceY * zoom) - translationY;
        if (i === 0) {
            context.moveTo(x, -y);
        } else {
            context.lineTo(x, -y);
        }

        x += space;
    }
    context.strokeStyle = 'black';
    context.stroke();
}

canvas.addEventListener('mousedown', function(e){
    const rc = canvas.getBoundingClientRect();
    let startX = e.pageX - rc.left;
    let startY = e.pageY - rc.top;

    const mouseMove = (evt) => {
        const px = evt.pageX - rc.left;
        const py = evt.pageY - rc.top;
        const dx = px - startX;
        const dy = py - startY;
        translationX += dx;
        translationY += dy;
        startX = px;
        startY = py;

        plot();
    }
    
    const mouseUp = (evt) => {
        document.removeEventListener('mousemove', mouseMove);
        document.removeEventListener('mouseup', mouseUp);
    }
    
    document.addEventListener('mousemove', mouseMove);
    document.addEventListener('mouseup', mouseUp);
});

canvas.addEventListener('wheel', function(e){
    const n = zoom - e.deltaY / 10;
    zoom = Math.min(500, Math.max(1, n));

    plot();
});

plot();