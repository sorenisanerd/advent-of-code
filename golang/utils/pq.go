package utils

import "container/heap"

type PriorityQueue[T any] priorityQueue[T]

func NewPriorityQueue[T any](getPriority func(T) int) PriorityQueue[T] {
	pq := PriorityQueue[T]{}
	ppq := (*priorityQueue[T])(&pq)
	ppq.getPriority = getPriority
	return pq
}

func (pq *PriorityQueue[T]) Ascending(x bool) {
	ppq := (*priorityQueue[T])(pq)
	ppq.ascending = x
	pq.Fix()
}

func (pq *PriorityQueue[T]) Len() int {
	return len(pq.q)
}

func (pq *PriorityQueue[T]) Push(x T) {
	ppq := (*priorityQueue[T])(pq)
	heap.Push(ppq, x)
}

func (pq *PriorityQueue[T]) Fix() {
	ppq := (*priorityQueue[T])(pq)
	heap.Init(ppq)
}

func (pq *PriorityQueue[T]) Pop() *T {
	ppq := (*priorityQueue[T])(pq)
	v := heap.Pop(ppq)
	return v.(*T)
}

// Note the difference between priorityQueue and PriorityQueue!
// priorityQueue is for the heap implementation, PriorityQueue is for the end user.

type priorityQueue[T any] struct {
	q           []*T
	getPriority func(T) int
	ascending   bool
}

func (pq priorityQueue[T]) Len() int {
	return len(pq.q)
}

func (pq priorityQueue[T]) Less(i, j int) bool {
	return (pq.getPriority(*(pq.q[i])) < pq.getPriority(*(pq.q[j]))) == pq.ascending
}

func (pq *priorityQueue[T]) Swap(i, j int) {
	pq.q[i], pq.q[j] = pq.q[j], pq.q[i]
}

func (pq *priorityQueue[T]) Push(x any) {
	t := x.(T)
	pq.q = append(pq.q, &t)
}

func (pq *priorityQueue[T]) Pop() any {
	item := pq.q[len(pq.q)-1]
	pq.q = pq.q[:len(pq.q)-1]
	return item
}
