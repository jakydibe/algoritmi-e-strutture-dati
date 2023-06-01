

array = [2,8,5,3,9,4,1,7]


###############################################################################################
###############################################################################################

#                   TERMINI


#ALGORITMI STABILI: algoritmi che mantengono l' ordine relativo deglie elementi ( in pratica, se due 
# elementi sono uguali l' algoritmo garantisce che l' ordine originale tra questi due elementi sara' mantenuto anche dopo il sort)

#ALGORITMO IN-PLACE:un algoritmo che richiede una quantita' di memoria ausiliaria che non cambia con la dimensione del problema. (Ovvero una qta' costante di memoria extra)
#IN PRATICA MODIFICA I DATI SULLA POSIZIONE ORIGINALE SENZA L' USO DI STRUTTURE AUSILIARIE





###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################

#  _____ _   _  _____ ______ _____ _______ _____ ____  _   _        _____  ____  _____ _______ 
# |_   _| \ | |/ ____|  ____|  __ \__   __|_   _/ __ \| \ | |      / ____|/ __ \|  __ \__   __|
#   | | |  \| | (___ | |__  | |__) | | |    | || |  | |  \| |     | (___ | |  | | |__) | | |   
#   | | | . ` |\___ \|  __| |  _  /  | |    | || |  | | . ` |      \___ \| |  | |  _  /  | |   
#  _| |_| |\  |____) | |____| | \ \  | |   _| || |__| | |\  |      ____) | |__| | | \ \  | |   
# |_____|_| \_|_____/|______|_|  \_\ |_|  |_____\____/|_| \_|     |_____/ \____/|_|  \_\ |_|   
#                                                                                              
#                                                                                             
#INSERTION SORT                                                                                                                         #
#TEORIA:                                                                                                                                #
#   1)esaminare ogni oggetto e compararlo con l' oggetto alla sua sinistra                                                              #
#   2)inserire l' oggetto nella posizione corretta dentro l' array                                                                      #        
                                                                                                                                        #
#complessita' O(n^2)     

#Casi utili:     -dati che continuano ad aggiornarsi in tempo reale
#                -insieme di dati molti piccoli
                                                                                                               #
def insertion_sort(A):                                                                                                                  #
    for i in range(len(A)):                                                                                                             #    
        j = i                                                                                                                           #
        while j > 0 and A[j-1] > A[j]: #itero finche' il mio elemento sta nel posto giusto                                              #
            tmp = A[j-1] #swappo gli elementi                                                                                           #    
            A[j-1] = A[j]                                                                                                               #
            A[j] = tmp                                                                                                                  #
            j = j-1 #continuo a iterare                                                                                                 #
                                                                                                                                        #
    return A                                                                                                                            #
                                                                                                                                        #
                                                                                                                                        #
                                                                                                                                        #
                                                                                                                                        #
print(f"insertion_sort: {insertion_sort(array)}")     



                                                                                                       
###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################

#  __  __ ______ _____   _____ ______    _____  ____  _____ _______ 
# |  \/  |  ____|  __ \ / ____|  ____|  / ____|/ __ \|  __ \__   __|
# | \  / | |__  | |__) | |  __| |__    | (___ | |  | | |__) | | |   
# | |\/| |  __| |  _  /| | |_ |  __|    \___ \| |  | |  _  /  | |   
# | |  | | |____| | \ \| |__| | |____   ____) | |__| | | \ \  | |   
# |_|  |_|______|_|  \_\\_____|______| |_____/ \____/|_|  \_\ |_|   
#                                                                   
#                                                                 

#MERGE SORT, DIVIDE ET IMPERA
#TEORIA:
#   1)dividere array in 1 sotto array finche' ogni sottoarray ha un solo elemento
#   2)una volta che ho elementi individuali li ri-unisco insieme (1 alla volta, quindi inizialmente saranno coppie) e nel fare cio' li sorto
#   3) dopo di che avro' molti array(da due) sortati localmente ma tutti disordinati, qui continuo a sortare tra gli array finche non si ri-unisce tutto in un solo array

