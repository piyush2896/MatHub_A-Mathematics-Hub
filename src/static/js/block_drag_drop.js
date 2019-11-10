$(document).ready(function () {
    $('body').attr("mode", "maker");
    Blockly.inject('blockly-div', {
        toolbox: document.getElementById('toolbox'),
        toolboxPosition: 'start',
        horizontalLayout: true,
        scrollbars: false,
        horizontalLayout: false
    });

    document.getElementById('file_upload').addEventListener('change', handleFileSelection, false);
    $('#fab_btn_upload').click(function(){
        $('#file_upload').click();
    });

    $('#fab_btn_upload').hover(function(){
        $('#speech').text("Upload your old workspace");
    }, function() {
        $('#speech').text("Hello, there!");
    });

    $('#fab_btn_download').hover(function(){
        $('#speech').text("Download your current workspace");
    }, function() {
        $('#speech').text("Hello, there!");
    });

    $('#fab_btn_erase').hover(function(){
        $('#speech').text("Clear your current workspace");
    }, function() {
        $('#speech').text("Hello, there!");
    });

    $('#fab_btn_play').hover(function(){
        $('#speech').text("Run your current workspace");
    }, function() {
        $('#speech').text("Hello, there!");
    });

    $('#fab_btn_play').click(function() {
        var code = Blockly.Python.workspaceToCode(Blockly.getMainWorkspace());
        console.log(code);
    })
});

function clearWorkspace() {
    Blockly.getMainWorkspace().clear();
    $('#speech').text("Hello, there!");
}

function loadWorkspace(xml) {
    clearWorkspace();
    Blockly.Xml.domToWorkspace(xml, Blockly.getMainWorkspace());
}

function workspaceToXml() {
    return Blockly.Xml.workspaceToDom(Blockly.getMainWorkspace());
}

function generateFilename() {
    var today = new Date();
    var time = today.getHours() + "-" + today.getMinutes() + "-" + today.getSeconds();
    return time + '.xml'
}

function downloadWordkspace() {
    let workspaceXML = workspaceToXml();
    var element = document.createElement('a');
    var bb = new Blob([workspaceXML.outerHTML], {type: 'text/plain'});
    element.style.display = 'none';
    element.setAttribute('href', window.URL.createObjectURL(bb));
    element.setAttribute('download', generateFilename());
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

function handleFileSelection(evt){
    var file = evt.target.files[0];
    console.log(file);
    var reader = new FileReader();
    if(!file.type.match("text/xml")){
        alert("Not a correct file!");
    }else{
        reader.readAsText(file);
        reader.onloadend = function(){
            xmlDom = Blockly.Xml.textToDom("<xml>" + $(reader.result).html() + "</xml>");
            console.log(xmlDom)

            loadWorkspace(xmlDom);
        };
    }
}
