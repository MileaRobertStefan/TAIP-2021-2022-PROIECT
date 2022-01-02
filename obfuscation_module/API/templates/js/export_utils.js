import {addDeobfuscationInputZone} from "./deobfuscation_utils";

export function readTextFile(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            let local_master_key = JSON.parse(e.target.result)
            Object.keys(local_master_key.zone_keys).forEach((key) => {
                addDeobfuscationInputZone(local_master_key.zone_keys[key]);
            })
            window.img_id = local_master_key.image_id
            document.getElementById("screenshot").setAttribute("src", "/images/" + local_master_key.image_id + ".png")
        }

        reader.readAsText(input.files[0]);
    }
}

export function saveStaticDataToFile() {
    let local_master_key = JSON.parse(JSON.stringify(window.global_master_key));
    for (const zone in local_master_key['zone_keys']) {
        let id = zone.replace("zone_", "")
        if (!document.getElementById("checkbox-zone-" + id).checked) {
            delete local_master_key['zone_keys'][zone]
        }
    }
    const blob = new Blob([JSON.stringify(local_master_key)],
        {type: "text/plain;charset=utf-8"});
    saveAs(blob, "exportKeys.txt");
}