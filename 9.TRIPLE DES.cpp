#include <stdio.h>
#include <string.h>

void des_rounds(char text[], int key)
{
    for(int r=0; r<16; r++)
    {
        for(int i=0; i<strlen(text); i++)
        {
            text[i] = text[i] ^ (key + r);
        }
    }
}

void triple_des_encrypt(char text[], int k1, int k2, int k3)
{
    des_rounds(text, k1);
    des_rounds(text, k2);
    des_rounds(text, k3);
}

void triple_des_decrypt(char text[], int k1, int k2, int k3)
{
    des_rounds(text, k3);
    des_rounds(text, k2);
    des_rounds(text, k1);
}

int main()
{
    int choice;
    int k1, k2, k3;
    char text[100];

    printf("\nTRIPLE DES PROGRAM\n");
    printf("1. Encrypt\n");
    printf("2. Decrypt\n");

    printf("Enter your choice: ");
    scanf("%d",&choice);

    printf("Enter the text: ");
    scanf("%s",text);

    printf("Enter key1: ");
    scanf("%d",&k1);

    printf("Enter key2: ");
    scanf("%d",&k2);

    printf("Enter key3: ");
    scanf("%d",&k3);

    if(choice==1)
    {
        triple_des_encrypt(text,k1,k2,k3);
        printf("Encrypted Text: %s\n",text);
    }
    else if(choice==2)
    {
        triple_des_decrypt(text,k1,k2,k3);
        printf("Decrypted Text: %s\n",text);
    }
    else
    {
        printf("Invalid choice\n");
    }

    return 0;
}
