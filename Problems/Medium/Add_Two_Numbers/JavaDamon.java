package Medium.Add_Two_Numbers;

public class JavaDamon {
    // Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        if (l1 == null || l2 == null) {
            return null;
        }

        int num1, num2, result;
        int carry = 0;
        ListNode newNode = null;
        ListNode head = null;

        while (l1 != null || l2 != null || carry == 1) {

            result = 0;
            num1 = 0;
            num2 = 0;

            if (l1 != null) {
                num1 = l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                num2 = l2.val;
                l2 = l2.next;
            }

            result = num1 + num2 + carry;

            if (result > 9) {
                carry = 1;
            } else {
                carry = 0;
            }

            if (head == null) {
                if (result > 9) {
                    newNode = new ListNode(result - 10);
                    head = newNode;
                } else {
                    newNode = new ListNode(result);
                    head = newNode;
                }
            } else {
                if (carry == 0) {
                    //System.out.println(result);
                    newNode.next = new ListNode(result);
                    newNode = newNode.next;
                } else {
                    newNode.next = new ListNode(result - 10);
                    newNode = newNode.next;
                }
            }
        }

        return head;
    }
}
