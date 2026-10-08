fetch("/api/data")
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("project-list");
    data.forEach(project => {
      const card = document.createElement("div");
      card.className = "col";
      card.innerHTML = `
        <div class="card h-100 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">${project.title}</h5>
            <p class="card-text">${project.description}</p>
          </div>
        </div>
      `;
      container.appendChild(card);
    });
  });