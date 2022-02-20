let button = document.getElementById("button")
let image = document.getElementById("image");


button.addEventListener("click", async function(){
    let results = await fetch('http://127.0.0.1:5000/hello',{
        methods: 'GET'
    });
    let decoded = (await results.json())
    image.src = decoded[Math.floor(Math.random() * decoded.length)]
    image.style.height = "auto"
    image.style.width = "400px"
})

