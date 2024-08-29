To download data from the client without requesting the server.

```
function download_data(data_to_download) {
        var data = new Blob([data_to_download], { type: 'text/plain' });
        var bloburl = window.URL.createObjectURL(data);

        const a = document.createElement('a');
        a.setAttribute('href', bloburl)
        a.setAttribute('download', 'filename.ext')
        a.style.display = 'none'
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a)
        window.URL.revokeObjectURL(bloburl);
    }

```

Usage

```
download_data("I love balloons")
```
