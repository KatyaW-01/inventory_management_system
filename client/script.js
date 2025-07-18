fetch(("http://127.0.0.1:5000/inventory"))
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
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
  .then(renderEvent)
})

function renderEvent(event) {
  const div = document.createElement("div")
  div.classList.add("product-card")

  const header = document.createElement("h2")
  header.textContent = event.product

  const price = document.createElement("p")
  price.textContent = `Price: $${event.price}`

  const stock = document.createElement("p")
  stock.textContent = `Stock: ${event.stock}`

  div.appendChild(header)
  div.appendChild(price)
  div.appendChild(stock)
  
  document.querySelector("#inventory-items").appendChild(div)
}
