document.addEventListener('DOMContentLoaded', function() {
    // Remoção de itens
    document.querySelectorAll('.remover-btn').forEach(btn => {
        btn.addEventListener('click', async function() {
            const ip = this.getAttribute('data-ip');
            
            try {
                const response = await fetch(`/remover_ip/${ip}`, {
                    method: 'DELETE'
                });
                
                const result = await response.json();
                alert(result.message);
                location.reload();
            } catch(error) {
                console.error('Erro ao remover:', error);
                alert('Erro ao remover registro');
            }
        });
    });

    // Carregar dados via API
    document.getElementById('carregarDados').addEventListener('click', async () => {
        const resultDiv = document.getElementById('apiResult');
        resultDiv.innerHTML = '<p>Carregando...</p>';

        try {
            const response = await fetch('/get_nomes');
            const data = await response.json();

            let html = '<table><tr><th>Nome</th><th>IP</th><th>Data</th></tr>';
            
            data.forEach(item => {
                html += `
                    <tr>
                        <td>${item.nome}</td>
                        <td>${item.ip}</td>
                        <td>${item.data}</td>
                    </tr>
                `;
            });
            
            html += '</table>';
            resultDiv.innerHTML = html;
        } catch(error) {
            resultDiv.innerHTML = `<p class="error">Erro: ${error.message}</p>`;
        }
    });
});