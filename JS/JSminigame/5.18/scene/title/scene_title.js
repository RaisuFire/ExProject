class SceneTitle extends GuaScene {
    constructor(game) {
        super(game)
        // var label = GuaLabel.new(game, "hello")
        // this.addElement(label)        

        // var ps = GuaParticleSystem.new(game)
        // this.addElement(ps)

        var w = GuaAnimation.new(game)
        w.x = 100
        w.y = 200
        this.w = w 
        this.addElement(w)
        this.setupInput()
    }
    setupInput() {
        var self = this
        self.game.registerAction('a', function(keyStatus) {
            self.w.move(-2, keyStatus)
        })
        self.game.registerAction('d', function(keyStatus) {
            self.w.move(2, keyStatus)
        })
    }
}


