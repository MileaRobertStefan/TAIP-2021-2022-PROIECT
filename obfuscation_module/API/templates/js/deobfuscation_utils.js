
export function addDeobfuscationInputZone(){
    const inputZones = document.getElementById("input-zones");
    const zoneNumber = inputZones.childElementCount;

    const container = document.createElement('deobfuscator-input-container');
    const inputZone = document.createElement("div");
    inputZone.setAttribute("id", "input-zone-" + (zoneNumber + 1));

    const input = document.createElement("input");
    input.setAttribute("class", "generated-key");

    container.appendChild(inputZone);
    inputZone.appendChild(input)

    inputZones.appendChild(container)
}

export function sendToDeofuscationApi(){
}