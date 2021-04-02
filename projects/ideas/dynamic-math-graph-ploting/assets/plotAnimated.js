function f(x) {
    return x * x * x;
}

let zoom = 100;
let translationX = 250;
let translationY = 250;
let resolution = 5;

const canvas = document.getElementById('plot');
const context = canvas.getContext('2d');

function plot(pointOnly) {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    context.clearRect(0, 0, w, h);

    const space = w / resolution;
    if (!pointOnly) {
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

    if (resolution < 20) {
        x = 0;
        for (let i = 0; i < resolution; i += 1) {
            const spaceX = (x - translationX) / zoom;
            const spaceY = f(spaceX);
            const y = (spaceY * zoom) - translationY;

            context.fillStyle = 'black';
            context.fillRect(x - 4, - y - 4, 8, 8);

            x += space;
        }
    }
    if (pointOnly) {
        setTimeout(() => plot(false), 500);
    }
}

function replot() {
    resolution += 1;
    plot(true);
    if (resolution < 20) {
        setTimeout(replot, 1000);
    }
}

replot();