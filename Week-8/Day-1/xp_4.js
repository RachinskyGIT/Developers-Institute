        // Function to calculate the volume of a sphere
        function calculateVolume(radius) {
            return (4 / 3) * Math.PI * Math.pow(radius, 3);
        }

        // Event listener for form submission
        document.getElementById("MyForm").addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent form submission

            // Get the input value
            var radius = parseFloat(document.getElementById("radius").value);

            // Calculate the volume
            var volume = calculateVolume(radius);

            // Display the volume
            document.getElementById("volume").value = volume.toFixed(2);
        });