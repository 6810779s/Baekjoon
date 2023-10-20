function solution(park, routes) {
    let answer = [];
    const n = park.length;
    const m = park[0].length;
    let x = 0;
    let y = 0;
    const dx = [1, -1, 0, 0]; //S, N, E, W
    const dy = [0, 0, 1, -1];
    const map_d = {'S':0,'N':1, 'E':2, 'W':3}
    
    park.forEach((row, idx)=>{
        for (let i=0; i<row.length; i++){
            if (row[i] == 'S'){
                x = idx;
                y = i;
            }
        }
    })
    
    
    routes.forEach((order)=>{
        const [d, num] = order.split(" ");
        const move_d = map_d[d];
        let flag = false
        let nx = x
        let ny = y
        for (let i=0; i<num;i++){
            nx += dx[move_d];
            ny += dy[move_d];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m){
                flag = true
                break
            } 
            if (park[nx][ny] == 'X'){
                flag = true
                break
            }
        }
         if (!flag){
            x = nx
            y = ny
        }
    })
    
    return [x,y];
}