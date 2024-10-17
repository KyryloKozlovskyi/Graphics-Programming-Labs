// Ball class
class Ball {
    // Constructor for ball class with x, y, xspeed, yspeed, radius, rotation parameters
    constructor(x, y, xspeed, yspeed, radius, rotation, color) {
        this.x = x;
        this.y = y;
        this.xspeed = xspeed;
        this.yspeed = yspeed;
        this.radius = radius;
        this.rotation = rotation; // Rotation speed of the peace sign
        this.angle = 0; // Start angle at 0
        this.gravity = 0.01; // Gravity constant
        this.energyLoss = 0.9; // Energy loss on each bounce
        this.color = color;

    }

    // Draw peace sign
    draw(ctx) {
        this.angle += this.rotation; // Increment the angle by the rotation speed
        ctx.beginPath(); // Start drawing the peace sign
    
        // Outer circle
        ctx.fillStyle = this.color; // Set the color
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
        ctx.fillStyle = "#000000" // Reset the color

        // Draw a vertical line
        ctx.moveTo(this.x + this.radius * Math.sin(this.angle - Math.PI), this.y + this.radius * Math.cos(this.angle - Math.PI));
        ctx.lineTo(this.x + this.radius * Math.sin(this.angle), this.y + this.radius * Math.cos(this.angle));

        // Draw a left diagonal line
        ctx.moveTo(this.x - this.radius * Math.cos(this.angle + Math.PI / 4), this.y + this.radius * Math.sin(this.angle + Math.PI / 4));
        ctx.lineTo(this.x, this.y);

        // Draw a right diagonal line
        ctx.lineTo(this.x + this.radius * Math.sin(this.angle + Math.PI / 4), this.y + this.radius * Math.cos(this.angle + Math.PI / 4));
        ctx.stroke(); // Draw the lines
    }

    // Move ball
    move(ctx, paddle1, paddle2) {
        // Apply gravity to the vertical speed
        this.yspeed += this.gravity;

        // Update the x, y location
        this.y += this.yspeed;
        this.x += this.xspeed;

        // Up -> Down bounce
        if (this.y >= ctx.canvas.height - this.radius) { // If the ball hits the bottom
            this.yspeed *= -1 * this.energyLoss; // Reverse the yspeed and apply energy loss
            this.y = ctx.canvas.height - this.radius; // Adjust position
        } else if (this.y <= this.radius) { // If the ball hits the top
            this.yspeed *= -1; // Reverse the yspeed
            this.y = this.radius; // Adjust position
        }

        // Left -> Right bounce
        if (this.x >= ctx.canvas.width - this.radius) { // If the ball hits the right
            this.xspeed *= -1; // Reverse the xspeed
            this.x = ctx.canvas.width - this.radius; // Adjust position
            paddle2.score -= 1; // Decrease the score for paddle2
        } else if (this.x <= this.radius) { // If the ball hits the left
            this.xspeed *= -1; // Reverse the xspeed
            this.x = this.radius; // Adjust position
            paddle1.score -= 1; // Decrease the score for paddle1
        }

        // Reset the score to 0 if it goes below 0
        if (paddle1.score < 0) {
            paddle1.score = 0;
        }
        else if (paddle2.score < 0) {
            paddle2.score = 0;
        }
    }

    changeRotation(newSpeed) {
        this.rotation = newSpeed;
    }
}