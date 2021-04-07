var orchestraLayout = function(num, xPos, yPos) {
    let l = 0
    let r = num-1
    let t = 0
    let b = num-1
    let count=1
    let all=1
    let target = num*num
    let mat = new Array(num).fill(0).map(_ => new Array(num).fill(0))
    while (all <= target){
        for(let i=l;i<r+1;i++){
            mat[t][i] = count
            if (count === 9) {
                count = 1
            } else {
                count ++
            }
            all++
        }
        t++
        for(let i=t;i<b+1;i++){
            mat[i][r] = count
            if (count === 9) {
                count = 1
            } else {
                count ++
            }
            all++
        }
        r--
        for(let i=r;i>l-1;i--){
            mat[b][i] = count
            if (count === 9) {
                count = 1
            } else {
                count ++
            }
            all++
        }
        b--
        for(let i=b;i>t-1;i--){
            mat[i][l] = count
            if (count === 9) {
                count = 1
            } else {
                count ++
            }
            all++
        }
        l++
    }
    console.log(mat)
    return mat[xPos][yPos]
};

console.log(orchestraLayout(3,0,2))