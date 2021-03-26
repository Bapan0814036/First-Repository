package main
import "fmt"

func generator() func() int{
   var i int
   i=0
   return func()int{
            i++
            return i
          }
}

func main(){
  numgen:=generator()
  for i:=0;i<5;i++{
      fmt.Print(numgen(),"\t")
  }
}


