document.addEventListener('DOMContentLoaded', function () {
    const locations = [
        "Faridabad, Haryana", "Jhajjar, Haryana", "Gurugram, Haryana", "Sonipat, Haryana",
        "Aligarh, Uttar Pradesh", "Bahadurgarh, Haryana", "Sikandrabad, Uttar Pradesh",
        "Gohana, Haryana", "Baraut, Uttar Pradesh", "Rohtak, Haryana", "Panipat, Haryana",
        "Karnal, Haryana", "Baghpat, Uttar Pradesh", "Bulandshahr, Uttar Pradesh",
        "Hapur, Uttar Pradesh", "Meerut, Uttar Pradesh", "Palwal, Haryana", "Rewari, Haryana"
    ];

    const crops = [
        "Paddy (Common)", "Paddy (Grade A)", "Maize", "Jowar (Hybrid)",
        "Jowar (Maldandi)", "Bajra", "Arhar (Tur)", "Moong", "Urad",
        "Groundnut", "Cotton (Medium Staple)", "Cotton (Long Staple)",
        "Wheat", "Sugarcane", "Mustard", "Gram (Chana)", "Lentil (Masur)",
        "Barley", "Safflower"
    ];

    // Simulate data generation based on Python script's logic
    // This provides a visual representation similar to what the Python script would produce.
    const demandData = [];
    for (let i = 0; i < locations.length; i++) {
        const row = [];
        const loc = locations[i];
        for (let j = 0; j < crops.length; j++) {
            const crop = crops[j];
            let score = Math.floor(Math.random() * 3) + 1; // Base random score 1-3 for unrefined

            // Refinement logic (simplified from Python)
            if (crop === "Wheat") score = Math.random() > 0.3 ? 5 : 4;
            else if (crop === "Paddy (Common)" || crop === "Paddy (Grade A)") score = Math.floor(Math.random() * 3) + 3; // 3,4,5
            else if (crop === "Sugarcane") {
                if (loc.includes("Uttar Pradesh") || ["Karnal, Haryana", "Sonipat, Haryana", "Panipat, Haryana", "Rohtak, Haryana"].includes(loc)) {
                    score = 5;
                } else if (["Faridabad, Haryana", "Gurugram, Haryana", "Bahadurgarh, Haryana"].includes(loc)) {
                    score = Math.random() > 0.5 ? 2 : 1;
                } else {
                    score = Math.floor(Math.random() * 3) + 2; // 2,3,4
                }
            }
            else if (crop === "Cotton (Medium Staple)" || crop === "Cotton (Long Staple)") {
                 if (["Panipat, Haryana", "Gurugram, Haryana", "Faridabad, Haryana", "Meerut, Uttar Pradesh", "Aligarh, Uttar Pradesh"].includes(loc)) {
                    score = Math.random() > 0.3 ? 5 : 4;
                 } else if (["Rohtak, Haryana", "Sonipat, Haryana"].includes(loc)) {
                    score = Math.random() > 0.5 ? 4 : 3;
                 } else {
                    score = Math.floor(Math.random() * 3) + 1; // 1,2,3
                 }
            }
            else if (crop === "Mustard") score = Math.floor(Math.random() * 3) + 3; // 3,4,5
            else if (crop === "Maize") score = Math.floor(Math.random() * 3) + 2; // 2,3,4
            else if (["Arhar (Tur)", "Moong", "Urad", "Gram (Chana)", "Lentil (Masur)"].includes(crop)) score = Math.floor(Math.random() * 3) + 2; // 2,3,4
            else if (["Jowar (Hybrid)", "Jowar (Maldandi)", "Bajra"].includes(crop)) score = Math.floor(Math.random() * 3) + 1; // 1,2,3
            else if (crop === "Groundnut") score = Math.random() > 0.5 ? 3 : 2;
            else if (crop === "Barley") {
                score = Math.floor(Math.random() * 3) + 1; // 1,2,3
                if (["Gurugram, Haryana", "Sonipat, Haryana", "Faridabad, Haryana"].includes(loc)) {
                     score = Math.random() > 0.5 ? 4 : 3;
                }
            }
            else if (crop === "Safflower") score = Math.floor(Math.random() * 3); // 0,1,2

            row.push(Math.min(5, Math.max(0, Math.round(score)))); // Ensure score is integer within 0-5
        }
        demandData.push(row);
    }

    const container = document.getElementById('heatmap-container');
    if (!container) {
        console.error("Heatmap container not found!");
        return;
    }
    const table = document.createElement('table');

    // Create table header (crops)
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    const thCorner = document.createElement('th');
    thCorner.textContent = "Location / Crop"; // Label for the corner cell
    headerRow.appendChild(thCorner);

    crops.forEach(crop => {
        const th = document.createElement('th');
        th.textContent = crop;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body (locations and demand scores)
    const tbody = document.createElement('tbody');
    locations.forEach((location, i) => {
        const tr = document.createElement('tr');
        const thLoc = document.createElement('th'); // Location name cell (as a header in the row)
        thLoc.textContent = location;
        tr.appendChild(thLoc);

        demandData[i].forEach(score => {
            const td = document.createElement('td');
            td.textContent = score;
            td.className = `score-${score}`; // Apply class for color coding
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    container.appendChild(table);
});