function ElementSizeMonitor(el, sizeChangeCallback) {
    this.element = el;
    this.callback = sizeChangeCallback;
    this.resize = this.resize.bind(this);
    this.lastWidth = -1;
    this.lastHeight = -1;
    this.lastLeft = -1;
    this.lastTop = -1;
    window.addEventListener('resize', this.resize);
    this.resize();
};
ElementSizeMonitor.prototype.resize = function () {
    const rc = this.element.getBoundingClientRect();
    const width = rc.width;
    const height = rc.height;
    const left = rc.left;
    const top = rc.top;
    if (this.lastWidth !== width ||  this.lastHeight !== height || this.lastLeft !== left || this.lastTop !== top) {
        this.callback(left, top, width, height);
        this.lastWidth = width;
        this.lastHeight = height;
        this.lastLeft = left;
        this.lastTop = top;
    }
};
ElementSizeMonitor.prototype.end = function() {
    window.removeEventListener('resize', this.resize);
}

function ElementContainerConstraint(container, element, opts) {
    this.options = Object.assign({}, {
        securityPadding: 10,
    }, opts);
    var id = element.getAttribute('id');
    if (id === null || id === undefined) {
        id = 'constraint-' + Date.now().toString() + Math.random().toString();
        element.setAttribute('id');
    }
    this.element = element;
    this.id = id;
    this.container = container;
    const limitStyle = document.createElement('style');
    limitStyle.setAttribute('type', 'text/css');
    document.head.appendChild(limitStyle);
    this.limitStyle = limitStyle;
    this.callback = this.callback.bind(this);
    this.resizer = new ElementSizeMonitor(container, this.callback);
}

ElementContainerConstraint.prototype.callback = function(containerLeft, containerTop, containerWidth, containerHeight){
    this.limitStyle.innerText = '';
    const rc = this.element.getBoundingClientRect();
    const left = rc.left;
    const top = rc.top;
    const right = rc.left + rc.width;
    const bottom = rc.top + rc.height;
    const containerRight = containerLeft + containerWidth;
    const containerBottom = containerTop + containerHeight;
    let dx = 0;
    let dy = 0;
    if (right > containerRight) {
        dx = right - containerRight + this.options.securityPadding;
    }
    if (bottom > containerBottom) {
        dy = bottom - containerBottom + this.options.securityPadding;
    }
    let innerLeft = left - containerLeft;
    const rawInnerLeft = innerLeft;
    let innerTop = top - containerTop;
    const rawInnerTop = innerTop;
    if (dx > 0) {
        if (innerLeft > 0) {
            if (innerLeft >= dx) {
                innerLeft -= dx;
                dx = 0;
            } else {
                dx -= innerLeft - this.options.securityPadding;
                innerLeft = this.options.securityPadding;
            }
        }
    }
    if (dy > 0) {
        if (innerTop > 0) {
            if (innerTop >= dy) {
                innerTop -= dy;
                dy = 0;
            } else {
                dy -= innerTop - this.options.securityPadding;
                innerTop = this.options.securityPadding;
            }
        }
    }
    let styles = '';
    if (dx > 0) {
        const w = rc.width - dx;
        styles += 'width: ' + w + 'px !important;';
    }
    if (dy > 0) {
        const h = rc.height - dy;
        styles += 'height: ' + h + 'px !important;';
    }
    if (innerLeft !== rawInnerLeft) {
        styles += 'left: ' + innerLeft + 'px !important;';
    }
    if (innerTop !== rawInnerTop) {
        styles += 'top: ' + innerTop + 'px !important;';
    }
    this.limitStyle.innerText = '#' + this.id +  ' { ' + styles + ' }';
}