#il codice sara' ricorsivo e diviso in 2 parti:
#       1) mergesort(A), che chiama ricorsivamente se stessa finche non si ha un solo elemento e allora chiama merge()
#       2) merge(A,B), che unisce i due array  in un terzo array sortandoli tra di loro

#COMPLESSITA: O(n*log(n))

#ALGORITMO STABILE
#Casi utili: -quando mi serve velocita' e stabilita'

def mergesort(A):
    if len(A) == 1: #se la lunghezza dell' array e' 
        return A
    mid = int(len(A)-1)
    
    #divido l' array in 2    
    array1 = A[0:mid] 
    array2 = A[mid:]
    
    array1 = mergesort(array1) #chiamo ricorsivamente finche non tornano
    array2 = mergesort(array2)
    
    #in pratica riesce ad arrivare fin qui solo quanola funzione mergesort viene chiamate con array di dimensione 1 e quindi ritorna l' array. dopo averli tornati arriviamo qui  e si chiama la merge
    return merge(array1,array2)
    
def merge(A,B): #unisco i due array sortandoli
    C = []
    
    while (len(A) != 0 and len(B) != 0):  #finche uno dei due non ha finito gli elementi
    #controllo elemento per elemento (tanto i due array sono localmente sortati) quindi il primo con il primo etc etc e aggiungo a C togliendo dal mio array
        if A[0] > B[0]:
            C.append(B[0])
            B.pop(0)
        else:
            C.append(A[0])
            A.pop(0)
            
    #ARRIVATI QUI UNO DEI DUE ARRAY NON HA PIU' ELEMENTO
    #PERCIO 'SVUOTO' L' ALTRO; OVVERO AGGIUNGO GLI ELEMENTI RESTANT 
            
    while len(A) != 0:
        C.append(A[0])
        A.pop(0)

    while len(B) != 0:
        C.append(B[0])
        B.pop(0)
        
    return C #ritorna l' algoritmo sortato
        
       
print(f"merge_sort: {mergesort(array)}")           

###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################                                                                                                 
#   ____  _    _ _____ _____ _  __       _____  ____  _____ _______ 
#  / __ \| |  | |_   _/ ____| |/ /      / ____|/ __ \|  __ \__   __|
# | |  | | |  | | | || |    | ' /      | (___ | |  | | |__) | | |   
# | |  | | |  | | | || |    |  <        \___ \| |  | |  _  /  | |   
# | |__| | |__| |_| || |____| . \       ____) | |__| | | \ \  | |   
#  \___\_\\____/|_____\_____|_|\_\     |_____/ \____/|_|  \_\ |_|   
#                                                                   
#                                                                   
#QUICK SORT, ricorsivo Divide et Impera

#KEYWORD: "PIVOT", un elemento che ha alla sua sinistra tutti elementi minori di lui e alla sua destra elementi tutti maggiori di  lui 

#TEORIA:
        
#       1)scelgo un pivot e creo due partizioni: 1 array con elementi minori di lui e un altro array con gli elementi maggiori di lui
#               1.1) inizio da sx e metto un 'leftwall' (ovver l' indice a cui si trova l' ultimo elemento minore del mio pivot finche' ho analizzato
#               1.2) scorro l' array e comparando gli elemento col pivot, se sono minori di lui, diventeranno il nuovo leftwall e li swappo con il leftwall(+1)

#       2)quando l' array e' stato partizionato swappo il pivot on il leftwall e ripeto ricorsivamente il passaggio 1) e 2) finche' non ho un elemento e basta ad array(qui avremo finito)
    
        # sara' composto da due funzioni:
            #1) Quicksort(A,low,high) che ad ogni chiamata chiama Partition e in seguito  ricorsivamente se stessa finche' non abbiamo un solo elemento
            #2) Partition(A,low,high) che si occupa di partizionare l' array in < o > del pivot
            
            
#Casi utili: -solitamente e' il piu' veloce e NON E' STABILE
            
            
#COMPLESSITA: peggiore: O(N^2), medio THETA(N*log_2(N))
            
def quicksort(A,low,high):
    if(low < high): #se ho un solo elemento rimasto nell' array
        pivot = partition(A,low,high) #partiziono l' array
        quicksort(A,low,pivot) #chiamo ricorsivamente l' array dei minori
        quicksort(A,pivot + 1,high) #e l' array dei maggiori, DA NOTARE CHE IL PIVOT VIENE ESCLUSO IN TUTTE E DUE LE CHIAMATE
    return A
        
