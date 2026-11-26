// 计时包装：给函数包一层，跑完打印耗时。
// 用法: go run stopwatch.go
package main

import (
	"fmt"
	"time"
)

func stopwatch(name string, fn func() int) func() int {
	return func() int {
		start := time.Now()
		result := fn()
		fmt.Printf("%s took %s\n", name, time.Since(start).Round(time.Millisecond))
		return result
	}
}

func main() {
	slowJob := stopwatch("slowJob", func() int {
		time.Sleep(200 * time.Millisecond)
		sum := 0
		for i := 0; i < 100000; i++ {
			sum += i
		}
		return sum
	})
	fmt.Println("result:", slowJob())
}
