class GuaAnimation {
	constructor(game) {
		this.game = game

		//为了省事， 在这里hard code 一套动画
		this.animations = {
			idle: [],
		}
		for (var i = 1; i < 4; i++) {
			var name = `b${i}`
			var t = game.textureByname(name)
			this.animations['idle'].push(t)
		// log('this.animations', this.animations['idle'])            
		}
	
		this.animationsName = 'idle'
		this.texture = this.frames()[0]
		this.w = this.texture.width
		this.h = this.texture.height

		this.frameIndex = 0
		this.frameCount = 3

		// this.animations = {
		// 	idle: [],
		// 	run:[],
		// }
		// for (var i = 1; i < 5; i++) {
		// 	var name = `idle${i}`
		// 	var t = game.textureByname(name)
		// 	this.animations['idle'].push(t)
		// // log('this.animations', this.animations['idle'])            
		// }
		// for (var i = 1; i < 5; i++) {
		// 	var name = `run${i}`
		// 	var t = game.textureByname(name)
		// 	this.animations['run'].push(t)
		// }
		// this.animationsName = 'idle'
		// this.texture = this.frames()[0]
		// this.w = this.texture.width
		// this.h = this.texture.height

		// this.frameIndex = 0
		// this.frameCount = 3

		//
		this.flipx = false
		this.retation = 0

		//重力和加速度
		this.gy = 10
		this.vy = 0 
	}

	static new(game) {
		return new this(game)
	}

	frames() {
		return this.animations[this.animationsName]
	}

	jump() {
		this.vy = -10
		this.retation = -45
	}

	update() {
		//更新受力
		this.y += this.vy
		this.vy += this.gy * 0.2
		var h = 520
		if(this.y > h) {
			this.y = h
			// this.retation = 0
		}

		//更新角度
		if(this.retation < 45) {
			this.retation += 5
		}

		this.frameCount--
		if (this.frameCount == 0) {
			this.frameCount = 3
			this.frameIndex = (this.frameIndex + 1) % this.frames().length
			this.texture = this.frames()[this.frameIndex]
		}
	}

	draw() {
		var context = this.game.context
		context.save()

		var w2 =  this.w / 2
		var h2 =  this.h / 2
		context.translate(this.x + w2, this.y + h2);
		if (this.flipx) {
			context.scale(-1, 1)	
		}
		context.rotate(this.retation * Math.PI / 180)
		context.translate(-w2, -h2);
		
		// Draw the image    
		context.drawImage(this.texture, 0, 0, );

		context.restore();	
	}

	move(x, keyStatus) {
        this.flipx = (x < 0)
        this.x += x
        // var animationsName = {
        //                 down: 'run',
        //                 up: 'idle',
        // }
        // var name = animationsName[keyStatus]
        // this.changeAnimation(name)
	}

	changeAnimation(name) {
        this.animationsName = name
	}
}