def partition(A,low,high):
    pivot = A[low] #in  questo caso scelgo il primo el. dell array ma la scelta del pivot e' completamente arbitraria
    leftwall = low #inizializzo il 'leftwall' (indice degli elementi minori o uguali al mio pivot) al primo elemento (il pivot stesso) perche' rende tutto piu' semplice
    
    for i in range(low+1,high,1): #inizio dal secondo elemento perche' il primo e' il pivot
        if A[i] < pivot:
            #swappo l' elemento con il leftwall
            tmp = A[leftwall]
            A[leftwall] = A[i]
            A[i] = tmp
            #incremento di 1 il leftwall
            leftwall = leftwall + 1
    
    tmp_p = A[leftwall]
    pivot = A[leftwall]
    A[low] = tmp_p #il mio ex leftwall viene messo come primo elemento
    
    return leftwall #ritorno la posizione del pivot
    
print(f"quick_sort: {quicksort(array,0,len(array)-1)}")         

###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  

  

#   _____ ____  _    _ _   _ _______ _____ _   _  _____       _____  ____  _____ _______ 
#  / ____/ __ \| |  | | \ | |__   __|_   _| \ | |/ ____|     / ____|/ __ \|  __ \__   __|
# | |   | |  | | |  | |  \| |  | |    | | |  \| | |  __     | (___ | |  | | |__) | | |   
# | |   | |  | | |  | | . ` |  | |    | | | . ` | | |_ |     \___ \| |  | |  _  /  | |   
# | |___| |__| | |__| | |\  |  | |   _| |_| |\  | |__| |     ____) | |__| | | \ \  | |   
#  \_____\____/ \____/|_| \_|  |_|  |_____|_| \_|\_____|    |_____/ \____/|_|  \_\ |_|   
#                                                                                        
#                      

#COUNTING SORT (algoritmo stabile)
#TEORIA: Creo un array delle 'frequenze'; ovvero un array in cui tengo conto del numero delle occorrenze di un determinato elemento nell' array     
                
                #esempio con array = [2,8,5,3,9,4,1,7]



                
#   1)Trovo l' elemento massimo dell' array che sara' la grandezza del mio array delle occorrenze max(array0 = 9
#   2)Conto le occorrenze di ciascun elemento nell' array                                                           
#   3)Modifico l' array delle occorrenze aggiungendo ad ogni suo elemento la somma dei precedenti (es. [0,1,1,1,1,1,0,1,1,1] ---> [0,1,2,3,4,5,5,6,7,8]
#   4)con un array vuoto inizio a posizionare gli oggetti nella loro posizione giusta decrementando sempre di 1 il loro contatore. L' array 'sommato' ci dira' esattamente in quale posizione devo stare
            #es. inizio con il primo elemento '2': [0,1,"2",3,4,5,5,6,7,8]--decremento-->[0,1,"1",3,4,5,5,6,7,8]
            #                                       [0,0,2,0,0,0,0,0,0] e continuo cosi'
            
#COMPLESSITA: O(n + k), dove n è il numero di elementi in input e k è l'intervallo di valori in input.           

#Casi utili: -Molto efficiente quando abbiamo un piccolo intervalli dei possibili valori (es. max(A) = 9), inoltre E' STABILE 

def countingsort(A):
    massimo = max(A)
    minimo = min(A)
    
    B = [0] * (massimo - minimo + 1)
    
    for num in A: #itero ogni elemento dell' array per aggiungere e creare l' array delle occorrenze
        B[num-minimo] += 1 #aggiungo le occorrenze ad ogni elemento
        
    for i in range(1,len(B)): #modifico l' array delle occorrenze per creare l' array 
        B[i] = B[i] + B[i-1]
        
    C = [0] * len(A)
    
    for i in range(len(A)): #questa riga e' brutta perche' in pratica io devo aggiungere il primo elemento di A (nel nostro caso 2) a C nella posizione che mi dice B[primo-elemento-di-A]
        C[B[A[i]-minimo] - minimo] = A[i] #aggiungo a C gli elementi di A. Ricorda l' esempio: A=[2,8,5,3,9,4,1,7], B=[1,2,3,4,5,5,6,7,8], C=[0,2,0,0,0,0,0,0]
        B[A[i]-minimo] -= 1   #decremento gli elementi a B
    
    return C

