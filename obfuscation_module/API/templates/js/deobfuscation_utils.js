
export function addDeobfuscationInputZone(text = ''){
    const inputZones = document.getElementById("input-zones");
    const zoneNumber = inputZones.childElementCount;

    const container = document.createElement('deobfuscator-input-container');
    const inputZone = document.createElement("div");

    const input = document.createElement("input");
    input.setAttribute("class", "generated-key");
    input.setAttribute("value", text);

    input.setAttribute("id", "input-zone-" + (zoneNumber + 1));
    container.appendChild(inputZone);
    inputZone.appendChild(input)

    inputZones.appendChild(container)
}

export function sendToDeofuscationApi(){
    let fd = new FormData();
    let image_id;
    if (window.img_id) {
        image_id = window.img_id
    } else {
        let urlParams = new URLSearchParams(window.location.search);
        image_id = urlParams.get('image-name').replace(".png", "")
        window.img_id = image_id
    }


    fd.append('image_id', image_id);
    fd.append("zones", getKeysFromInputZones());
    $.ajax({
        url: 'deobfuscate',
        type: 'post',
        data: fd,
        contentType: false,
        processData: false,
    }).done((data) => {
        $("#screenshot2")
            .attr('src', "data:image/png;base64," + data)
    });
}

function replaceAll(str, find, replace) {
    return str.replace(new RegExp(find, 'g'), replace);
}

function getKeysFromInputZones() {
    let master_key = {}
    let kk = document.getElementById("input-zones").childElementCount;

    for (let i = 1; i <= kk; i++) {
        let text = document.getElementById("input-zone-" + i).value;
        if (text !== '')
            master_key["zone_" + i] = text
    }

    master_key = replaceAll(JSON.stringify(master_key), "\\\\\\\\", "\\")
    return master_key;
}


