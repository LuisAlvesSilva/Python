function buscarCEP() {
    var cepInput = document.getElementById('cepInput').value;
    var resultDiv = document.getElementById('result');

    // Limpar resultados anteriores
    resultDiv.innerHTML = '';

    // Validar o formato do CEP
    var cepPattern = /^\d{5}-?\d{3}$/;
    if (!cepPattern.test(cepInput)) {
        resultDiv.innerHTML = '<p class="error">CEP inválido. Digite no formato correto.</p>';
        return;
    }

    // Fazer requisição para a API ViaCEP
    var url = 'https://viacep.com.br/ws/' + cepInput + '/json/';
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if ('erro' in data) {
                resultDiv.innerHTML = '<p class="error">' + data.erro + '</p>';
            } else {
                resultDiv.innerHTML = '<p><strong>CEP:</strong> ' + data.cep + '</p>' +
                                      '<p><strong>Logradouro:</strong> ' + data.logradouro + '</p>' +
                                      '<p><strong>Bairro:</strong> ' + data.bairro + '</p>' +
                                      '<p><strong>Cidade:</strong> ' + data.localidade + '</p>' +
                                      '<p><strong>Estado:</strong> ' + data.uf + '</p>' +
                                      '<p><strong>DDD:</strong> ' + data.ddd + '</p>';
            }
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
            resultDiv.innerHTML = '<p class="error">Erro na requisição. Tente novamente mais tarde.</p>';
        });
}
