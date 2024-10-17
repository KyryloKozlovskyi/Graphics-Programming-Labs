class Paddle {
    // Constructor for paddle class with x, y, width, height parameters
    constructor(x, y, radius) {
        this.radius = radius;
        this.x = x;
        this.y = y;
        this.collisionTime = null; // To store the time of collision
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
        if (y < this.radius) {
            this.y = this.radius;
        } else if (y > canvas.height - this.radius) {
            this.y = canvas.height - this.radius;
        } else {
            this.y = y;
        }
        this.draw();
    }

    collisionDetector(xBall, yBall, rBall, ctx) {
        //console.log(frameCounter);
        // Message up one the screen for 18 frames
        // Frame counter set to 0 on the collision
        // If frame counter < 18  display the message
        //console.log("TST")
        //console.log(xBall, yBall, rBall)
        //console.log(this.x, this.y, this.radius + " PADDLE")
        var distance = Math.sqrt(Math.pow(xBall - this.x, 2) + Math.pow(yBall - this.y, 2));
        const currentTime = performance.now();
        //console.log(distance)
        if (distance < rBall + this.radius) {
            //ctx.font = "50px Arial";
            //ctx.fillText("Collision", 10, 80);
            this.collisionTime = currentTime; // Store the time of collision
            console.log("Collision detected at time: " + currentTime); // Log the time of collision
        }
        
        // Display the message if collision was detected within the last 0.75 seconds
        if (this.collisionTime && currentTime - this.collisionTime < 750) {
            ctx.font = "50px Arial";
            ctx.fillStyle = "red";
            ctx.fillText("Collision", 10, 80);
        }
    }
}