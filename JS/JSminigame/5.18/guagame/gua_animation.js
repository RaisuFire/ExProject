class GuaAnimation {
    constructor(game) {
        this.game = game
        //为了省事， 在这里hard code 一套动画
        this.animations = {
            idle: [],
            run:[],
        }
        for (var i = 1; i < 5; i++) {
            var name = `idle${i}`
            var t = game.textureByname(name)
            this.animations['idle'].push(t)
        // log('this.animations', this.animations['idle'])            
        }
        for (var i = 1; i < 5; i++) {
            var name = `run${i}`
            var t = game.textureByname(name)
            this.animations['run'].push(t)
        }
        this.animationsName = 'idle'
        this.texture = this.frames()[0]
        this.w = this.texture.width
        this.h = this.texture.height

        this.frameIndex = 0
        this.frameCount = 3

        //
        this.flipx = false
    }

    static new(game) {
        return new this(game)
    }

    frames() {
        return this.animations[this.animationsName]
    }

    update() {
        this.frameCount--
        if (this.frameCount == 0) {
            this.frameCount = 3
            this.frameIndex = (this.frameIndex + 1) % this.frames().length
            this.texture = this.frames()[this.frameIndex]
        }
    }

    draw() {
        var context = this.game.context
        if (this.flipx) {
            context.save()

            var x = this.x + this.w / 2
            context.translate(x, 0);
            context.scale(-1, 1)
            context.translate(-x, 0);
            
            // Draw the image    
            context.drawImage(this.texture, this.x, this.y);
            context.restore();
        } else {
            context.drawImage(this.texture, this.x, this.y);
        }
    }

    move(x, keyStatus) {
        this.flipx = (x < 0)
        this.x += x
        var animationsName = {
            down: 'run',
            up: 'idle',
        }
        var name = animationsName[keyStatus]
        this.changeAnimation(name)
    }

    changeAnimation(name) {
        this.animationsName = name
    }
}