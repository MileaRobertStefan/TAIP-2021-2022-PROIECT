import {FacesDetector} from "./faces_detector";
import {readURL, submitRect} from "./obfuscation_utils";
import {addDeobfuscationInputZone, sendToDeofuscationApi} from "./deobfuscation_utils";

(() => {
    window.location.pathname.includes("deobfuscate") ? addDeobfuscationPageEvents() : addObfuscationPageEvents();

})()


function addObfuscationPageEvents() {
    document.getElementById("file").addEventListener('input', (e) => {
        readURL(e.target);
    });

    document.getElementById("face-detect").addEventListener('click', () => {
        new FacesDetector(window.rectangleDrawer).postToServerForFaceDetection();
    });

    document.getElementById("submit-rect").addEventListener('click', () => {
        submitRect();
    });
}

function addDeobfuscationPageEvents() {
    document.getElementById("deobfuscation-input-container").addEventListener('click', () => {
        addDeobfuscationInputZone();
    });

    document.getElementById("submit-input-zones").addEventListener('click', () => {
        sendToDeofuscationApi();
    });
}