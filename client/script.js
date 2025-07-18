fetch(("http://127.0.0.1:5000/inventory"))
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
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
