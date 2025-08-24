// Fetch notices from API and display
let allCirculars = [];

async function loadCirculars() {
  try {
    const response = await fetch("/circulars/api/");
    allCirculars = await response.json();
    displayCirculars(allCirculars);
  } catch (error) {
    console.error("Error loading circulars:", error);
  }
}

function displayCirculars(circulars) {
  const container = document.getElementById("circularsContainer");
  container.innerHTML = "";

  if (circulars.length === 0) {
    container.innerHTML = `<p style="text-align:center;">No circulars found.</p>`;
    return;
  }

  circulars.forEach(c => {
    const card = document.createElement("div");
    card.className = "circular-card";

    card.innerHTML = `
        <h3>${c.subject}</h3>
        <p>${c.content.substring(0, 100)}...</p>
        <p><strong>To:</strong> ${c.to_list}</p>
        <p><strong>CC:</strong> ${c.copy_list}</p>
        <p class="meta">Published: ${c.created_at}</p>
        <a href="/notice/${c.id}/" class="view-btn">
            <i class="fas fa-eye"></i> View
        </a>
        `;

    container.appendChild(card);
  });
}

// Apply filters
function applyFilters() {
  const filterTo = document.getElementById("filterTo").value;
  const filterDate = document.getElementById("filterDate").value;

  let filtered = allCirculars;

  if (filterTo) {
    filtered = filtered.filter(c => c.to_list.includes(filterTo));
  }

  if (filterDate) {
    filtered = filtered.filter(c => c.created_at.includes(formatDate(filterDate)));
  }

  displayCirculars(filtered);
}

// Reset filters
function resetFilters() {
  document.getElementById("filterTo").value = "";
  document.getElementById("filterDate").value = "";
  displayCirculars(allCirculars);
}

// Format date for comparison
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-GB", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  });
}

// Initial load
document.addEventListener("DOMContentLoaded", loadCirculars);


