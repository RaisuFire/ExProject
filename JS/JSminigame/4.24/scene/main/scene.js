class player extends GuaImage {
    constructor(game) {
        setup()
    }

    setup() {
        this.game.registerAction('a', function() {
            // this.player.x -= 5
            log("this.player:", this.player)
        })
        this.game.registerAction('d', function() {
            this.player.moveRight()
        })
    }
}

class Scene extends GuaScene {
    constructor(game) {
        super(game)
        this.setup()
    }

    setup() {
        var game = this.game
        this.bg = GuaImage.new(game, 'skybg')
        this.player = GuaImage.new(game, 'player')
        this.cloud = GuaImage.new(game, 'cloud')
        this.enemy0 = GuaImage.new(game, 'enemy0')
        this.player.x = 100
        this.player.y = 400


        // this.game.registerAction('f', function(){
        //     ball.fire()
        // })

        this.elements = []
        this.elements.push(this.bg)
        this.elements.push(this.player)
        this.elements.push(this.cloud)
        this.elements.push(this.enemy0)

        // this.game.registerAction('a', function(){
        //     // this.player.x -= 5
        //     log("this.player:", this.player)
        // })
        // this.game.registerAction('d', function(){
        //     this.player.moveRight()
        // })
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
        this.cloud.y += 1
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
