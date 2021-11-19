var rectangles = [];

var load_rect = (event) => {
    const $ = document.querySelector.bind(document);

    /**
     * Collection of rectangles defining user generated regions
     */

    rectangles = []
    // DOM elements
    const $screenshot = $('#screenshot');
    const $draw = $('#draw');
    const $marquee = $('#marquee');
    const $boxes = $('#boxes');

    document.getElementById("draw").setAttribute("width", $screenshot.width)
    document.getElementById("draw").setAttribute("height", $screenshot.height)
    document.getElementById("draw").setAttribute("viewBox", "0 0 " + $screenshot.width + " " + $screenshot.height);

    // Temp variables
    let startX = 0;
    let startY = 0;
    const marqueeRect = {
        x: 0,
        y: 0,
        width: 0,
        height: 0,
    };

    console.log($screenshot);
    $marquee.classList.add('hide');
    $screenshot.addEventListener('pointerdown', startDrag);

    function startDrag(ev) {
        if (hitTest(ev.layerX, ev.layerY))
            return;
        // middle button delete rect
        if (ev.button === 1) {
            const rect = hitTest(ev.layerX, ev.layerY);
            if (rect) {
                rectangles.splice(rectangles.indexOf(rect), 1);
                redraw();
            }
            return;
        }
        window.addEventListener('pointerup', stopDrag);
        $screenshot.addEventListener('pointermove', moveDrag);
        $marquee.classList.remove('hide');
        startX = ev.layerX;
        startY = ev.layerY;
    }

    function stopDrag(ev) {
        $marquee.classList.add('hide');
        window.removeEventListener('pointerup', stopDrag);
        $screenshot.removeEventListener('pointermove', moveDrag);
        if (ev.target === $screenshot && marqueeRect.width && marqueeRect.height && !hitTest(ev.layerX, ev.layerY)) {
            rectangles.push(Object.assign({}, marqueeRect));
            redraw();
        }
        console.log(rectangles)
    }

    function moveDrag(ev) {
        let x = ev.layerX;
        let y = ev.layerY;
        let width = startX - x;
        let height = startY - y;
        if (width < 0) {
            width *= -1;
            x -= width;
        }
        if (height < 0) {
            height *= -1;
            y -= height;
        }
        Object.assign(marqueeRect, {x, y, width, height});
        drawRect($marquee, marqueeRect);
    }

    function hitTest(x, y) {
        return rectangles.find(rect => (
            x >= rect.x &&
            y >= rect.y &&
            x <= rect.x + rect.width &&
            y <= rect.y + rect.height
        ));
    }

    function redraw() {
        boxes.innerHTML = '';
        rectangles.forEach((data) => {
            boxes.appendChild(drawRect(
                document.createElementNS("http://www.w3.org/2000/svg", 'rect'), data
            ));
        });
    }

    function drawRect(rect, data) {
        const {x, y, width, height} = data;
        rect.setAttributeNS(null, 'width', width);
        rect.setAttributeNS(null, 'height', height);
        rect.setAttributeNS(null, 'x', x);
        rect.setAttributeNS(null, 'y', y);
        return rect;
    }
};

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            const image = new Image();
            image.src = e.target.result;
            image.onload = function () {
                // access image size here
                console.log(this.width);
                console.log(this.height);
                $("#screenshot")
                    .attr('src', e.target.result)
                    // .attr("width" , this.width)
                    // .attr("height" , this.height)
                    .attr('onload', load_rect)
            };
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function postToServer(masterKey) {
    var fd = new FormData();
    console.log($('#file'));
    var files = $('#file')[0].files;

    // Check file selected or not
    if (files.length > 0) {
        fd.append('photo', files[0]);
        fd.append('zones', masterKey)
        $.ajax({
            url: 'obfuscate',
            type: 'post',
            data: fd,
            contentType: false,
            processData: false,
        });
    }
}

function submitRect() {
    let masterkey = {}
    masterkey.zones = []
    for (let coord of rectangles) {
        console.log(coord);
        let zone = {}
        zone['coordinates'] = [[coord.y, coord.x], [coord.y + coord.height, coord.x + coord.width]];
        let layers = []
        let layer = {'alg_id': 1, 'key_data': {'key': "parola123"}}

        layers.push(layer);
        zone['layers'] = layers;
        masterkey.zones.push(zone);
    }


    postToServer(JSON.stringify(masterkey));
}