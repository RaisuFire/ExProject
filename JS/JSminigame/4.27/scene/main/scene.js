const config = {
    player_speed: 10,
    cloud_speed: 1,
    enemy_speed: 5,
    bullet_speed: 5,
    fire_cooldown:5,
}

class Player extends GuaImage {
    constructor(game) {
        super(game, 'player')
        this.setup()
    } 
    setup() {
        this.speed = 10
        this.cooldown = 0   
        this.mutldirection = 3     
    }

    update() {
        this.speed = config.player_speed
        // log('player_speed', config.player_speed)
        if (this.cooldown > 0) {
            this.cooldown--
        }
    }
    moveLeft() {
        this.x -= this.speed 
    }
    moveRight() {
        this.x += this.speed
    }
    moveup() {
        this.y -= this.speed
    }
    movedown() {
        this.y += this.speed
    }
    fire () {
        if (this.cooldown == 0) {
            this.cooldown = config.fire_cooldown
            var x = this.x + this.w / 2
            var y = this.y
            for (var i = 0; i < this.mutldirection; i++) {
                var b = Bullet.new(this.game)
                b.direction = i % this.mutldirection
                b.x = x 
                b.y = y
                this.scene.addElement(b)
            }
        }    
    }
    
}

class Bullet extends GuaImage {
    constructor(game) {
        super(game, 'bullet')        
        this.direction = randomBetween(0,1)      
        this.setup()
        
    } 
    setup() {
        // this.speedy = 10
        this.speedy = config.bullet_speed        
        this.speedx = 2
    }

    static new(game, name) {
        var i = new this(game, name)
        return i
    }

    update() {
        this.y -= this.speedy    
        // log("direction", this.direction)    
        if (this.direction == 0) {
            this.x += this.speedx
        } else if (this.direction == 1) {
            
        } else {
            this.x -= this.speedx
        }
    }
}


const randomBetween = function(start, end) {
    var n = Math.random() * (end - start  + 1)
    return Math.floor(n + start)
}

class Enemy extends GuaImage {
    constructor(game) {
        var type = randomBetween(0, 2)
        var name = 'enemy' + type
        super(game, name)
        this.setup()
    } 
    setup() {
        this.speed = randomBetween(2, 5)    
        this.x = randomBetween(0, 350)
        this.y = -randomBetween(0, 200)
    }

    update() {
        this.y += this.speed
        if (this.y > 600) {
            this.setup()
        }
    }
}

class Cloud extends GuaImage {
    constructor(game) {
        var type = randomBetween(0, 2)
        var name = 'cloud' + type
        super(game, name)
        this.setup()
    } 
    setup() {
        this.speed = randomBetween(1, 3)    
        this.x = randomBetween(0, 350)
        this.y = -randomBetween(0, 200)
    }

    update() {
        this.speed = config.cloud_speed
        this.y += this.speed
        if (this.y > 600) {
            this.setup()
        }
    }
}


class Scene extends GuaScene {
    constructor(game) {
        super(game)
        this.setup()
        this.setupInputs()        
    }

    setup() {
        var game = this.game
        this.numberOfElements = 10
        this.numberOfClouds = 3
        this.bg = GuaImage.new(game, 'skybg')
        this.player = Player.new(game)
        this.player.x = 100
        this.player.y = 400

        this.addElement(this.bg)
        this.addElement(this.player)
        
        this.addEnemies()
        this.addClouds()

        //add particles
        var ps = GuaParticleSystem.new(this.game)
        this.addElement(ps)
    }
    addEnemies() {
        var es = []
        for(var i = 0; i <= this.numberOfElements; i++) {
            var e = Enemy.new(this.game )
            es.push(e)
            this.addElement(e)
        }
        this.enemies = es
    }

    addClouds() {
        var cs = []
        for(var i = 0; i <= this.numberOfClouds; i++) {
            var c = Cloud.new(this.game )
            cs.push(c)
            this.addElement(c)
        }
        this.clouds = cs
    }

    static new(game) {
        var i = new this(game)
        return i
    }

    // draw() {
    //     this.game.drawImage(this.bg)
    //     this.game.drawImage(this.player)
    // }
    
    update() {
        super.update()
    }

    setupInputs() {
        var g = this.game
        var s = this
        g.registerAction('a', function(){
            s.player.moveLeft()
        })
        g.registerAction('d', function(){
            s.player.moveRight()
        })
        g.registerAction('w', function(){
            s.player.moveup()
        })
        g.registerAction('s', function(){
            s.player.movedown()
        })
        g.registerAction('j', function(){
            s.player.fire()
        })
    }

 
}


// var Scene = function(game) {
//     var s = {
//         game: game,
//     }
//     // 初始化
//     var paddle = Paddle(game)
//     var ball = Ball(game)

//     var score = 0

//     // var blocks = loadLevel(game, 1)

//     game.registerAction('a', function(){
//         paddle.moveLeft()
//     })
//     game.registerAction('d', function(){
//         paddle.moveRight()
//     })
//     game.registerAction('f', function(){
//         ball.fire()
//     })

//     s.draw = function() {
//         // draw 背景
//         game.context.fillStyle = "#554"
//         game.context.fillRect(0, 0, 400, 300)
//         // draw
//         game.drawImage(paddle)
//         game.drawImage(ball)

//         // draw labels
//         game.context.fillText('分数: ' + score, 10, 290)
//     }
//     s.update = function() {
//         if (window.paused) {
//             return
//         }

//         ball.move()
//         // 判断游戏结束
//         if (ball.y > paddle.y) {
//             // 跳转到 游戏结束 的场景
//             var end = SceneEnd.new(game)
//             game.replaceScene(end)
//         }
//         // 判断相撞
//         if (paddle.collide(ball)) {
//             // 这里应该调用一个 ball.反弹() 来实现
//             ball.反弹()
//         }

//     }

//     // mouse event
//     var enableDrag = false
//     game.canvas.addEventListener('mousedown', function(event) {
//         var x = event.offsetX
//         var y = event.offsetY
//         log(x, y, event)
//         // 检查是否点中了 ball
//         if (ball.hasPoint(x, y)) {
//             // 设置拖拽状态
//             enableDrag = true
//         }
//     })
//     game.canvas.addEventListener('mousemove', function(event) {
//         var x = event.offsetX
//         var y = event.offsetY
//         // log(x, y, 'move')
//         if (enableDrag) {
//             log(x, y, 'drag')
//             ball.x = x
//             ball.y = y
//         }
//     })
//     game.canvas.addEventListener('mouseup', function(event) {
//         var x = event.offsetX
//         var y = event.offsetY
//         log(x, y, 'up')
//         enableDrag = false
//     })

//     return s
// }
