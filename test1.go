package main
import "os/exec"

func main(){
   cmd:=exec.Command("py test200.py")
   out,err:=cmd.Output();err!=nil{
     fmt.Println(err.Error())
   }
}