print(f"counting_sort: {countingsort(array)}")         


    
###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  

#  _____            _____ _______   __     _____  ____  _____ _______ 
# |  __ \     /\   |  __ \_   _\ \ / /    / ____|/ __ \|  __ \__   __|
# | |__) |   /  \  | |  | || |  \ V /    | (___ | |  | | |__) | | |   
# |  _  /   / /\ \ | |  | || |   > <      \___ \| |  | |  _  /  | |   
# | | \ \  / ____ \| |__| || |_ / . \     ____) | |__| | | \ \  | |   
# |_|  \_\/_/    \_\_____/_____/_/ \_\   |_____/ \____/|_|  \_\ |_|   
#                                                                     
#           

#TEORIA:
                # array_esempio = [170,45,75,90,802,24,2,66]
# sortiamo i numeri dalla cifra meno significativa alla piu' significativa    

#STEP (Con esempio):    1) sorto le unita' quindi array [170,45,75,90,802,24,2,66]------------>[170,90,802,2,24,45,75,66]    
                #       2) sorto i decimali quindi [170,90,802,2,24,45,75,66] ------------->[802,2,24,45,66,170,75,90]
                #continuo cosi' per le centinaia [802,2,24,45,66,170,75,90] -------> [2,24,45,66,75,90,170,802] array e' sortato
                
#per farlo applico il Counting Sort per ogni cifra

#quindi e' composto da un radixsort e un countingsort modificato
                
#COMPLESSITA: O(N*k) n è il numero di elementi nell'array di input. k è il numero di cifre nel numero massimo presente nell'array.

#Casi Utili: -intervallo dei valori conosciuto e abbastanza piccolo

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

    return arr

    
print(f"radixsort: {radixsort(array)}")         


###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  
#  _    _ ______          _____        _____  ____  _____ _______ 
# | |  | |  ____|   /\   |  __ \      / ____|/ __ \|  __ \__   __|
# | |__| | |__     /  \  | |__) |    | (___ | |  | | |__) | | |   
# |  __  |  __|   / /\ \ |  ___/      \___ \| |  | |  _  /  | |   
# | |  | | |____ / ____ \| |          ____) | |__| | | \ \  | |   
# |_|  |_|______/_/    \_\_|         |_____/ \____/|_|  \_\ |_|   
#                                                                 
#                                                                

#L' HEAP e' un albero binario ordinato
#un MAX-HEAP e' un heap con ogni parent>child

#codice sara' diviso in: build_max_heap()--- crea un max-heap da un unsorted array
#                        heapify() ---- simile a build_max_heap ma assume che l' array e' gia sortato          

#PROCEDIMENTO: 1)crea max-heap
#              2)rimuovi l' elemento piu' grande
#              3)metti l' item in una partizione sortata
#              4)ripeti

#esempio con array= [2,8,5,3,9,1]-------build_max_heap-----> [9,8,5,3,2,1] ------- swappo 9 con l' ultimo elemento ----> [1,8,5,3,2,9] e non lo considero piu' nel mio "heap" (perche' e' gia' sortato)
#ripeto

#formato da 3 funzioni: heapsort(A), heapify(A,i)


#COMPLESSITA:  O(n log n)

#Casi utili: -nella pratica piu' lento di quicksort, e' ottimo quando vogliamo ordinamento in-place , NON E' STABILE

