import {addInputZone, drawRectangle, redrawRectangles} from "./rectangle_drawer_utils";

export class RectanglesDrawer {
    rectangles = [];
    image_width_ratio
    image_height_ratio
    startX = 0;
    startY = 0;
    screenshot;
    marquee;
    marqueeRect = {
        x: 0,
        y: 0,
        width: 0,
        height: 0,
    };

    constructor(imageHeight, imageWidth) {
        this.init(imageHeight, imageWidth);
    }

    init(image_height, image_width) {
        const $ = document.querySelector.bind(document);
        redrawRectangles(this.rectangles);
        document.getElementById("input-zones").innerHTML = '';

        this.screenshot = $('#screenshot');
        this.marquee = $('#marquee');

        document.getElementById("draw").setAttribute("width", this.screenshot.width)
        document.getElementById("draw").setAttribute("height", this.screenshot.height)
        document.getElementById("draw").setAttribute("viewBox", "0 0 " + this.screenshot.width + " " + this.screenshot.height);

        this.image_width_ratio = image_width / this.screenshot.width
        this.image_height_ratio = image_height / this.screenshot.height

        this.marquee.classList.add('hide');
        this.screenshot.addEventListener('pointerdown', (ev) => {
            console.log(ev);
            this.startDrag.apply(this, [ev]);
        });
    }

    startDrag(ev) {
        if (this.hitTest(ev.layerX, ev.layerY))
            return;
        // middle button delete rect
        if (ev.button === 1) {
            const rect = this.hitTest(ev.layerX, ev.layerY);
            if (rect) {
                this.rectangles.splice(this.rectangles.indexOf(rect), 1);
                redrawRectangles(this.rectangles);
            }
            return;
        }
        window.addEventListener('pointerup', (ev) => {
            this.stopDrag.apply(this, [ev])
        });
        this.screenshot.addEventListener('pointermove', (ev) => {
            this.moveDrag.apply(this, [ev])
        });
        this.marquee.classList.remove('hide');
        this.startX = ev.layerX;
        this.startY = ev.layerY;
    }

    stopDrag(ev) {
        this.marquee.classList.add('hide');
        window.removeEventListener('pointerup', (ev) => {
            this.stopDrag.apply(this, [ev])
        });
        this.screenshot.removeEventListener('pointermove', (ev) => {
            this.moveDrag.apply(this, [ev])
        });

        if (ev.target === this.screenshot && this.marqueeRect.width && this.marqueeRect.height && !this.hitTest(ev.layerX, ev.layerY)) {
            this.rectangles.push(Object.assign({}, this.marqueeRect));
            redrawRectangles(this.rectangles);
            addInputZone(this.rectangles);
        }
    }

    moveDrag(ev) {
        let x = ev.layerX;
        let y = ev.layerY;
        let width = this.startX - x;
        let height = this.startY - y;
        if (width < 0) {
            width *= -1;
            x -= width;
        }
        if (height < 0) {
            height *= -1;
            y -= height;
        }
        Object.assign(this.marqueeRect, {x, y, width, height});
        drawRectangle(this.marquee, this.marqueeRect);
    }

    hitTest(x, y) {
        return this.rectangles.find(rect => (
            x >= rect.x &&
            y >= rect.y &&
            x <= rect.x + rect.width &&
            y <= rect.y + rect.height
        ));
    }

}