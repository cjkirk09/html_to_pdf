var text;
var textafter;
function getText() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            var data = this.responseText;
            text = data;
            data = data.replace(/\n/g, '<br/>');
            textafter = data;
            window.document.getElementById('hobbit-text').innerHTML = data;
        }
    };
    xhttp.open("GET", "/hobbit-text", true);
    xhttp.send();
}

getText();