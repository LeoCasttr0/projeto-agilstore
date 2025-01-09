(function(win, doc) {
    'use strict';

    // Verifica se o usuário quer mesmo apagar o dado
    if (doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel');
        for (let i = 0; i < btnDel.length; i++) {
            // Adiciona o evento de clique para cada botão
            btnDel[i].addEventListener('click', function (event) {
                if (confirm('Deseja mesmo apagar este dado ?')) {
                    return true;

                } else {
                    event.preventDefault();
                }
            });
        }
    }

})(window, document);