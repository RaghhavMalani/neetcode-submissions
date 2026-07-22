/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private int gcd(int a, int b){
        while (b > 0){
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }

    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode curr = head;
        while (curr.next != null){
            int v1 = curr.val;
            int v2 = curr.next.val;
            curr.next = new ListNode(gcd(v1,v2),curr.next);
            curr = curr.next.next;
        }
        return head;
    }
}