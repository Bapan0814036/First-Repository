package main
import "os/exec"
import "os"
import "log"

func main(){
   cmd:=exec.Command("C:\Users\babiswas\Desktop\Python3.8\python.exe "+"test200.py")
   cmd.Stdout=os.Stdout
   cmd.Stderr=os.Stderr
   log.Println(cmd.Run())
}