
const obfuscatorsOptionsList = ["Affine", "Encryption", "Scramble", "Color", "Puzzle", "XOR"];
var rectangles = [];
var zones = []
var image_width, image_height;
var image_width_ratio, image_height_ratio;
var load_rect = (event) => {
    const $ = document.querySelector.bind(document);

    /**
     * Collection of rectangles defining user generated regions
     */

    rectangles = []
    redraw()
    document.getElementById("input-zones").innerHTML = ''

    // DOM elements
    const $screenshot = $('#screenshot');
    const $draw = $('#draw');
    const $marquee = $('#marquee');
    const $boxes = $('#boxes');
    const $boxesText = $('#boxesText');

    document.getElementById("draw").setAttribute("width", $screenshot.width)
    document.getElementById("draw").setAttribute("height", $screenshot.height)
    document.getElementById("draw").setAttribute("viewBox", "0 0 " + $screenshot.width + " " + $screenshot.height);

    image_width_ratio = image_width / $screenshot.width
    image_height_ratio = image_height / $screenshot.height

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
            addInputZone()
        }
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
        boxesTexts.innerHTML = '';
        let i = 0
        rectangles.forEach((data) => {
            i += 1
            boxes.appendChild(drawRect(
                document.createElementNS("http://www.w3.org/2000/svg", 'rect'), data
            ));
            appendTextToRect(data, i)
        });
    }

    function appendTextToRect(data, i) {
        fontSize = 30
        font = fontSize + "px times new roman";

        canvas = document.createElement("canvas");
        context = canvas.getContext("2d");
        context.font = font;
        width = context.measureText(i).width;

        var svgNS = "http://www.w3.org/2000/svg";
        var newText = document.createElementNS(svgNS, "text");
        newText.setAttributeNS(null, "x", (data.x + data.width / 2) - (width / 2));
        newText.setAttributeNS(null, "y", (data.y + data.height / 2) + 16 / 2);
        newText.setAttributeNS(null, "style", "text-shadow : -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white; " + "font:" + font);

        var textNode = document.createTextNode(i);
        newText.appendChild(textNode);
        boxesTexts.appendChild(newText);
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

function addInputZone() {
        const container = document.createElement('obfuscator-input-container');
        container.setAttribute("id", "input-zone-" + rectangles.length);

        container.appendChild(getObfuscatorInput());
        container.appendChild(getGeneratedKeyField());
        container.appendChild(getCopyButton());

        document.getElementById("input-zones").appendChild(container);
}

function getCopyButton(){
    const button = document.createElement("div");
    button.setAttribute("class", "copy");
    button.addEventListener("click", ()=>{copy(rectangles.length);});
    button.innerText = "Copy";
    return button;
}


function getGeneratedKeyField(){
    const div = document.createElement("div");
    div.setAttribute("class", "generated-key");
    div.innerText = "Zone " + rectangles.length + " Key";
    return div;
}

function getObfuscatorInput(){
        const selectWrapper = document.createElement('div');

        const customDropdown = document.createElement("span");
        customDropdown.setAttribute("class", "custom-dropdown");

        selectWrapper.append(customDropdown);
        customDropdown.appendChild(getObfuscatorsSelector());

        return selectWrapper;
}


function getObfuscatorsSelector(){
    const selectElement = document.createElement("select");
    selectElement.setAttribute("class", "fancy-selector");

    for (let i=0; i<obfuscatorsOptionsList.length; i++){
        const option = document.createElement("option");
        option.setAttribute("value", i.toString());
        option.innerText = obfuscatorsOptionsList[i];
        selectElement.appendChild(option);
    }
    return selectElement;
}

function addDeobfuscationInputZone(){
    $('#submit-input-zones').css("display", "inline");
    let el = document.createElement('html');
    el.innerHTML = "<div id='input-zone-"+rectangles.length+"' style ='display: flex; align-items: center'>" +
                        "<input class='generated-key' style='max-width: 300px; border-radius: 5px 5px 5px 5px;'/>"+
                    "</div>";
    document.getElementById("input-zones").appendChild(el)
}

function sendToDeofuscationApi(){
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            const image = new Image();
            image.src = e.target.result;
            image.onload = function () {
                // access image size here
                image_width = this.width;
                image_height = this.height;
                $("#screenshot")
                    .attr('src', e.target.result)
                    // .attr("width" , this.width)
                    // .attr("height" , this.height)
                    .attr('onload', load_rect)
            };

            const mainTag = document.getElementsByTagName("main")[0];
            const hasPictureClass = mainTag.classList.contains("main--has-picture");

            if (!hasPictureClass) {
                mainTag.classList.add("main--has-picture");
            }
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
        }).done((data) => {
            let i = 0
            data.image_id = JSON.parse(data.image_id)
            Object.keys(data.zone_keys).forEach((key) => {
                $('.generated-key')[i].innerHTML = data.zone_keys[key]
                i++;
            })
            showObfuscateLink(data.image_id)
        });
    }
}

