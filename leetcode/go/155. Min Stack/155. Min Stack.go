package main

type MinStack struct {
	slice  [][2]int
}

func Constructor() MinStack {
	return MinStack{}
}


func (this *MinStack) Push(val int) {
	minVal := val
	if len(this.slice) > 0 {
		if minVal = this.slice[len(this.slice)-1][1]; val < minVal {
			minVal = val
		}
	}
	this.slice = append(this.slice, [2]int{val, minVal})
}

func (this *MinStack) Pop() {
	this.slice = this.slice[:len(this.slice)-1]
}

func (this *MinStack) Top() int {
	return this.slice[len(this.slice)-1][0]
}


func (this *MinStack) GetMin() int {
	return this.slice[len(this.slice)-1][1]
}
