const testFolder = __dirname;
const fs = require('fs');
const path = require('path')
const {spawn} = require('child_process')

function getUrl(file) {
    const contents = fs.readFileSync(file, 'utf8')

    contents.split(/\r?\n/).forEach(line => {
    let matches = line.match('/^(https?:\/\/)/g');

        if (matches) {
            return matches[0]
        }
    })
    
}

function spawnVim(file) {
    let terminal = spawn('cat', [file]);

    terminal.stdout.on("data", data => {
        console.log(`stdout: ${data.toString()}`)
    })

    terminal.on("error", data => {
        console.log(` ${data}`)
    })

}

fs.readdir(testFolder, (err, files) => {
    let url;

    files.forEach(file => {
      let url = getUrl(file);
      if (path.extname(file) === '.webloc') {   
        spawnVim(url)
      }
  });
});