import {RectanglesDrawer} from "./rectangles_drawer";

let image_width, image_height;

export function readURL(input) {
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
                    .attr('onload', () => {
                        window.rectangleDrawer = new RectanglesDrawer(image_height, image_width)
                    })
            };
        };

        reader.readAsDataURL(input.files[0]);
    }
}

export function submitRect() {
    let masterkey = {}
    let image_height_ratio = window.rectangleDrawer.image_height_ratio;
    let image_width_ratio = window.rectangleDrawer.image_width_ratio;

    masterkey.zones = []
    let i = 0;
    for (let coord of window.rectangleDrawer.rectangles) {
        i += 1
        console.log(coord);
        let zone = {}
        zone['coordinates'] = [[(coord.y * image_height_ratio) | 0, (coord.x * image_width_ratio) | 0], [((coord.y + coord.height) * image_height_ratio) | 0, ((coord.x + coord.width) * image_width_ratio) | 0]];
        let layers = []
        const id = document.getElementById("input-zone-" + i).getElementsByTagName("select")[0].value
        let layer = {'alg_id': id, 'key_data': {'key': "parola123"}}

        layers.push(layer);
        zone['layers'] = layers;
        masterkey.zones.push(zone);
    }

    console.log(masterkey);
    postToServer(JSON.stringify(masterkey));
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

function showObfuscateLink(img_name) {
    $("#link-to-obfuscate-pic")
        .attr("href", "/deobfuscate-page?image-name=" + img_name.toString() + ".png")
        .css("display", "inline")
        .html("Click here to go to the obfuscated picture")
}