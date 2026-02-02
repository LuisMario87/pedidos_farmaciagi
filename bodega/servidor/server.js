const express = require('express');
const fileUpload = require('express-fileupload');
const app = express();

app.use(fileUpload());

app.post('/enviar-pedido', (req, res) => {
  const archivo = req.files.pedido;
  archivo.mv(`./pedidos/${archivo.name}`);
  res.send('Pedido recibido');
});

app.listen(3000);
