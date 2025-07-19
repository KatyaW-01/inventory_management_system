//get all products
fetch(("http://127.0.0.1:5000/inventory"))
  .then(response => response.json())
  .then(inventory => {
    inventory.forEach(renderInventory);
  })

//add new product
document.querySelector("form").addEventListener("submit", (event) => {
  event.preventDefault()
  const product = document.querySelector("#product-name").value
  const price = document.querySelector("#price").value 
  const stock = document.querySelector("#stock").value 

  fetch("http://127.0.0.1:5000/inventory", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify( { product, price, stock })
  })
  .then(response => response.json())
  .then(renderInventory)
})

//delete a product
document.addEventListener("click", (event) => {
  if (event.target.classList.contains("del-button")) {
    const id = event.target.dataset.id

    fetch(`http://127.0.0.1:5000/inventory/${id}`, {
      method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
      if(data.message == "Product deleted") {
        const productCard = event.target.closest(".product-card")
        if(productCard) {
          productCard.remove()
        }
      } else {
        console.log("Error removing product")
      }
    })
  }
  if (event.target.classList.contains('add-info')) {
    event.preventDefault()
    const productCard = event.target.closest(".product-card")
    const form_value = productCard.querySelector(".add-new-info").value
    const barcode = parseInt(form_value)
    fetch(`http://127.0.0.1:5000/${barcode}`)
    .then(response => response.json())
    .then(data => {
      const product_paragraph = document.querySelector(`.id-${event.target.dataset.id}`)
      product_paragraph.textContent = `Ingredients: ${data.ingredients}`
    })
    .catch(error => console.log(error))
  }
})

//display products
function renderInventory(event) {
  const div = document.createElement("div")
  div.setAttribute("class", "product-card")

  const header = document.createElement("h2")
  header.textContent = event.product

  const price = document.createElement("p")
  price.textContent = `Price: $${event.price}`

  const stock = document.createElement("p")
  stock.textContent = `Stock: ${event.stock}`

  const paragraph = document.createElement("p")
  paragraph.setAttribute("class", `id-${event.id}`) 

  const button = document.createElement("button")
  button.setAttribute("class", "del-button")
  button.dataset.id = event.id
  button.textContent = 'Delete'

  const form = document.createElement("form")
  form.setAttribute("class", "product-form")

  const input = document.createElement("input")
  input.setAttribute("type", "text")
  input.setAttribute("placeholder", "Enter barcode")
  input.setAttribute("name", "barcode")
  //input.id = "add-new-info"
  input.setAttribute("class", "add-new-info")

  const submit = document.createElement("button")
  submit.setAttribute("class", "add-info")
  submit.setAttribute("type", "submit")
  submit.dataset.id = event.id 
  submit.textContent = "Add Info"

  form.appendChild(input)
  form.appendChild(submit)

  div.appendChild(header)
  div.appendChild(price)
  div.appendChild(stock)
  div.appendChild(paragraph)
  div.appendChild(form)
  div.appendChild(button)
  
  document.querySelector("#inventory-items").appendChild(div)
}