def heapify(arr,n, i):
    largest = i  # inizialissmo il piu' grande come il parent (con cui e' stata chiamata heapify questa volta)
    
    #ricorda appunto che un heap e' fatto in modo tale che alla sinistra di un elemento 'i' c'e' quello con indice 2*i + 1 e a destra 2*i + 2
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2

    #controllo se esiste la sinistra e se e' maggiore del parent
    if l < n and arr[i] < arr[l]:
        largest = l

    #  controllo se esiste la sinistra e se e' maggiore del parent

    if r < n and arr[largest] < arr[r]:
        largest = r

    # se il parent i non e' il piu grande allor devo swappare il piu' grande largest con il parent i e chiamo di nuovo heapify ricorsivamente, stavolta con largest come parent
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    
    # creo un max-heap.
    for i in range(n, -1, -1):#iterando dal piu grande al piu' piccolo
        heapify(arr, n, i)
        
    for i in range(n - 1, 0, -1): #iterando al contrario 
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

    return arr

print(f"heapsort: {heapsort(array)}")         


###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  
###################################################################################################################################################################################
###################################################################################################################################################################################  
###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  
###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  

#  ____ _____ _   _          _______     __     _____ ______          _____   _____ _    _ 
# |  _ \_   _| \ | |   /\   |  __ \ \   / /    / ____|  ____|   /\   |  __ \ / ____| |  | |
# | |_) || | |  \| |  /  \  | |__) \ \_/ /    | (___ | |__     /  \  | |__) | |    | |__| |
# |  _ < | | | . ` | / /\ \ |  _  / \   /      \___ \|  __|   / /\ \ |  _  /| |    |  __  |
# | |_) || |_| |\  |/ ____ \| | \ \  | |       ____) | |____ / ____ \| | \ \| |____| |  | |
# |____/_____|_| \_/_/    \_\_|  \_\ |_|      |_____/|______/_/    \_\_|  \_\\_____|_|  |_|
#                                                                                          
#                                                                                          


#TEORIA: devo cercare un elemento in un array sortato:
#       1) controllo se l' elemento al centro dell' array e' l'elemento che cercavo(se lo e' mi fermo)
#       2) se il centro e' maggiore ripeto lo stesso procedimento ma considerando solo l' array A[mid:], altrimenti l' opposto
#       3) mi fermo solo quando il mid e' l' elemento che cercavo

#COMPLESSITA: O(log_2(N))

def binary_search_iterativa(A,target):
    left = 0
    right = len(A) -1
    
    while left <= right: #itero finche' non ho iterato tutto
        mid = (right+left)//2
        
        if A[mid] == target: #se il mio target e' il mid ritorno la posizione
            return mid
            
            #altrimenti studio solo gli array (escludento il mid) alla dx o sx del mid
        elif A[mid] > target:
            right = mid -1
        elif A[mid] < target:
            left = mid + 1
            
    return -1 #se non trovo il target torno -1
    
    
def binary_search_ricorsiva(A,target,left,right):

    if right >= left:
        mid = (right+left)//2
        
        if A[mid] == target: #se il mio target e' il mid ritorno la posizione
            return mid
            
            #altrimenti studio solo gli array (escludento il mid) alla dx o sx del mid
        elif A[mid] > target:
            right = mid -1
            return binary_search_ricorsiva(A,target,left,right)
        elif A[mid] < target:
            left = mid + 1
            return binary_search_ricorsiva(A,target,left,right)
    else:
        return -1

array_sortato = heapsort(array)
print(f"binary_search_iterativa, cerco il 7 in: {array_sortato}: {binary_search_iterativa(array_sortato,7)}")       
print(f"binary_search_ricorsiva, cerco il 7 in: {array_sortato}: {binary_search_ricorsiva(array_sortato,7,0,len(array_sortato)-1)}")         


###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  
###################################################################################################################################################################################
###################################################################################################################################################################################  
###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  
###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  
#  _____  ______ _____ 
# |  __ \|  ____/ ____|
# | |  | | |__ | (___  
# | |  | |  __| \___ \ 
# | |__| | |    ____) |
# |_____/|_|   |_____/ 
#                      
#                      
#DFS (Depth-First-Search), algoritmo per esplorare una componente connessa esplorando 
#La classificazione dei nodi in white, gray e black è una tecnica comune per tenere traccia dello stato dei nodi durante un attraversamento DFS.

#White rappresenta un nodo non visitato.
#Gray rappresenta un nodo visitato ma non ancora completamente esplorato.
#Black rappresenta un nodo completamente esplorato.

def DFS(graph):
        color = {node: 'WHITE' for node in graph}

