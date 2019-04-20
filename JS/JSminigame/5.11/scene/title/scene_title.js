class SceneTitle extends GuaScene {
    constructor(game) {
        super(game)
        var label = GuaLabel.new(game, "hello")
        this.addElement(label)        

        var ps = GuaParticleSystem.new(game)
        this.addElement(ps)
 
    }
    // draw() {
    //     // draw labels
    //     this.game.context.fillText('按 k 开始游戏', 100, 190)
    // }

    // game.registerAction('k', function(){
    //     var s = Scene(game)
    //     game.replaceScene(s)
    // })
}


class GuaLabel {
    constructor(game, text) {
        this.game = game
        this.text = text

    }
    static new(game, text) {
        var i = new this(game, text)
        return i
    }
    draw() {
        this.game.context.fillText(this.text, 100, 190)
    }
    update() {

    }
}


class GuaParticle extends GuaImage {
    constructor(game) {
        super(game, 'fire')
        this.setup()
        this.gravity = 10
    }
    setup() {
        this.life = 20
    }
    init(x, y, vx, vy) {
        this.x = x 
        this.y = y
        this.vx = vx 
        this.vy = vy
    }

    update() {
        this.life--
        this.x += this.vx 
        this.y += this.vy
        // var factor = 0.05
        // this.vx += (factor * this.vx) + Math.sin()
        // this.vy += (factor * this.vy) + Math.cos(l * n)
    }
}

class GuaParticleSystem {
    constructor(game, x, y) {
        this.game = game
        this.x = x
        this.y = y
        this.setup()
    }
 
    static new(game, x, y) {
        var i = new this(game, x, y)
        return i
    }

    setup() {
  
        this.numberOfParticles = 20
        this.particles = []
        for (var i = 0; i < this.numberOfParticles; i++) {
            var p = GuaParticle.new(this.game)       
            //设置初始化坐标
            var s = 5
            // var vx = randomBetween(-s, s)
            // var vy = randomBetween(-s, s)
            var l = this.particles.length
            var n = 6.28 / this.numberOfParticles
            var vx = Math.sin(n * l)
            var vy = Math.cos(n * l)
            p.init(this.x, this.y, vx, vy)     
            this.particles.push(p)
        }
        log("particles;", this.particles.length)
    }

    draw() {
        for (var p of this.particles) {
            p.draw()
        }
    }
    update() {
        // 小火花添加重力
        for (var p of this.particles) {
            var l = this.particles.length
            var n = 6.28 / this.numberOfParticles
            p.vy += p.gravity * Math.cos(n * l) * 0.001
           
        }

        //删除死掉的小火花
        // this.particles = this.particles.filter(p => p.life > 0)
        if (this.particles.length > 0) {
            for (var p of this.particles) {
                // log("p", p.life)
                if (p.life < 0) {
                    this.particles.pop(p)
                }
            }
        }

        //更新所有的小火花
        for (var p of this.particles) {
            p.update()
        }
    }
}


