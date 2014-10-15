#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct entry{
    char *str;
    struct entry *next;
};

struct list{
    struct entry *next;
};

struct list head = {NULL};
char string[] = "   the    sky   is         blue   ";

void DeleteList(struct list *head);
void DeleteList(struct list *head)
{
    if (NULL == head)
        return;
    struct entry *ptr = head->next;

    while(NULL != ptr){
        struct entry *next = ptr->next;
        free(ptr);
        ptr = next;
    }

    return;
}

char* ReverseWordsInAString(char *str);
char* ReverseWordsInAString(char *str)
{
    if (NULL == str)
        return NULL;
    int len = strlen(str)+1;
    char newstr[len];
    struct entry *entry = NULL;
    char *saveptr = NULL;
    char *ptr = strtok_r(str, " ", &saveptr);
    while(NULL != ptr){
        if (NULL == (entry = (struct entry *)calloc(1, sizeof(struct entry))))
            return NULL;
        entry->next = head.next;
        head.next = entry;
        entry->str = ptr;
        ptr = strtok_r(NULL, " ", &saveptr);
    }

    memset(newstr, 0x00, len);
    struct entry *p = head.next;
    while(NULL != p){
        strncat(newstr, p->str, strlen(p->str));
        strncat(newstr, " ", strlen(" "));
        p = p->next;
    }

    strncpy(str, newstr, len);
    return NULL;
}

int main(void)
{
    printf("string : %s\n", string);
    ReverseWordsInAString(string);
    printf("Reverse string : %s\n", string);
    DeleteList(&head);
    return 0x00;
}
