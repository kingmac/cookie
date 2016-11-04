var g_g = {};

function main() {
  // Frame rate.
	g_g.frameRate = 60;
	g_g.fps       = g_g.frameRate;
	g_g.thisTick  = new Date().getTime();
	g_g.lastTick  = g_g.thisTick;
	g_g.delta     = 60/g_g.frameRate;

	// The game canvas.
	g_g.canvas = document.getElementById('game');
	g_g.ctx    = g_g.canvas.getContext('2d');
	setScreenSize();

	g_g.camera = new trig.Coord(0, 0);

	g_g.mouse = new trig.Coord(0, 0);
	g_g.mouseButtons = { left:  new Key(),
		                 right: new Key() };
	g_g.keys = [];
	for (var i = 0; i < 222; ++i) {
		g_g.keys.push(new Key());
	}
	g_g.keyBinds = {
		spacebar: 32,
		shift: 16,
		escape: 27,
		key_p: 80
	};



	// Sets up everything.
	setInputCallbacks();
	loadMedia();

	reset();

	// Sets up the game loop.
	if (typeof g_g.gameLoop != "undefined")
	clearInterval(g_g.gameLoop);
	g_g.gameLoop = setInterval(update, 1000/g_g.frameRate);
}


function reset() {
	g_g.center = new trig.Coord(0, 0);
	g_g.averageFps = g_g.frameRate;
	g_g.player = new trig.Coord(g_g.center.x, g_g.center.y)
}


function update() {
	g_g.thisTick = new Date().getTime();
	g_g.fps = 1000 / (g_g.thisTick-g_g.lastTick);
	if (g_g.fps == 0)
		g_g.delta = 0;
	else
		g_g.delta = 60 / g_g.fps;

	var smoothing = 0.9; // larger=more smoothing
	g_g.averageFps = (g_g.averageFps * smoothing) + (g_g.fps * (1.0-smoothing));


	g_g.player.move(g_g.player.dirTo(g_g.mouse), 5);


	// Draw
	g_g.ctx.fillStyle = "#000";
	g_g.ctx.fillRect(0, 0, g_g.canvas.width, g_g.canvas.height);

	g_g.ctx.fillStyle = "#fff";
	g_g.ctx.fillRect(g_g.player.x-50, g_g.player.y-50, 100, 100);


	// End drawing
	// Keys
	g_g.mouseButtons.left.update();
	g_g.mouseButtons.right.update();
	for (var i in g_g.keys) {
	  g_g.keys[i].update();
	}

	//screenFinalize();

	g_g.lastTick = g_g.thisTick;
}


function gameOver() {
	screenChange(2);
	g_g.gameOverTime = new Date().getTime();
	if (g_g.score > g_g.highScore) {
		g_g.highScore = g_g.score;
		document.cookie = "high-score=" + g_g.score.toString();
	}
}


function loadMedia() {

}


function setScreenSize() {
	g_g.canvas.width  = Math.min(1920, window.innerWidth);
	g_g.canvas.height = Math.min(1080, window.innerHeight);
}


function screenX(x) {
  return x - g_g.camera.x;
}

function screenY(y) {
  return y - g_g.camera.y;
}

function realX(x) {
  return x + g_g.camera.x;
}

function realY(y) {
  return y + g_g.camera.y;
}


// Common

RgbColor = function(r, g, b) {
  this.r = r;
  this.g = g;
  this.b = b;
};

RgbColor.prototype.get = function() {
  return "rgb(" + this.r.toString() + "," + this.g.toString() + "," + this.b.toString() + ")";
};


function randomRange(min, max) {
	return Math.floor(randomRangeReal(min, max));
}

function randomRangeReal(min, max) {
  return Math.random() * (max - min) + min;
}


// Events

Key = function() {
	this.pressed  = false;
	this.released = false;
	this.down     = false;
};

Key.prototype.press = function() {
	if (this.down == false) {
		this.pressed = true;
		this.down    = true;
	}
};

Key.prototype.release = function() {
	this.released = true;
	this.down     = false;
};

Key.prototype.update = function() {
	this.pressed  = false;
	this.released = false;
};


function getMouseButtonIsLeft(num) {
	var left = (navigator.appName == "Microsoft Internet Explorer") ? 1 : 0;
	return (num == left);
}


function setInputCallbacks() {
	document.addEventListener("mousemove", function (evt) {
		var rect = g_g.canvas.getBoundingClientRect();
		g_g.mouse.x = evt.clientX - rect.left;
		g_g.mouse.y = evt.clientY - rect.top;
		//var message = 'Mouse position: ' + g_g.mouse.x + ',' + g_g.mouse.y;
		//console.log(message);
	}, false);


	window.onresize = function() {
		setScreenSize();
	};

	document.onmousedown = function(e) {
		if (getMouseButtonIsLeft(e.button)) {
			g_g.mouseButtons.left.press();
		}
		else {
			g_g.mouseButtons.right.press();
		}
	};

	document.onmouseup = function(e) {
		if (getMouseButtonIsLeft(e.button)) {
			g_g.mouseButtons.left.release();
		}
		else {
			g_g.mouseButtons.right.release();
		}
	};

	document.onkeydown = function(e) {
		g_g.keys[e.which].press();
	};

	document.onkeyup = function(e) {
		g_g.keys[e.which].release();
	};

}

// Must be at bottom.
main();