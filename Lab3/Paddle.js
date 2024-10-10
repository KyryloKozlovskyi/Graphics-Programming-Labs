class Paddle {
    // Constructor for paddle class with x, y, width, height parameters
    constructor(x, y, width, height) {
        this.width = width;
        this.height = height;
        this.x = x;
        this.y = y;
    }

    // Draw paddle
    draw() {
        ctx.beginPath();
        ctx.rect(this.x, this.y, this.width, this.height); // Draw the paddle
        ctx.stroke();
    }

    // Move the paddle
    move(direction) {
        const step = 10; // Step size for paddle movement
        if (direction === 'up' && this.y > 0) {
            this.y -= step;
        } else if (direction === 'down' && this.y < canvas.height - this.height) {
            this.y += step;
        }
        this.draw();
    }

    // Move the paddle with mouse
    moveTo(y) {
        this.y = y;
        this.draw();
    }
}