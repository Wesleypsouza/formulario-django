let botaoBaixar = document.getElementById("botaobaixar")

botaoBaixar.addEventListener("click", () => {
    let campoEmail = document.getElementById("campoemail")
    let campoData = document.getElementById("campodata")

    campoEmail.removeAttribute("required")
    campoData.removeAttribute("required")

    window.open("/cadastro/baixar-dados")
})