const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.post('/run', (req, res) => {
    const code = req.body.code;
    const filename = 'temp.c';
    const outputExe = 'temp.out';

    // 1. Salva o código em um arquivo .c
    fs.writeFileSync(filename, code);

    // 2. Comanda o GCC para compilar e depois executar
    exec(`gcc ${filename} -o ${outputExe} && ./${outputExe}`, (error, stdout, stderr) => {
        // Limpeza dos arquivos temporários
        if (fs.existsSync(filename)) fs.unlinkSync(filename);
        if (fs.existsSync(outputExe)) fs.unlinkSync(outputExe);

        if (error) {
            return res.json({ error: stderr || error.message });
        }
        res.json({ output: stdout });
    });
});

app.listen(3000, () => console.log('Servidor rodando em http://localhost:3000'));