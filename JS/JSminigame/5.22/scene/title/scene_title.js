class SceneTitle extends GuaScene {
    constructor(game) {
        super(game)
        // var label = GuaLabel.new(game, "hello")
        // this.addElement(label)        

        // var ps = GuaParticleSystem.new(game)
        // this.addElement(ps)

        var bg1 = GuaImage.new(game,'bg1')
        this.addElement(bg1)

        this.grounds = []
        for (var i = 0; i < 30; i++) {
            var g = GuaImage.new(game, 'ground')
            g.x = i*19
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


