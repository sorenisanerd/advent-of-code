package utils

import (
	"errors"
	"fmt"
	"reflect"
	"strconv"
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/stretchr/testify/assert"
)

var hundredInts []int

func init() {
	hundredInts = make([]int, 100)
	for i := 0; i < 100; i++ {
		hundredInts[i] = i
	}
}

func f1(x int) (int, error) {
	if x == 5 {
		return 0, errors.New("We failed")
	}
	return x, nil
}

func TestMust(t *testing.T) {
	type args struct {
		arg1 int
	}
	tests := []struct {
		name    string
		args    args
		want    int
		wantErr bool
	}{
		{"No error", args{42}, 42, false},
		{"Error", args{5}, 42, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				if r := recover(); r == nil && tt.wantErr {
					t.Errorf("Must() did not panic")
				}
			}()
			if got := Must(f1, tt.args.arg1); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Must() = %v, want %v", got, tt.want)
			}
		})
	}

}

func TestGetPrefixes(t *testing.T) {
	tests := []struct {
		name string
		args []string
		want [][]string
	}{
		{"Empty", []string{}, [][]string{{}}},
		{"One element", []string{"foo"}, [][]string{{}, {"foo"}}},
		{"Two elements", []string{"foo", "bar"}, [][]string{{}, {"foo"}, {"foo", "bar"}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetPrefixes(tt.args); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetPrefixes(%v) = %v, want %v", tt.args, got, tt.want)
			}
		})
	}
}

var chooseOneTests = []struct {
	name  string
	input []int
	want  []ChooseOneTuple[int]
}{
	{"Empty", []int{}, []ChooseOneTuple[int]{}},
	{"One element", []int{1}, []ChooseOneTuple[int]{{1, []int{}}}},
	{"Two elements", []int{1, 2}, []ChooseOneTuple[int]{
		{1, []int{2}},
		{2, []int{1}},
	}},
	{"Three elements", []int{1, 2, 3}, []ChooseOneTuple[int]{
		{1, []int{2, 3}},
		{2, []int{1, 3}},
		{3, []int{1, 2}},
	}},
}

func TestChooseOneGenerator(t *testing.T) {
	for _, tt := range chooseOneTests {
		t.Run(tt.name, func(t *testing.T) {
			l := []ChooseOneTuple[int]{}
			for t := range ChooseOneGenerator(tt.input) {
				cp := make([]int, len(t.Rest))
				copy(cp, t.Rest) // This is going to come back to bite me (2023-01-14)
				l = append(l, ChooseOneTuple[int]{t.Val, cp})
			}

			if diff := cmp.Diff(tt.want, l); diff != "" {
				t.Errorf("ChooseOne() mismatch (-want +got):\n%s", diff)
			}
		})
	}
}

func TestChooseOne(t *testing.T) {
	for _, tt := range chooseOneTests {
		t.Run(tt.name, func(t *testing.T) {
			l := []ChooseOneTuple[int]{}
			l = append(l, ChooseOne(tt.input)...)
			if got := l; !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ChooseOne() = %v, want %v", got, tt.want)
			}
		})
	}
}

var x int
var y []int

func BenchmarkChooseOne(b *testing.B) {
	for i := 0; i < b.N; i++ {
		for _, t := range ChooseOne(hundredInts) {
			x = t.Val
			y = t.Rest
		}
	}
}

func BenchmarkChooseOneGenerator(b *testing.B) {
	for i := 0; i < b.N; i++ {
		for t := range ChooseOneGenerator(hundredInts) {
			x = t.Val
			y = t.Rest
		}
	}
}

func BenchmarkChooseOneCallback(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ChooseOneCallBack(hundredInts, func(car int, cdr []int) {
			x = car
			y = cdr
		})
	}
}

