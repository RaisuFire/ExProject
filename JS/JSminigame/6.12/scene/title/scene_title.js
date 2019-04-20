class Pipes {
    constructor(game) {
        this.game = game
        this.pipes = []
        this.pipeSpace = 150
        this.pipeDistance = 200
        this.columsOfPipes = 3
        for (var i = 0; i < this.columsOfPipes; i++) {
            var p1 = GuaImage.new(game, 'pipe')
            p1.flipY = true
            p1.x = 500 + i * this.pipeDistance
            var p2 = GuaImage.new(game, 'pipe')
            p2.x = p1.x
            this.resetPipesPosition(p1, p2)
            this.pipes.push(p1)
            this.pipes.push(p2)
        }
    }

    static new(game) {
        return new this(game)
    }

    resetPipesPosition(p1, p2) {
        p1.y = randomBetween(-200, 0)
        p2.y = p1.y + p1.h+ this.pipeDistance
    }

    update() {
        for (var p of this.pipes) {
            p.x -= 5
            if (p.x < -100) {
                p.x += this.pipeDistance * this.columsOfPipes
            }

        }
    }

    draw() {
        var context = this.game.context
        for (var p of this.pipes) {

            context.save()

            var w2 = p.w / 2
            var h2 = p.h / 2
            context.translate(p.x + w2, p.y + h2);
            var scaleX = p.flipX ? -1 : 1
            var scaleY = p.flipY ? -1 : 1
            context.scale(scaleX, scaleY)
            context.rotate(p.retation * Math.PI / 180)
            context.translate(-w2, -h2);

            // Draw the image
            context.drawImage(p.texture, 0, 0, );

            context.restore();
        }
    }
}


class SceneTitle extends GuaScene {
    constructor(game) {
        super(game)
        // var label = GuaLabel.new(game, "hello")
        // this.addElement(label)

        // var ps = GuaParticleSystem.new(game)
        // this.addElement(ps)

        var bg1 = GuaImage.new(game, 'bg1')
        this.addElement(bg1)

        this.pipe = Pipes.new(game)
        this.addElement(this.pipe)

        this.grounds = []
        for (var i = 0; i < 30; i++) {
            var g = GuaImage.new(game, 'ground')
            g.x = i * 19
            g.y = 550
            this.addElement(g)
            this.grounds.push(g)
        }

        this.skipCount = 5

        //player
        var b = GuaAnimation.new(game)
        b.x = 180
        b.y = 200
        this.bird = b
        this.addElement(b)
        this.setupInput()
    }

    update() {
        super.update()
        //地图移动
        this.skipCount--

        var offset = 5
        if (this.skipCount == 0) {
            this.skipCount = 5
            offset = -20
        }
        for (var i = 0; i < 30; i++) {
            var g = this.grounds[i]
            g.x -= offset
        }
    }

    setupInput() {
        var self = this
        var b = this.bird
        self.game.registerAction('a', function(keyStatus) {
            b.move(-2, keyStatus)
        })
        self.game.registerAction('d', function(keyStatus) {
            b.move(2, keyStatus)
        })
        self.game.registerAction('j', function(keyStatus) {
            b.jump()
        })
    }
}
