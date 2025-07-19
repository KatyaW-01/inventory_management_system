fetch(("http://127.0.0.1:5000/inventory"))
  .then(response => response.json())
  .then(inventory => {
    inventory.forEach(renderInventory);
  })

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

document.addEventListener("click", (event) => {
  if (event.target.classList.contains("del-button")) {
    const id = event.target.dataset.id

    fetch(`http://127.0.0.1:5000/inventory/${id}`, {
      method: "DELETE"
    })
    .then(response => response.json())
    .then(renderInventory)
  }
})

function renderInventory(event) {
  const div = document.createElement("div")
  div.setAttribute("class", "product-card")

  const header = document.createElement("h2")
  header.textContent = event.product

  const price = document.createElement("p")
  price.textContent = `Price: $${event.price}`

  const stock = document.createElement("p")
  stock.textContent = `Stock: ${event.stock}`

  const button = document.createElement("button")
  button.setAttribute("class", "del-button")
  button.dataset.id = event.id
  button.textContent = 'Delete'

  div.appendChild(header)
  div.appendChild(price)
  div.appendChild(stock)
  div.appendChild(button)
  
  document.querySelector("#inventory-items").appendChild(div)
}
