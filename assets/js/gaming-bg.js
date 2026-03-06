/**
 * Interactive Particle/Matrix Background for Gaming Light Mode
 * This script creates a floating particle network that reacts to the mouse.
 */

const canvas = document.getElementById('gaming-canvas');
const ctx = canvas.getContext('2d');

let particlesArray = [];
let mouse = {
    x: null,
    y: null,
    radius: 120 // Radius of interaction
};

window.addEventListener('mousemove', function (event) {
    mouse.x = event.x;
    mouse.y = event.y;
});

window.addEventListener('resize', function () {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
});

class Particle {
    constructor(x, y, directionX, directionY, size, color) {
        this.x = x;
        this.y = y;
        this.directionX = directionX;
        this.directionY = directionY;
        this.size = size;
        this.color = color;
    }

    // Method to draw individual particle
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
        ctx.fillStyle = this.color;
        ctx.fill();
    }

    // Check cursor position and move particle
    update() {
        // Reverse direction if hitting edge
        if (this.x > canvas.width || this.x < 0) {
            this.directionX = -this.directionX;
        }
        if (this.y > canvas.height || this.y < 0) {
            this.directionY = -this.directionY;
        }

        // Check collision detection - mouse position / particle position
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx * dx + dy * dy);

        // Push particles away
        if (distance < mouse.radius + this.size) {
            if (mouse.x < this.x && this.x < canvas.width - this.size * 10) {
                this.x += 1.5;
            }
            if (mouse.x > this.x && this.x > this.size * 10) {
                this.x -= 1.5;
            }
            if (mouse.y < this.y && this.y < canvas.height - this.size * 10) {
                this.y += 1.5;
            }
            if (mouse.y > this.y && this.y > this.size * 10) {
                this.y -= 1.5;
            }
            // Highlight particles near the mouse with the accent-glow color
            this.color = '#ff6b6b';
        } else {
            // Revert to Cyan/Base color if not near mouse
            this.color = '#00d2d3';
        }

        // Move particle
        this.x += this.directionX;
        this.y += this.directionY;

        // Draw particle
        this.draw();
    }
}

// Create particle array
function init() {
    particlesArray = [];
    let numberOfParticles = (canvas.height * canvas.width) / 10000;
    // Limit max particles to prevent lag
    if (numberOfParticles > 200) numberOfParticles = 200;
    if (numberOfParticles < 50) numberOfParticles = 50;

    for (let i = 0; i < numberOfParticles; i++) {
        let size = (Math.random() * 2) + 0.5;
        let x = (Math.random() * ((innerWidth - size * 2) - (size * 2)) + size * 2);
        let y = (Math.random() * ((innerHeight - size * 2) - (size * 2)) + size * 2);

        // Slower movement for background ambiance
        let directionX = (Math.random() * 1) - 0.5;
        let directionY = (Math.random() * 1) - 0.5;

        let color = '#00d2d3'; // Tactical Cyan default

        particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
    }
}

// Check if particles are close enough to draw line between them
function connect() {
    let opacityValue = 1;
    for (let a = 0; a < particlesArray.length; a++) {
        for (let b = a; b < particlesArray.length; b++) {
            let distance = ((particlesArray[a].x - particlesArray[b].x) * (particlesArray[a].x - particlesArray[b].x)) +
                ((particlesArray[a].y - particlesArray[b].y) * (particlesArray[a].y - particlesArray[b].y));

            // If close, draw line
            if (distance < (canvas.width / 7) * (canvas.height / 7)) {
                opacityValue = 1 - (distance / 15000);

                ctx.strokeStyle = `rgba(0, 210, 211, ${opacityValue})`;
                ctx.lineWidth = 0.5;
                ctx.beginPath();
                ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                ctx.stroke();
            }
        }
    }
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);

    // Only draw and clear if canvas is visible (Light Mode)
    if (getComputedStyle(canvas).display !== 'none') {
        ctx.clearRect(0, 0, innerWidth, innerHeight);

        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
        }
        connect();
    }
}

// Ensure the canvas sits statically in the background, only rendering in Light mode
function setupCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
    animate();
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Set initial size
    setupCanvas();

    // Since the theme toggle changes [data-theme], we must ensure the canvas is responsive.
    // The CSS display: none handles hiding it in Dark Mode perfectly. 
});
