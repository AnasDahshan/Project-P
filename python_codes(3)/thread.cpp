#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>

int counter = 0;
pthread_mutex_t counterlock;

void* increment() {
    int i;
    for (i = 0 ; i < 10 ; i++) {
        pthread_mutex_lock(&counterlock);
        pthread_t id = pthread_self();
        counter++;
        printf("THREAD ID : %ld COUNTER = %d\n", id, counter);
        pthread_mutex_unlock(&counterlock);
    }
    return NULL;
}

int main (void) {
    pthread_t thread[2];
    for (int i = 0 ; i < 2 ; i++) {
        pthread_create(&thread[i], NULL, &increment, NULL);
    }
    for (int i = 0 ; i < 2 ; i++) {
        pthread_join(thread[i], NULL);
    }
    printf("Counter = %d", counter);
    return 0;
}