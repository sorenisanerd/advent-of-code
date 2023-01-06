package utils

import (
	"errors"
	"reflect"
	"testing"
)

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
