// Ball class
class Ball {
    // Constructor for ball class with x, y, xspeed, yspeed, radius parameters
    constructor(x, y, xspeed, yspeed, radius) {
        this.x = x;
        this.y = y;
        this.xspeed = xspeed;
        this.yspeed = yspeed;
        this.radius = radius;
    }

    // Draw peace sign
    draw(ctx) {
        ctx.beginPath(); // Start drawing the peace sign

        // Outer circle
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
        ctx.stroke();

        // Vertical line
        ctx.moveTo(this.x, this.y - this.radius); // Start from the top of the circle
        ctx.lineTo(this.x, this.y + this.radius); // Draw a line to the bottom of the circle
        ctx.stroke(); // Draw the line

        // Left diagonal line
        ctx.moveTo(this.x, this.y); // Start from the center of the circle
        ctx.lineTo(this.x - this.radius * Math.cos(7 * Math.PI / 4), this.y + this.radius * Math.sin(Math.PI / 4)); // Draw a line to the bottom left of the circle
        ctx.stroke(); // Draw the line

        // Right diagonal line
        ctx.moveTo(this.x, this.y); // Start from the center of the circle
        ctx.lineTo(this.x + this.radius * Math.cos(7 * Math.PI / 4), this.y + this.radius * Math.sin(Math.PI / 4)); // Draw a line to the bottom right of the circle
        ctx.stroke(); // Draw the line
    }

    // Move ball
    move(ctx) {
        // Update the x, y location
        this.y += this.yspeed;
        this.x += this.xspeed;

        // Up -> Down bounce
        if (this.y >= ctx.canvas.height - this.radius) { // If the ball hits the bottom
            this.yspeed *= -1; // Reverse the yspeed
            this.y = ctx.canvas.height - this.radius; // Adjust position
        } else if (this.y <= this.radius) { // If the ball hits the top
            this.yspeed *= -1; // Reverse the yspeed
            this.y = this.radius; // Adjust position
        }

        // Left -> Right bounce
        if (this.x >= ctx.canvas.width - this.radius) { // If the ball hits the right
            this.xspeed *= -1; // Reverse the xspeed
            this.x = ctx.canvas.width - this.radius; // Adjust position
        } else if (this.x <= this.radius) { // If the ball hits the left
            this.xspeed *= -1; // Reverse the xspeed
            this.x = this.radius; // Adjust position
        }
    }
}