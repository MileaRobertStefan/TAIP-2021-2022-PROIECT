const obfuscatorsOptionsList = ["Affine", "Encryption", "Scramble", "Color", "Puzzle", "XOR"];

export const drawRectangle = (rectangleContainer, rectangleData) => {
    const { x, y, width, height } = rectangleData;
    rectangleContainer.setAttributeNS(null, 'width', width);
    rectangleContainer.setAttributeNS(null, 'height', height);
    rectangleContainer.setAttributeNS(null, 'x', x);
    rectangleContainer.setAttributeNS(null, 'y', y);
    return rectangleContainer;
};

export const redrawRectangles = (rectangles) => {
    const boxes = document.getElementById("boxes");

    boxes.innerHTML = "";

    rectangles.forEach((rectangle, idx) => {
        boxes.appendChild(drawRectangle(
            document.createElementNS("http://www.w3.org/2000/svg", 'rect'), rectangle
        ));
        appendTextToRectangle(rectangle, idx + 1);
    });
};

export function addInputZone(rectangles) {
        const container = document.createElement('obfuscator-input-container');
        container.setAttribute("id", "input-zone-" + rectangles.length);
        container.setAttribute("class", "cull-center")

        container.appendChild(getCheckbox(rectangles))
        container.appendChild(getObfuscatorInput());
        container.appendChild(getGeneratedKeyField(rectangles));
        container.appendChild(getCopyButton(rectangles));

        document.getElementById("input-zones").appendChild(container);
}

function getCheckbox(rectangles) {
    const label = document.createElement("label")
    label.setAttribute("class", "container")

    const inputBox = document.createElement('input');
    inputBox.setAttribute("type", "checkbox")
    inputBox.setAttribute("checked", "checked")
    inputBox.setAttribute("id", "checkbox-zone-" + rectangles.length);

    const span = document.createElement("span")
    span.setAttribute("class", "checkmark")

    label.appendChild(inputBox)
    label.appendChild(span)
    return label
}

const appendTextToRectangle = (rectangle, text) => {
    const canvas = document.createElement("canvas");
    const canvasContext = canvas.getContext("2d");
    const textWidth = canvasContext.measureText(text).width;

    const svgNS = "http://www.w3.org/2000/svg";
    const textContainer = document.createElementNS(svgNS, "text");

    textContainer.setAttributeNS(null, "x", ((rectangle.x + rectangle.width / 2) - (textWidth / 2)).toString());
    textContainer.setAttributeNS(null, "y", (rectangle.y + rectangle.height / 2) + 16 / 2);

    const textNode = document.createTextNode(text);
    textContainer.appendChild(textNode);
    document.querySelector("#boxesTexts").appendChild(textContainer);
};


function getCopyButton(rectangles){
    const button = document.createElement("div");
    const i = rectangles.length;
    button.setAttribute("class", "copy");
    button.addEventListener("click", ()=>{ copy(i); });
    button.innerText = "Copy";
    return button;
}

function getGeneratedKeyField(rectangles){
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
    selectElement.setAttribute("multiple", "multiple");

    for (let i=0; i<obfuscatorsOptionsList.length; i++){
        const option = document.createElement("option");
        option.setAttribute("value", i.toString());
        option.innerText = obfuscatorsOptionsList[i];
        selectElement.appendChild(option);
    }

    return selectElement;
}

function copy(i) {
    console.log(i);
    const copyText = $('.generated-key')[i - 1]
    navigator.clipboard.writeText(copyText.innerHTML);
}