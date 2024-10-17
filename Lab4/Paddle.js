class Paddle {
    // Constructor for paddle class with x, y, width, height parameters
    constructor(x, y, radius) {
        this.radius = radius;
        this.x = x;
        this.y = y;
        this.collisionTime; // To store the time of collision
    }

    // Draw paddle
    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI); // Draw the paddle ball
        ctx.stroke();
    }

    // Move the paddle
    move(direction, ctx) {
        const step = 10; // Step size for paddle movement
        if (direction === 'up' && this.y > 0) {
            this.y -= step;
        } else if (direction === 'down' && this.y < ctx.canvas.height - this.radius) {
            this.y += step;
        }
        this.draw(ctx);
    }

    // Move the paddle with mouse
    moveTo(y, ctx) {
        if (y < this.radius) {
            this.y = this.radius;
        } else if (y > ctx.canvas.height - this.radius) {
            this.y = ctx.canvas.height - this.radius;
        } else {
            this.y = y;
        }
        this.draw(ctx);
    }

    // Detect collision with the match ball
    collisionDetector(matchBall, ctx) {
        const distance = Math.sqrt(Math.pow(matchBall.x - this.x, 2) + Math.pow(matchBall.y - this.y, 2));
        const currentTime = performance.now();

        if (distance < matchBall.radius + this.radius) {
            this.collisionTime = currentTime; // Store the time of collision

            // Reverse the speed of the match ball
            matchBall.xspeed *= -1;
            matchBall.yspeed *= -1;

            // Adjust the position of the match ball to prevent it from getting stuck
            const overlap = matchBall.radius + this.radius - distance;
            const angle = Math.atan2(matchBall.y - this.y, matchBall.x - this.x);
            matchBall.x += Math.cos(angle) * overlap;
            matchBall.y += Math.sin(angle) * overlap;
        }

        // Display the message if collision was detected within the last 0.75 seconds
        if (this.collisionTime && currentTime - this.collisionTime < 750) {
            ctx.font = "50px Arial";
            ctx.fillStyle = "red";
            ctx.fillText("Collision", 10, 80);
        }
    }
}