function postToServerForFaceDetection() {
    var fd = new FormData();
    console.log($('#file'));
    var files = $('#file')[0].files;

    // Check file selected or not
    if (files.length > 0) {
        fd.append('photo', files[0]);
        $.ajax({
            url: 'http://localhost:5001/detection',
            type: 'post',
            data: fd,
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(response) {
                console.log(response);
                if (response.has_faces === true)
                    processDetectedFaces(response.coordinates);
            }
        });
    }
}

function submitRect() {
    let masterkey = {}
    masterkey.zones = []
    let i = 0;
    for (let coord of rectangles) {
        i += 1
        console.log(coord);
        let zone = {}
        zone['coordinates'] = [[(coord.y * image_height_ratio) | 0, (coord.x * image_width_ratio) | 0], [((coord.y + coord.height) * image_height_ratio) | 0, ((coord.x + coord.width) * image_width_ratio) | 0]];
        let layers = []
        id = document.getElementById("input-zone-" + i).getElementsByTagName("select")[0].value
        let layer = {'alg_id': id, 'key_data': {'key': "parola123"}}

        layers.push(layer);
        zone['layers'] = layers;
        masterkey.zones.push(zone);
    }


    postToServer(JSON.stringify(masterkey));
}

const appendTextToRectangle = (boxesTexts, rectangle, text) => {
    const font = "30px times new roman";
    const canvas = document.createElement("canvas");
    const canvasContext = canvas.getContext("2d");
    const textWidth = canvasContext.measureText(text).width;

    canvasContext.font = font;

    const svgNS = "http://www.w3.org/2000/svg";
    const textContainer = document.createElementNS(svgNS, "text");

    textContainer.setAttributeNS(null, "x", (rectangle.x + rectangle.width / 2) - (textWidth / 2));
    textContainer.setAttributeNS(null, "y", (rectangle.y + rectangle.height / 2) + 16 / 2);
    textContainer.setAttributeNS(null, "style", "text-shadow : -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white; " + "font:" + font);

    const textNode = document.createTextNode(text);
    textContainer.appendChild(textNode);
    boxesTexts.appendChild(textContainer);
};

const drawRectangle = (rectangleContainer, rectangleData) => {
    const { x, y, width, height } = rectangleData;
    rectangleContainer.setAttributeNS(null, 'width', width);
    rectangleContainer.setAttributeNS(null, 'height', height);
    rectangleContainer.setAttributeNS(null, 'x', x);
    rectangleContainer.setAttributeNS(null, 'y', y);
    return rectangleContainer;
};

const redrawRectangles = () => {
    const boxes = document.getElementById("boxes");
    const boxesText = document.getElementById("boxesText");

    boxes.innerHTML = "";
    boxesTexts.innerHTML = "";

    rectangles.forEach((rectangle, idx) => {
        boxes.appendChild(drawRectangle(
            document.createElementNS("http://www.w3.org/2000/svg", 'rect'), rectangle
        ));
        appendTextToRectangle(boxesTexts, rectangle, idx + 1);
    });
};

function faceDetection() {
    postToServerForFaceDetection();
}

function processDetectedFaces(coordinates) {
    console.log("obfuscating faces...");
    for (let coords of coordinates) {
         console.log("for coordinate...");
//         if (!hitTest(coords.top, coords.right)) {
            console.log(coords);
            rectangles.push({
                x: coords.left / image_width_ratio,
                y: coords.top / image_height_ratio,
                width: (coords.right - coords.left) / image_width_ratio,
                height: (coords.bottom - coords.top) / image_height_ratio
            });
            redrawRectangles();
            addInputZone();
//        }
    }
}
function copy(i) {
    copyText = $('.generated-key')[i - 1]
    navigator.clipboard.writeText(copyText.innerHTML);
}

function showObfuscateLink(img_name) {
    $("#link-to-obfuscate-pic")
        .attr("href", "/deobfuscate-page?image-name=" + img_name.toString() + ".png")
        .css("display", "inline-block")
        .html("Click here to go to the obfuscated picture")
}
