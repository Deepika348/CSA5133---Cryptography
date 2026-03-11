#include <stdio.h>
#include <string.h>

void des_rounds(char text[], int key)
{
    int len = strlen(text);

    for(int r = 0; r < 16; r++)   // 16 DES rounds
    {
        for(int i = 0; i < len; i++)
        {
            text[i] = text[i] ^ (key + r);
        }
    }
}

int main()
{
    int choice;
    int key;
    char text[100];

    printf("DES PROGRAM\n");
    printf("1. Encrypt\n");
    printf("2. Decrypt\n");

    printf("Enter your choice: ");
    scanf("%d",&choice);

    printf("Enter the text: ");
    scanf("%s",text);

    printf("Enter key: ");
    scanf("%d",&key);

    if(choice == 1)
    {
        des_rounds(text,key);
        printf("Encrypted Text: %s\n",text);
    }
    else if(choice == 2)
    {
        des_rounds(text,key);
        printf("Decrypted Text: %s\n",text);
    }
    else
    {
        printf("Invalid choice\n");
    }

    return 0;
}