func TestChooseOneCallback(t *testing.T) {
	for _, tt := range chooseOneTests {
		t.Run(tt.name, func(t *testing.T) {
			l := []ChooseOneTuple[int]{}
			//l = append(l,
			ChooseOneCallBack(tt.input, func(car int, cdr []int) {
				// ALERT!
				// Part of the reason why we use a callback is to avoid
				// allocating all the slices and copying them around, etc.
				// A side effect is that the cdr slice is reused for each
				// call, so we need to copy it.
				cdrCopy := make([]int, len(cdr))
				copy(cdrCopy, cdr)
				l = append(l, ChooseOneTuple[int]{car, cdrCopy})
			})
			if got := l; !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ChooseOne() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestExtractInts(t *testing.T) {
	tests := []struct {
		name string
		want []int
	}{
		{"", []int{}},
		{"2", []int{2}},
		{"-2", []int{-2}},
		{"1-2", []int{1, -2}},
		{"1--2", []int{1, -2}},
		{"aaaaa", []int{}},
		{"aa12aaa", []int{12}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ExtractInts(tt.name); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ExtractInts() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSplitLines(t *testing.T) {
	tests := []struct {
		name string
		want []string
	}{
		{"", []string{""}},
		{"\n", []string{"", ""}},
		{"a\nb", []string{"a", "b"}},
		{"a\nb\n", []string{"a", "b", ""}},
		{"a\nb\n\n", []string{"a", "b", "", ""}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SplitLines(tt.name); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("SplitLines() = %q, want %q", got, tt.want)
			}
		})
	}
}

func TestChunkByTotalCount(t *testing.T) {
	type args struct {
		s     []int
		count int
	}
	tests := []struct {
		name      string
		args      args
		want      [][]int
		wantPanic bool
	}{
		{"0/1", args{[]int{}, 1}, [][]int{{}}, false},
		{"0/2", args{[]int{}, 2}, [][]int{{}, {}}, false},
		{"1/2", args{[]int{1}, 2}, [][]int{{1}, {}}, true},
		{"2/2", args{[]int{1, 2}, 2}, [][]int{{1}, {2}}, false},
		{"12/5", args{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 5}, [][]int{}, true},
		{"15/5", args{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 3}, [][]int{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}}, false},
		{"15/5", args{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 5}, [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}, {13, 14, 15}}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := ChunkByTotalCount(tt.args.s, tt.args.count); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ChunkByTotalCount() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestChunkBySliceSize(t *testing.T) {
	type args struct {
		s     []int
		count int
	}
	tests := []struct {
		name      string
		args      args
		want      [][]int
		wantPanic bool
	}{
		{"0/0", args{[]int{}, 0}, [][]int{}, true},
		{"0/-1", args{[]int{}, -1}, [][]int{}, true},
		{"0/1", args{[]int{}, 1}, [][]int{}, false},
		{"0/2", args{[]int{}, 2}, [][]int{}, false},
		{"1/2", args{[]int{1}, 2}, [][]int{{1}}, false},
		{"2/2", args{[]int{1, 2}, 2}, [][]int{{1, 2}}, false},
		{"12/5", args{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}, 5}, [][]int{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12}}, false},
		{"15/5", args{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}, 5}, [][]int{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := ChunkBySliceSize(tt.args.s, tt.args.count); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ChunkByTotalCount() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMinInts(t *testing.T) {
	tests := []struct {
		name      string
		ints      []int
		want      int
		wantPanic bool
	}{
		{"No ints", []int{}, 0, true},
		{"1", []int{1}, 1, false},
		{"1,2", []int{1, 2}, 1, false},
		{"3,1,2", []int{3, 1, 2}, 1, false},
		{"-1,-3,-2", []int{-1, -3, -2}, -3, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := MinInts(tt.ints...); got != tt.want {
				t.Errorf("MinInts() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMaxInts(t *testing.T) {
	tests := []struct {
		name      string
		ints      []int
		want      int
		wantPanic bool
	}{
		{"No ints", []int{}, 0, true},
		{"1", []int{1}, 1, false},
		{"1,2", []int{1, 2}, 2, false},
		{"1,3,2", []int{1, 3, 2}, 3, false},
		{"-1,-3,-2", []int{-1, -3, -2}, -1, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := MaxInts(tt.ints...); got != tt.want {
				t.Errorf("MaxInts() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBound(t *testing.T) {
	type args struct {
		i    int
		low  int
		high int
	}
	tests := []struct {
		name      string
		args      args
		want      int
		wantPanic bool
	}{
		{"0/0/0", args{0, 0, 0}, 0, false},
		{"0/1/0", args{0, 1, 0}, 0, true},
		{"0/0/1", args{0, 0, 1}, 0, false},
		{"-1/0/10", args{-1, 0, 10}, 0, false},
		{"11/0/10", args{11, 0, 10}, 10, false},
		{"10/0/10", args{10, 0, 10}, 10, false},
		{"0/0/10", args{0, 0, 10}, 0, false},
		{"1/0/10", args{1, 0, 10}, 1, false},
		{"9/0/10", args{9, 0, 10}, 9, false},
		{"9900009/0/10", args{9900009, 0, 10}, 10, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := Bound(tt.args.i, tt.args.low, tt.args.high); got != tt.want {
				t.Errorf("Bound() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetByIdx(t *testing.T) {
	tests := []struct {
		name      string
		s         []int
		i         int
		want      int
		wantPanic bool
	}{
		{"[1,2,3][0]", []int{1, 2, 3}, 0, 1, false},
		{"[1,2,3][-1]", []int{1, 2, 3}, -1, 3, false},
		{"[1,2,3][-2]", []int{1, 2, 3}, -2, 2, false},
		{"[1,2,3][-3]", []int{1, 2, 3}, -3, 1, false},
		{"[1,2,3][-4]", []int{1, 2, 3}, -4, 1, true},

		{"[1,2,3][1]", []int{1, 2, 3}, 1, 2, false},
		{"[1,2,3][2]", []int{1, 2, 3}, 2, 3, false},
		{"[1,2,3][3]", []int{1, 2, 3}, 3, 2000, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := GetByIdx(tt.s, tt.i); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetByIdx() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMap(t *testing.T) {
	l1 := []int{1, 2, 3, 4, 5}
	l2 := []string{"1", "2", "3", "4", "5"}

	assert.Equal(t, []int{2, 4, 6, 8, 10}, Map(func(i int) int { return i * 2 }, l1))
	assert.Equal(t, l2, Map(func(i int) string { return fmt.Sprint(i) }, l1))
	assert.Equal(t, l1, Map(func(i string) int { return Atoi(i) }, l2))
}

func TestFilter(t *testing.T) {
	l1 := []int{1, 2, 3, 4, 5}
	l2 := []string{"1", "2", "3", "4", "56"}

	assert.Equal(t, []int{1, 3, 5}, Filter(func(i int) bool { return i%2 == 1 }, l1))
	assert.Equal(t, []string{"56"}, Filter(func(s string) bool { return len(s) > 1 }, l2))
}

func TestReduce(t *testing.T) {
	l1 := []int{1, 2, 3, 4, 5}
	l2 := []string{"1", "2", "3", "4", "56"}

	assert.Equal(t, 35, Reduce(func(a, b int) int { return a + b }, l1, 20))
	assert.Equal(t, "foo12345", Reduce(func(a string, b int) string { return a + fmt.Sprint(b) }, l1, "foo"))
	assert.Equal(t, 73, Reduce(func(a int, b string) int { return a + Atoi(b) }, l2, 7))
}

var Itoa = strconv.Itoa

func TestAll(t *testing.T) {
	l1 := []int{1, 2, 3, 4, 5}
	l2 := []int{1, 2, 33, 4, 5}
	l3 := Map(Itoa, l2)

	assert.True(t, All(func(a int) bool { return a < 10 }, l1))
	assert.False(t, All(func(a int) bool { return a < 10 }, l2))
	assert.False(t, All(func(a string) bool { return len(a) < 2 }, l3))
	assert.True(t, All(func(a string) bool { return len(a) < 3 }, l3))
}

func Test_f1(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name      string
		args      args
		want      int
		assertion assert.ErrorAssertionFunc
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := f1(tt.args.x)
			tt.assertion(t, err)
			assert.Equal(t, tt.want, got)
		})
	}
}
