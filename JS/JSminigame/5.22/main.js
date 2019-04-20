// var loadLevel = function(game, n) {
//     n = n - 1
//     var level = levels[n]
//     var blocks = []
//     for (var i = 0; i < level.length; i++) {
//         var p = level[i]
//         var b = Block(game, p)
//         blocks.push(b)
//     }
//     return blocks
// }

var enableDebugMode = function(game, enable) {
    if(!enable) {
        return
    }
    window.paused = false
    window.addEventListener('keydown', function(event){
        var k = event.key
        if (k == 'p') {
            // 暂停功能
            window.paused = !window.paused
        } else if ('1234567'.includes(k)) {
            // 为了 debug 临时加的载入关卡功能
            // blocks = loadLevel(game, Number(k))
        }
    })
    // 控制速度
    document.querySelector('#id-input-speed').addEventListener('input', function(event) {
        var input = event.target
        // log(event, input.value)
        window.fps = Number(input.value)
    })
}

var __main = function() {
    var images = {
        bullet: 'img/bullet.png',
        player: 'img/player.png',
        skybg: 'img/skybg.png',
        enemy0: 'img/enemy0.png',
        enemy1: 'img/enemy1.png',
        enemy2: 'img/enemy2.png',
        cloud0: 'img/cloud0.png',
        cloud1: 'img/cloud1.png',
        cloud2: 'img/cloud2.png',
        cloud3: 'img/cloud3.png',
        fire: 'img/fire.png',

        //多状态动画
        //空闲
        idle1:'img/idle/i1.png',
        idle2:'img/idle/i2.png',
        idle3:'img/idle/i3.png',
        idle4:'img/idle/i4.png',
        //走路
        run1:'img/walking/w1.png',
        run2:'img/walking/w2.png',
        run3:'img/walking/w3.png',
        run4:'img/walking/w4.png',

        //flappy bird 
        bg:'img/bird/bg.png',
        bg1:'img/bird/bg1.png',
        bird:'img/bird/bird.png',
        b1:'img/bird/b1.png',
        b2:'img/bird/b2.png',
        b3:'img/bird/b3.png',
        ground:'img/bird/ground.png',
        tube1:'img/bird/tube1.png',
        tube2:'img/bird/tube2.png',
    }
    var game = GuaGame.instance(30, images, function(g){
        // var s = Scene.new(g)
        var s = SceneTitle.new(g)
        g.runWithScene(s)
    })

    enableDebugMode(game, true)
}

__main()

