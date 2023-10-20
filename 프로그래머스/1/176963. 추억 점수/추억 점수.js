function solution(name, yearning, photo) {
    const answer = [];
    let yearning_dic = {}
    for (let i = 0; i<name.length; i++){
        yearning_dic[name[i]] = yearning[i]
    }
    for (row of photo){
        let total = 0;
        for (person of row){
            if(yearning_dic[person]){
                total += yearning_dic[person]
            }
        }
        answer.push(total)
    }
    
    return answer;
}