//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() {
    val num = readLine()!!.toInt()
    var dp = mutableListOf(0,1,1)
    for (i in 3..num){
        dp.add(dp[i-1]+dp[i-2])

    }
    println(dp[num])
}