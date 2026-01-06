/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(resolve =>setTimeout(resolve, millis));
}
sleep(2000).then(()=>{
    console.log("hey")
})
/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */