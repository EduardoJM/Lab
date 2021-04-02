function FakeScrollbar(element, thumb, inner, container, orientation) {
    this.element = element;
    this.thumb = thumb;
    this.orientation = orientation;
    this.inner = inner;
    this.container = container;
    this.transformX = 0;
    this.transformY = 0;
    this.mouseUp = this.mouseUp.bind(this);
    this.mouseDown = this.mouseDown.bind(this);
    this.mouseMove = this.mouseMove.bind(this);
}

FakeScrollbar.prototype.randomId = function(prefix) {
    let prefixStr = 'element';
    if (prefix !== null && prefix !== undefined) {
        prefixStr = prefix;
    }
    return prefixStr + Date.now().toString() + Math.floor(Math.random() * 100).toString();
}

FakeScrollbar.prototype.calcDimensions = function(el) {
    const node = el.cloneNode(true);
    node.setAttribute('id', this.randomId());
    node.style.position = 'absolute';
    node.style.left = '-10000px';
    node.style.top = '-10000px';
    document.body.appendChild(node);
    const rc = node.getBoundingClientRect();
    document.body.removeChild(node);
    const width = rc.width;
    const height = rc.height;
    return {
        width: width,
        height: height,
    };
}

FakeScrollbar.prototype.scroll = function(page) {
    const rc = this.element.getBoundingClientRect();
    const thumbRc = this.thumb.getBoundingClientRect();
    let relative = page;
    let percent = relative;
    if (this.orientation === 'horizontal') {
        relative = relative - rc.left;
        percent = relative / (rc.width - thumbRc.width);
    } else {
        relative = relative - rc.top;
        percent = relative / (rc.height - thumbRc.height);
    }
    if (Number.isNaN(percent) || percent < 0) {
        percent = 0;
    }
    if (percent > 1) {
        percent = 1;
    }
    if (this.orientation === 'horizontal') {
        const innerWidth = this.calcDimensions(this.inner).width;
        const outerWidth = this.container.clientWidth;
        const max = innerWidth - outerWidth;
        this.transformX = max * percent;
        this.thumb.style.transform = 'translateX(' + ((rc.width - thumbRc.width) * percent) + 'px)';
    } else {
        const innerHeight = this.calcDimensions(this.inner).height;
        const outerHeight = this.container.clientHeight;
        const max = innerHeight - outerHeight;
        this.transformY = max * percent;
        this.thumb.style.transform = 'translateY(' + ((rc.height - thumbRc.height) * percent) + 'px)';
    }
    this.inner.style.transform = 'translate(-' + this.transformX + 'px, -' + this.transformY + 'px)';
}

FakeScrollbar.prototype.mouseDown = function(e) {
    if(e.buttons !== 1) {
        return;
    }
    document.addEventListener('mousemove', this.mouseMove);
    document.addEventListener('mouseup', this.mouseUp);
}

FakeScrollbar.prototype.mouseUp = function() {
    document.removeEventListener('mousemove', this.mouseMove);
    document.removeEventListener('mouseup', this.mouseUp);
}

FakeScrollbar.prototype.mouseMove = function(e) {
    if(e.buttons !== 1) {
        return;
    }
    let page = e.pageY;
    if (this.orientation === 'horizontal') {
        page = e.pageX;
    }
    this.scroll(page);
}

FakeScrollbar.prototype.initialize = function() {
    this.thumb.addEventListener('mousedown', this.mouseDown);
}
