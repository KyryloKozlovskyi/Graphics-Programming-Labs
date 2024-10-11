class Paddle {
    // Constructor for paddle class with x, y, width, height parameters
    constructor(x, y, radius) {
        this.radius = radius;
        this.x = x;
        this.y = y;
    }

    // Draw paddle
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI); // Draw the paddle ball
        ctx.stroke();
    }

    // Move the paddle
    move(direction) {
        const step = 10; // Step size for paddle movement
        if (direction === 'up' && this.y > 0) {
            this.y -= step;
        } else if (direction === 'down' && this.y < canvas.height - this.radius) {
            this.y += step;
        }
        this.draw();
    }

    // Move the paddle with mouse
    moveTo(y) {
        if (y < 0) {
            this.y = 0;
        } else if (y > canvas.height - this.radius) {
            this.y = canvas.height - this.radius;
        } else {
            this.y = y;
        }
        this.draw();
    }
}