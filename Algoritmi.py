

array = [2,8,5,3,9,4,1,7]


###############################################################################################
###############################################################################################
#   _____  ____  _____ _______              _      _____  ____  _____  _____ _______ _    _ __  __  _____ 
#  / ____|/ __ \|  __ \__   __|       /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |/ ____|
# | (___ | |  | | |__) | | |         /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / | (___  
#  \___ \| |  | |  _  /  | |        / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |\___ \ 
#  ____) | |__| | | \ \  | |       / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |____) |
# |_____/ \____/|_|  \_\ |_|      /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_|_____/ 
#                                                                                                         


#TABELLA DELLE COMPLESSITA':

#ALGORITMO        |  WORST-CASE     |  AVERAGE CASE
#-----------------------------------------------------
#INSERTION-SORT   | Theta(n^2)      | Theta(n^2)     |    
#-----------------------------------------------------
#MERGE-SORT       | Theta(n*log(n)) | Theta(n*log(n))|
#-----------------------------------------------------
#HEAP-SORT        | O(n*log(n))     | --             |
#-----------------------------------------------------
#QUICK-SORT       | Theta(n^2)      | Theta(n*log(n))| (expected)
#-----------------------------------------------------
#COUNTING-SORT    | Theta(k + n)    | Theta(k+n)     |
#-----------------------------------------------------
#RADIX-SORT       | Theta(d(n+k))   | Theta(d(n+k))  |  
#-----------------------------------------------------
#BUCKET-SORT      | Theta(n^2)      | Theta(n)       |    (average-case)
#-----------------------------------------------------

#                   TERMINI

#ALGORITMI STABILI: algoritmi che mantengono l' ordine relativo deglie elementi ( in pratica, se due 
# elementi sono uguali l' algoritmo garantisce che l' ordine originale tra questi due elementi sara' mantenuto anche dopo il sort)

#ALGORITMO IN-PLACE:un algoritmo che richiede una quantita' di memoria ausiliaria che non cambia con la dimensione del problema. (Ovvero una qta' costante di memoria extra)
#IN PRATICA MODIFICA I DATI SULLA POSIZIONE ORIGINALE SENZA L' USO DI STRUTTURE AUSILIARIE

#ALGORITMO GREEDY:è un algoritmo di risoluzione dei problemi che segue la strategia di fare la scelta ottimale in ogni fase con l'aspettativa che queste scelte locali ottimali condurranno a una soluzione globale ottimale.



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
#   1)dividere array in 2 sotto array finche' ogni sottoarray ha un solo elemento
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
                
                #esempio con array = [2,8,5,3,9,4,1,7]   []


                
#   1)Trovo l' elemento massimo dell' array che sara' la grandezza del mio array delle occorrenze max(array0 = 9
#   2)Conto le occorrenze di ciascun elemento nell' array                                                           
#   3)Modifico l' array delle occorrenze aggiungendo ad ogni suo elemento la somma dei precedenti (es. [1,1,1,1,1,0,1,1,1] ---> [0,1,2,3,4,5,5,6,7,8]
#   4)con un array vuoto inizio a posizionare gli oggetti nella loro posizione giusta decrementando sempre di 1 il loro contatore. L' array 'sommato' ci dira' esattamente in quale posizione devo stare
            #es. inizio con il primo elemento '2': [1,"2",3,4,5,5,6,7,8]--decremento-->[1,"1",3,4,5,5,6,7,8]
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

#Un ALBERO DELLE DECISIONI è un modello delle possibili conseguenze di una serie di decisioni correlate, spesso utilizzato nell'analisi dei processi decisionali. 
#Nel contesto degli algoritmi di ordinamento, un albero delle decisioni potrebbe rappresentare le diverse scelte che un algoritmo potrebbe fare durante il processo di ordinamento.

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




###VERSIONE ALTERNATIVA:
# HEAPSORT(A):
    # BUILD-MAX-HEAP(A)
    # for i = A.length downto 2:
        # swap(A[1],A[i])
        # A.heap_size = A.heap_size - 1
        # MAX-HEAPIFY(A,1)
        
# BUILD-MAX-HEAP(A):
    # A.heap_size = A.length
    # for i = (A.length/2) downto 1:
        # MAX-HEAPIFY(A,i)
        
# MAX-HEAPIFY(A,i):
    # l = LEFT(i)
    # r = RIGHT(i)
    
    # if l<= H.heap_size and A[l] > A[i]:
        # largest = l
    # else:
        # largest = i
    
    # if r<= A.heap_size and A[r] > A[largest]:
        # largest = r
    # if largest != i:
        # swap(A[i],A[largest])
        # MAX-HEAPIFY(A,largest)
        
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

#                                                                                                         
#         GGGGGGGGGGGGG RRRRRRRRRRRRRRRRR                 AAA               FFFFFFFFFFFFFFFFFFFFFF IIIIIIIIII
#      GGG::::::::::::G R::::::::::::::::R               A:::A              F::::::::::::::::::::F I::::::::I
#    GG:::::::::::::::G R::::::RRRRRR:::::R             A:::::A             F::::::::::::::::::::F I::::::::I
#   G:::::GGGGGGGG::::G RR:::::R     R:::::R           A:::::::A            FF::::::FFFFFFFFF::::F II::::::II
#  G:::::G       GGGGGG   R::::R     R:::::R          A:::::::::A             F:::::F       FFFFFF   I::::I  
# G:::::G                 R::::R     R:::::R         A:::::A:::::A            F:::::F                I::::I  
# G:::::G                 R::::R     R:::::R        A:::::A A:::::A           F::::::FFFFFFFFFF      I::::I  
# G:::::G    GGGGGGGGGG   R:::::::::::::RR         A:::::A   A:::::A          F:::::::::::::::F      I::::I  
# G:::::G    G::::::::G   R::::RRRRRR:::::R       A:::::A     A:::::A         F:::::::::::::::F      I::::I  
# G:::::G    GGGGG::::G   R::::R     R:::::R     A:::::AAAAAAAAA:::::A        F::::::FFFFFFFFFF      I::::I  
# G:::::G        G::::G   R::::R     R:::::R    A:::::::::::::::::::::A       F:::::F                I::::I  
#  G:::::G       G::::G   R::::R     R:::::R   A:::::AAAAAAAAAAAAA:::::A      F:::::F                I::::I  
#   G:::::GGGGGGGG::::G RR:::::R     R:::::R  A:::::A             A:::::A   FF:::::::FF            II::::::II
#    GG:::::::::::::::G R::::::R     R:::::R A:::::A               A:::::A  F::::::::FF            I::::::::I
#      GGG::::::GGG:::G R::::::R     R:::::RA:::::A                 A:::::A F::::::::FF            I::::::::I
#         GGGGGG   GGGG RRRRRRRR     RRRRRRAAAAAAA                   AAAAAAAFFFFFFFFFFF            IIIIIIIIII



#GRAFO ORIENTATO
#Se i lati sono contrassegnati da delle frecce si parla di grafo orientato.
#in pratica se gli archi possono essere percorsi solo per il  verso dove punta la freccia

#GRAFI PESATI
#I grafi pesati sono una forma di grafi in cui ad ogni arco è associato un peso o un valore numerico. 
#Questo valore numerico può rappresentare diverse informazioni, come la distanza, il costo, il tempo o qualsiasi altra misura relativa all'arco.

#ORDINAMENTO TOPOLOGICO
#In teoria dei grafi un ORDINAMENTO TOPOLOGICO (in inglese topological sort) è un ordinamento lineare di tutti i vertici di un grafo diretto. 
#I nodi di un grafo si definiscono ordinati topologicamente se i nodi sono disposti in modo tale che ogni nodo viene
#si applica ai DAG(Grafi Diretti Aciclici)


#ORDINE DI UN NODO
#Un nodo è caratterizzato dal suo ordine, che è pari al numero di lati che terminano sul nodo stesso.

#MAGLIA
#È un sottografo in cui tutti i nodi hanno ordine 2; la maglia è dunque una figura chiusa.

#GRAFO CONNESSO
#È un grafo sul quale esiste almeno un percorso che unisce una qualunque coppia di nodi sul grafo. 
#In un grafo connesso non vi possono quindi essere nodi isolati

#ALBERO
#È un sottografo che contiene tutti i nodi; i nodi sono collegati e non sono presenti maglie.
#Poiché tutti i nodi sono collegati, l’albero conterrà (N − 1) lati del grafo diorigine. 
#La scelta dell’albero non è univoca

#ALBERO A STELLA
#È un albero in cui tutti gli N − 1 lati escono dallo stesso nodo. L’albero a
#stella è realizzabile solo se nel grafo esiste almeno un nodo di ordine N − 1.
#Il nodo comune è detto nodo radice.

#SINK UNIVERSALE
#Un "sink universale" è un concetto che si applica ai grafi diretti. 
#In un grafo diretto, un sink è un nodo che non ha alcun arco uscente, cioè non ha archi che puntano ad altri nodi del grafo.
#Il "sink universale" è una caratteristica interessante di alcuni grafi diretti. 
#Questo nodo speciale rappresenta una sorta di "destinazione finale" per tutti gli altri nodi del grafo. 


#CAMMINI MINIMI DA SORGENTE SINGOLA
#Questi algoritmi sono utilizzati per trovare il percorso di costo minimo da una sorgente (un nodo di partenza) a tutti gli altri nodi nel grafo. 
#In altre parole, l'obiettivo è determinare il percorso più breve da un nodo di partenza a tutti gli altri nodi. 
#Gli algoritmi più comuni per i cammini minimi da sorgente singola includono l'algoritmo di Dijkstra e l'algoritmo di Bellman-Ford.

#CAMMINI MINIMI TRA TUTTE LE COPPIE
#Questi algoritmi sono utilizzati per trovare il percorso di costo minimo tra tutte le coppie di nodi nel grafo. 
#L'obiettivo è determinare la distanza più breve tra ogni coppia di nodi nel grafo. 
#Gli algoritmi più comuni per i cammini minimi tra tutte le coppie sono l'algoritmo di Floyd-Warshall e l'algoritmo di Johnson.

#POTENZA DI UN GRAFO
#Potenza di un grafo nel contesto dei prodotti di grafi: 
#Data una matrice di adiacenza A di un grafo e un numero intero n, la n-esima potenza del grafo è rappresentata dalla n-esima potenza della sua matrice di adiacenza.



#ALBERO BINARIO DI RICERCA
#Un albero binario di ricerca (Binary Search Tree, BST) è una struttura dati ad albero che ha le seguenti proprietà:
#
#   -Ogni nodo ha un valore chiave e due figli, chiamati figlio sinistro e figlio destro.
#   -Per ogni nodo, tutte le chiavi nel suo sottoalbero sinistro sono minori della sua chiave, e tutte le chiavi nel suo sottoalbero destro sono maggiori della sua chiave.
#   -Ogni sottoalbero (cioè, ogni figlio di ogni nodo) è a sua volta un albero binario di ricerca.
#Queste proprietà rendono molto efficiente la ricerca di una specifica chiave nell'albero. 
#Infatti, la ricerca in un albero binario di ricerca si basa sulla comparazione della chiave da cercare con la chiave del nodo corrente: 
#               se la chiave da cercare è minore, la ricerca prosegue nel sottoalbero sinistro; 
#               se è maggiore, prosegue nel sottoalbero destro.
#
#L'inserimento e la rimozione di nodi in un BST richiedono anch'essi il rispetto delle proprietà degli alberi di ricerca binari.
#
#Tuttavia, un BST può degenerare in una lista se i nodi vengono inseriti in un ordine particolare (ad esempio, in ordine crescente)

#ALBERI ROSSO-NERI
#Gli alberi rosso-neri sono un tipo di albero binario di ricerca equilibrato. 
#Sono stati progettati per mantenere l'altezza dell'albero logaritmica rispetto al numero di elementi in esso, garantendo quindi un tempo di ricerca, inserimento e cancellazione efficiente.
#
#Ogni nodo di un albero rosso-nero ha un attributo extra per il colore: rosso o nero. 
#Questo colore è utilizzato per mantenere l'equilibrio dell'albero durante le operazioni di inserimento e cancellazione.
#
#Un albero rosso-nero deve soddisfare le seguenti proprietà:
#
#        -Ogni nodo è o rosso o nero.
#        -La radice è sempre nera.
#        -Tutte le foglie (NIL o nodi null) sono nere.
#        -Se un nodo è rosso, allora entrambi i suoi figli sono neri.
#        -Per ogni nodo, ogni percorso semplice da quel nodo alle foglie discendenti contiene lo stesso numero di nodi neri.
#        -Quando un nuovo nodo viene inserito o un nodo esistente viene cancellato, può essere necessario cambiare il colore di alcuni nodi e/o eseguire una rotazione (un'operazione che riorganizza i nodi) per mantenere queste proprietà. La rotazione è un'operazione locale che mantiene l'ordine dei nodi nel BST.




#MakeSet(x): Questa operazione crea un nuovo "gruppo" e mette l'oggetto x in quel gruppo. 
#Se pensi ai nodi di un grafo, MakeSet sarebbe come dire "Sto iniziando un nuovo gruppo di nodi connessi, e il primo nodo in questo gruppo è x".

#FindSet(x): Questa operazione ti dice a quale gruppo appartiene l'oggetto x. 
#Questo è utile se stai cercando di capire se due nodi sono nello stesso gruppo (cioè, se sono connessi tra di loro).

#Union(x, y): Questa operazione combina i gruppi di x e y in un unico gruppo. 
#Se x e y sono nodi in un grafo, Union sarebbe come dire "Ho scoperto che c'è un percorso tra x e y, quindi devo combinare i loro gruppi per riflettere il fatto che sono connessi".

#La funzione RELAX() è un'operazione fondamentale negli algoritmi su grafi ponderati, 
#come l'algoritmo di Dijkstra e l'algoritmo di Bellman-Ford. 
#Questa funzione tenta di migliorare la stima più breve conosciuta del percorso dal nodo iniziale a un determinato nodo, attraverso l'uso di un arco specifico.

###################################################################################################################################################################################
###################################################################################################################################################################################
###################################################################################################################################################################################  


grafo = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
#componente connessa: 
#  _____  ______ _____ 
# |  __ \|  ____/ ____|
# | |  | | |__ | (___  
# | |  | |  __| \___ \ 
# | |__| | |    ____) |
# |_____/|_|   |_____/ 
#                      
#                      
#DFS (Depth-First-Search), algoritmo per esplorare(in Profondita') una componente connessa 
#La classificazione dei nodi in white, gray e black è una tecnica comune per tenere traccia dello stato dei nodi durante un attraversamento DFS.

#White rappresenta un nodo non visitato.
#Gray rappresenta un nodo visitato ma non ancora completamente esplorato.
#Black rappresenta un nodo completamente esplorato.


#in pratica inizio dal primo nodo e poi esploro ricorsivamente tutte gli altri nodi

# Implementazione della funzione DFS
# Insieme per memorizzare i nodi visitati

    #DFS(ARRAY_NODI_VISITATI, GRAFO, NODO_ATTUALE)
    
    
def dfs(visited, grafo, nodo):
    print(nodo, end = " ")
    visited.add(nodo)#aggiungo il nodo corrente all' insieme dei visitati
    for vicino in grafo[nodo]:#esploro ogni vicino del mio nodo ma solo se non e' stato gia' visitato
        if vicino not in visited:
            dfs(visited, grafo, vicino)

# Esegui la funzione DFS

print("\nDFS:")
dfs(visited, grafo, 'A')


###########################################################################################################################################################################
#DFS ALTERNATIVA
#    DFS(G):
#        for u in G.V:               #inizializzo ogni nodo come bianco 
#            u.color = WHITE         #e con parent infinito
#            u.parent = null
#        time = 0                    #time 0 (per il sort topologico(?))
#        for u in G.V:               #per ogni nodo nel grafo se e' bianco(non e' stato visitato), chiamo DFS-visit
#            if u.color == WHITE:
#                DFS-VISIT(G,u)
#
#esplora la componente connessa
#   DFS-VISIT(G,u):                 
#        time = time+1              #incrementa il tempo
#        u.d = time                 #la distanza viene settata al tempo
#        u.color = GRAY             #il colore e' ora grigio perche' ho visitato lui ma non ancora i suoi neighbour
#        for v in G[u]              #per ogni neighbour del nodo se sono bianchi gli setto il parent al mio nodo
#            if v.color == WHITE:   #e chiamo la DFS-visit con loro
#            v.parent = u
#           DFS-VISIT(G,v)
#        u.color = BLACK            #dopo aver chiamato la dfs-visit per ogni vicino del mio nodo finalmente setto il mio nodo a BLACK(tutti i vicini visitati)
#        time = time+1              
#        u.f=time
###########################################################################################################################################################################



###################################################################################################################################################################################
###################################################################################################################################################################################
################################################################################################################################################################################### 

#  ____  ______ _____ 
# |  _ \|  ____/ ____|
# | |_) | |__ | (___  
# |  _ <|  __| \___ \ 
# | |_) | |    ____) |
# |____/|_|   |_____/ 
#                     
#                     
#BFS è un algoritmo di ricerca su grafico che visita i nodi in "ampiezza"
#visita prima tutti i nodi adiacenti a un nodo dato, prima di passare ai nodi di livello successivo. 
#in pratica funziona a "Livelli" orizzontali. cioe' prima di passare al livello successivo finisce quelli del suo livello

#crea una 'coda', .Itera finche' non e' vuota ed elimina il primo elemento(ovvero quello che abbiamo appena visitato)
    #ARRAY_VISITATI,GRAFO, NODO_CORRENTE
visited2 = []
def bfs(visited2, graph, node): #function for BFS

    queue = []

    visited2.append(node) #visito il primo nodo e lo aggiungo alla lista
    queue.append(node)

    while queue:          # finche' la coda non e' vuota
        m = queue.pop(0)  #poppo il primo el. della coda
        print(m, end = " ") 

        for neighbour in graph[m]: #per ogni vicino del mio nodo se non e' stato visitato lo visito e lo aggiungo alla coda
            if neighbour not in visited2: 
                visited2.append(neighbour)
                queue.append(neighbour)
            
print("\nBFS:")
bfs(visited2,grafo, 'A')


#BFS ALTERNATIVA
#funzionamento. ogni nodo che visito lo pusho nella queue(quando e' GRAY) e quando e' black lo dequeuo e diventa un parent

#BFS(G,s):
#    for u in G.V-{s}: #setuppo tutti i nodi eccetto il nodo di partenza
#        u.color = WHITE 
#        u.d = infinity
#        u.parent = null
        
#    s.color = gray  #setuppo il nodo di partenza
#    s.d = 0
#    s.parent - null
#    Q= vuoto
#    ENQUEUE(Q,s) #pusho s nella queue
#    while Q != vuoto:
#        u = dequeue(Q) # u = elemento che poppo da Q
#        for v in G[u]: #per ogni neighbour
#            if v.color == WHITE: #per ogni neighbour non esplorato
#                v.color = GRAY      #neighbour diventa gray---> esplorato
#                v.d = u.d+1
#                v.parent = u        #il suo parent e' settato al nodo original ovviamente
#                ENQUEUE(Q,v)        #lo aggiungo alla queue in quanto appena esplorato
#        u.color = BLACK #tutti neighbour esplorati-----> nodo diventa black



###################################################################################################################################################################################
###################################################################################################################################################################################
################################################################################################################################################################################### 


#  __  __  _____ _______ 
# |  \/  |/ ____|__   __|
# | \  / | (___    | |   
# | |\/| |\___ \   | |   
# | |  | |____) |  | |   
# |_|  |_|_____/   |_|   
#                        
# 
#MINIMUM SPANNING TREE (Grafi pesati ovviamente)
#è un albero di copertura che include tutti i vertici del grafo originale e che ha il peso minimo possibile. 
#In altre parole, la somma dei pesi di tutti i lati dell'albero di copertura è la più piccola possibile.
#Ci sono vari algoritmi che possono essere utilizzati per trovare il Minimum Spanning Tree di un grafo. Due dei più noti sono l'algoritmo di PRIM e l'algoritmo di KRUSKAL.
#
#L'Algoritmo di Prim inizia da un nodo arbitrario e cresce l'albero un nodo alla volta, sempre scegliendo il nodo più vicino al nodo attuale che non faccia parte dell'albero.
#L'Algoritmo di Kruskal, invece, inizia considerando ogni nodo come un albero a sé stante e unisce gli alberi scegliendo sempre l'arco più leggero che connette due alberi differenti.


#SAFE EDGE
#Nell'ambito degli alberi di copertura minima (Minimum Spanning Trees, MST), 
#un "SAFE EDGE" è un arco che può essere aggiunto all'albero di copertura senza violare la proprietà dell'albero di copertura.
#Più specificamente, un arco è "safe" se il suo aggiunta all'albero di copertura corrente non forma un ciclo e non aumenta il costo totale dell'albero di copertura oltre il minimo possibile.
#Gli algoritmi di Prim e Kruskal, ad esempio, costruiscono l'albero di copertura aggiungendo ripetutamente un "safe edge":
    #l'arco di peso minimo che collega un nodo nell'albero di copertura con un nodo fuori dall'albero di copertura (nel caso di Prim) 
    #o l'arco di peso minimo tra qualsiasi coppia di nodi in cui uno è nell'albero e l'altro no (nel caso di Kruskal).

#KRUSKAL!!
#1) prendo l' arco piu' piccolo
#2) continuo a prnedere l' arco piu' piccolo a patto che non crei un ciclo(semplicemente prendo un arco il cui vertice non sa gia' nei visitati)
#

#Time complexity O(E log(E)) (perche' devo sortare gli archi, uso mergesort ad esempio)

#MST-KRUSKAL(G,w):
#    A = vuoto
#    for v in G.V:
#        Make-SET(v)                     #crea un insieme contenente elemento v(e gli elementi a lui connessi(?))
#    sort(G.E)                           #sorta gli archi  
#    for (u,v) in G.E: (per ogni arco )
#        if Find-SET(u) != Find-SET(v):  #se i due vertici sono in insiemi diversi(non creo un ciclo)
#            A = A + (u,v)               #aggiungo l' arco al mio MST
#            UNION(u,v)                  #unisco i due gruppi dei vertici
#    return A
            
            
                                
#PRIM!!
#1) creo una empty list visited = []
#2) picko un vertice a caso e aggiungo al visited
#3) checko tutti gli archi e scelgo l' arco di costo minore(GREEDY ALGORITHM!!!) e aggiungo il nuovo vertice a visited
#4) controllo tutti gli archi 'disponibili' e scelgo il piu' corto (sempre a patto che non ci siano cicli)
#5) ripeto finche'

#MST-PRIM(G,w,r):
#    for u in G.V:                                   #setuppo i vertici
#        u.key = infinity
#        u.parent = null
#        
#    r.key = 0                                       #nodo di partenza, distanza 0
#    Q = G.V:                                        # Q insieme degli unvisited nodes
#    while Q != vuoto:                               # finche' non l'ho svuotato
#        u = EXTRACT-MIN(Q)                          #picko un vertice a caso() e lo rimuovo da Q
#        for v in G[u]:                              #per ogni suo neighbour
#            if v in Q and w(u,v) < v.key:           # se V non e' visitato ancora(se e' ancora in Q) e il costo dell' arco e' minore di v.key
#                v.parent = u                        #setto il parent e la key al vertice/arco u--(u,v)
#                v.key = w(u,v)


###################################################################################################################################################################################
###################################################################################################################################################################################
################################################################################################################################################################################### 

#    _____ _____ _   _  _____ _      ______       _____ _    _  ____  _____ _______     _____     _______ _    _ 
#   / ____|_   _| \ | |/ ____| |    |  ____|     / ____| |  | |/ __ \|  __ \__   __|   |  __ \ /\|__   __| |  | |
#  | (___   | | |  \| | |  __| |    | |__       | (___ | |__| | |  | | |__) | | |______| |__) /  \  | |  | |__| |
#   \___ \  | | | . ` | | |_ | |    |  __|       \___ \|  __  | |  | |  _  /  | |______|  ___/ /\ \ | |  |  __  |
#   ____) |_| |_| |\  | |__| | |____| |____      ____) | |  | | |__| | | \ \  | |      | |  / ____ \| |  | |  | |
#  |_____/|_____|_| \_|\_____|______|______|    |_____/|_|  |_|\____/|_|  \_\ |_|      |_| /_/    \_\_|  |_|  |_|


#ARCHI PESATI OVVIAMENTE


#abbiamo lo scopo di trovare il percorso piu' corto da un nodo specifico di partenza a tutti gli altri nodi del grafo

#La funzione RELAX() prende come input un arco (u, v) e un array di stime di distanze. 
#Se il costo del percorso dal nodo iniziale a v attraverso u è inferiore alla stima corrente della distanza da u a v, allora la stima viene aggiornata con il costo inferiore.

#################################################################################

#RELAX(u,v,w):
#    if v.d > u.d + w(u,v):   # se la distanza attuale per arrivare a v e' maggiore della distanza passando per u
#        v.d = u.d+w(u,v)     # allora aggiorno la distanza per arrivare a v, mettendo come percorso migliore il passaggio per u
#        v.parent = u         #quindi u diventa parent di v


#################################################################################
#BELLMAN FORD  
#1) creo una tabella delle distanze da s nodo di partenza; (tutti a infinito tranne s a 0)
#2) esploro tutti i suoi nodi adiacenti e aggiorno le distanze chiamando la RELAX
#3) ripeto per ogni nodo  cui mi connetto

#TIME-COMPLEXITY: (V*E)

#BELLMAN-FORD(G,w,s):
#    INITIALIZE-SINGLE-SOURCE(G,s)       #inizializzo s come nodo di partenza (s.d = 0, altri_nodi.d = infinity)
#    for i = 1 to len(G.V - 1):          #itero per ogni vertice ogni arco e RILASSO (provo ogni cammino per arrivare a quel vertice in pratica)
#        for (u,v) in G.E:              
#            RELAX(u,v,w)
#    for (u,v) in G.E:
#        if v.d > u.d + w(u,v):          #provo un' altra RELAX e checko se ha funzionato
#            return FALSE
#    return TRUE

#################################################################################

#DIJKSTRA
#teniamo una lista di UN-VISITED nodes

#1)inizializzo i vertici e il nodo di partenza (s.d = 0, altri_nodi.d = infinity)
#2)aggiorno le distanze esplorando gli archi adiacenti 
#3)avanzo sull' arco con peso minore e continuo l' esplorazione
#4) scelgo l' arco meno costoso tra tutti quelli esplorabili
#5) ripeto fino a che ho visitato ogni nodo

#TIME-COMPLEXITY: O(E + V*log(V))

#DIJKSTRA(G,w,s):
#    INITIALIZE-SINGLE-SOURCE(G,s)       #inizializzo s come nodo di partenza (s.d = 0, altri_nodi.d = infinity)
#    S = vuoto                           #
#    Q = G.V                             #Q insieme degli unvisited nodes
#
#    while Q != vuoto:                   #itero finche' non li ho visitati tutti
#        u = EXTRACT-MIN(Q)              #picko un vertice a caso() e lo rimuovo da Q
#        S = S + {u}                     #lo aggiungo alla tabella
#        for v in G[u]:                  #per ogni neighbour
#            RELAX(u,v,w)                #RILASSO gli archi

###################################################################################################################################################################################
###################################################################################################################################################################################
################################################################################################################################################################################### 


#             _      _          _____        _____ _____         _____ _    _  ____  _____ _______     _____     _______ _    _ 
#       /\   | |    | |        |  __ \ /\   |_   _|  __ \       / ____| |  | |/ __ \|  __ \__   __|   |  __ \ /\|__   __| |  | |
#      /  \  | |    | |  ______| |__) /  \    | | | |__) |     | (___ | |__| | |  | | |__) | | |______| |__) /  \  | |  | |__| |
#     / /\ \ | |    | | |______|  ___/ /\ \   | | |  _  /       \___ \|  __  | |  | |  _  /  | |______|  ___/ /\ \ | |  |  __  |
#    / ____ \| |____| |____    | |  / ____ \ _| |_| | \ \       ____) | |  | | |__| | | \ \  | |      | |  / ____ \| |  | |  | |
#   /_/    \_\______|______|   |_| /_/    \_\_____|_|  \_\     |_____/|_|  |_|\____/|_|  \_\ |_|      |_| /_/    \_\_|  |_|  |_|
#                                                                                                                                    

#FLOYD-WARSHALL (grafi orientati)   K-I-J
#1)inizializzo una matrice delle distanze(distanza tra gli stessi nodi e' 0, la diagonale)
#2)loopo una volta tutti gli archi e immetto il peso diretto tra i vertici di quell'  arco nella matrice
#3)NESTED FOR LOOP
#   3.1)per ogni k
#       3.2)per ogni i
#           3.3) per ogni j
#               3.4) faccio una relax ovvero :(checko se la distanza tra i e j e' maggiore della stessa distanza ma passanto per k)
                        #IF dist[i][j] > dist[i][k] + dist[k][j]: ------> aggiorno la matrice

#TIME-COMPLEXITY: O(V^3)

#FLOYD-WARSHALL(G):
#    D = G.V*G.V                 #creo una matrice delle distanze dei vertici
#    for v in len(G.V):
#        D[v][v] = 0             #inizializzo la diagonale a tutti 0(le distanze tra A ed A. tra B e b etc etc)
#    for e(u,v) in G.E:          #inizializzo ogni elemento della matrice collegato da archi diretti con le sue distanze dirette
#        D[u][v] = e(u,v)

#    for k in len(G.V):
#        for i in len(G.V):
#            for j in len(G.V):
#                if D[i][j] > D[i][k] + D[k][j]:     #se la distanza diretta e' maggiore che la distanza passando per un punto in mezzo
#                    dist[i][j]  = D[i][k] + D[k][j]:#aggiorno la matrice
    
#################################################################################
#JOHNSON ALGORITHM
#L'algoritmo di Johnson è un algoritmo per trovare i cammini minimi più brevi tra tutti i nodi di un grafo diretto pesato. 
#Può gestire i pesi negativi degli archi, a condizione che non ci siano cicli di costo negativo.
#Per i grafi sparsi, l'algoritmo di Johnson può essere più efficiente dell'algoritmo di Floyd-Warshall, che risolve lo stesso problema.
    
#Ecco un'idea di base dell'algoritmo di Johnson:
#1)aggiungi un nuovo nodo al grafo, con archi di peso 0 che vanno dal nuovo nodo a tutti gli altri nodi.

#2)Usa l'algoritmo di Bellman-Ford, partendo dal nuovo nodo, per determinare i pesi minimi verso tutti gli altri nodi. Se rilevi un ciclo di costo negativo, termina l'algoritmo.

#3)Ripesa il grafo: per ogni arco (u, v) con peso w(u, v), aggiorna il peso a w(u, v) + h(u) - h(v), 
#dove h(u) è la distanza minima dal nuovo nodo a u, come calcolato dal passaggio 2. Questo passaggio produce un grafo con pesi positivi, preservando le relazioni di ordine dei cammini minimi.

#4)Per ogni nodo nel grafo, applica l'algoritmo di Dijkstra per trovare la distanza più breve da quel nodo a tutti gli altri nodi nel grafo ripesato.

#5)Converti i pesi dei cammini minimi nel grafo ripesato ai loro valori originali.
    
def johnson(graph):
    # Aggiungi un nuovo nodo s e connettilo a tutti gli altri nodi con peso 0
    graph['s'] = {node: 0 for node in graph.keys()}

    # Calcola i pesi minimi da s a ogni nodo usando Bellman-Ford
    weights = bellman_ford(graph, 's')

    # Ricalcola i pesi del grafo
    for u in graph:
        for v in graph[u]:
            graph[u][v] += weights[u] - weights[v]

    # Rimuovi il nodo aggiunto
    del graph['s']

    # Calcola i percorsi più brevi da ogni nodo a ogni altro nodo con Dijkstra
    shortest_paths = {node: dijkstra(graph, node) for node in graph.keys()}

    return shortest_paths

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

#  _    _           _____ _    _      _______       ____  _      ______ 
# | |  | |   /\    / ____| |  | |    |__   __|/\   |  _ \| |    |  ____|
# | |__| |  /  \  | (___ | |__| |       | |  /  \  | |_) | |    | |__   
# |  __  | / /\ \  \___ \|  __  |       | | / /\ \ |  _ <| |    |  __|  
# | |  | |/ ____ \ ____) | |  | |       | |/ ____ \| |_) | |____| |____ 
# |_|  |_/_/    \_\_____/|_|  |_|       |_/_/    \_\____/|______|______|
#                                                                       
#                                                                       


#Le tabelle hash, conosciute anche come mappe hash o dizionari, sono strutture dati che implementano un array associativo, un tipo di struttura che può mappare chiavi a valori. 
#Le tabelle hash utilizzano una funzione hash per calcolare un indice in un array a partire dalla chiave di input. 
#Ciò consente di inserire, rimuovere e cercare elementi in base alla chiave con una complessità temporale media di O(1), cioè in tempo costante.

#KEY--->VALUE


#Ecco come funzionano le tabelle hash:

#Funzione hash: Una funzione hash prende la chiave di input e restituisce un indice dell'array.     HASH(KEY) ------> POSIZIONE_NELL_ARRAY
#un esempio stupido puo' essere, chiamo hash della chiave e faccio ad esempio 
#KEY = 'chiave_prova' ,md5(key) = eecee1abb055b946db4ea4b27c405b39. 
#Per avere il suo indice nell' array potrei fare :     eecee1abb055b946db4ea4b27c405b39  mod (lunghezza_array)                                                                                       
#Questa funzione deve essere abbastanza veloce da calcolare e deve ridurre al minimo le collisioni, cioè situazioni in cui chiavi diverse producono lo stesso indice.


#Inserimento di elementi: Quando si inserisce un elemento, la tabella hash calcola l'indice utilizzando la funzione hash sulla chiave, quindi memorizza il valore all'indice corrispondente nell'array.

#Ricerca di elementi: Quando si cerca un elemento per la sua chiave, la tabella hash calcola nuovamente l'indice utilizzando la funzione hash, 
#quindi restituisce il valore memorizzato all'indice corrispondente.

#Gestione delle collisioni: A volte, due chiavi diverse possono dare lo stesso indice (una collisione). 
#Esistono diverse tecniche per gestire queste collisioni, tra cui :
        #- l'INDIRIZZAMENTO APERTO (in cui si cercano posizioni libere nell'array), in pratica la ficco al primo posto libero 
        #- l'INDIRIZZAMENTO CHIUSO o catenamento (in cui più valori possono essere memorizzati allo stesso indice, spesso utilizzando una struttura dati come una lista o un'altra tabella hash).

#In Python, i dizionari (dict) sono implementati come tabelle hash. Ecco un esempio di utilizzo di un dizionario in Python:

#FATTORE DI CARICO di una tabella hash e' la percentuale di elementi presenti rispetto alla capacità totale della tabella. 
#In altre parole, rappresenta quanto è piena o occupata la tabella hash.



#DIRECT-ADDRESS-SEARCH(T,k)
def search(table, key):
    m = len(table)
    i = 0
    while i < m:
        j = (hash_function(key) + i) % m
        if table[j] is None:  # Se lo slot è vuoto
            return -1  # La chiave non esiste
        if table[j] == key:  # Se la chiave è stata trovata
            return j
        i += 1
    return -1  # La chiave non esiste

#DIRECT-ADDRESS-INSERT(T,x)
def insert(table, key):
    m = len(table)
    i = 0
    while i < m:                        #itero ogni elemento della tabella Hash
        j = (hash_function(key) + i) % m#j = hash(chiave) + indice % lunghezza_tabella
        if table[j] is None:            # Se lo slot è vuoto
            table[j] = key              #aggiungo la chiave allo slot
            return j
        i += 1
    raise Exception("Hash table overflow")

#DIRECT-ADDRESS-DELETE(T,x)
def delete(table, key):
    m = len(table)
    i = 0
    while i < m:
        j = (hash_function(key) + i) % m
        if table[j] is None:  # Se lo slot è vuoto
            return False  # La chiave non esiste
        if table[j] == key:  # Se la chiave è stata trovata
            table[j] = "DELETED"
            return True
        i += 1
    return False  # La chiave non esiste






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


#   __  __ ______ _____ _____          _   _                                                                                         
#  |  \/  |  ____|  __ \_   _|   /\   | \ | |   /\                                                                                   
#  | \  / | |__  | |  | || |    /  \  |  \| |  /  \                                                                                  
#  | |\/| |  __| | |  | || |   / /\ \ | . ` | / /\ \                                                                                 
#  | |  | | |____| |__| || |_ / ____ \| |\  |/ ____ \                                                                                
#  |_|__|_|______|_____/_____/_/    \_\_| \_/_/    \_\                                                                               
#  |  ____|                                                                                                                          
#  | |__                                                                                                                             
#  |  __|                                                                                                                            
#  | |____                                                                                                                           
#  |______|_______    _______ _____  _____ _______ _____ _____ _    _ ______       _____  _    ____  _____  _____ _____ _   _ ______ 
#   / ____|__   __|/\|__   __|_   _|/ ____|__   __|_   _/ ____| |  | |  ____|     |  __ \( )  / __ \|  __ \|  __ \_   _| \ | |  ____|
#  | (___    | |  /  \  | |    | | | (___    | |    | || |    | |__| | |__        | |  | |/  | |  | | |__) | |  | || | |  \| | |__   
#   \___ \   | | / /\ \ | |    | |  \___ \   | |    | || |    |  __  |  __|       | |  | |   | |  | |  _  /| |  | || | | . ` |  __|  
#   ____) |  | |/ ____ \| |   _| |_ ____) |  | |   _| || |____| |  | | |____      | |__| |   | |__| | | \ \| |__| || |_| |\  | |____ 
#  |_____/   |_/_/    \_\_|  |_____|_____/   |_|  |_____\_____|_|  |_|______|     |_____/     \____/|_|  \_\_____/_____|_| \_|______|


#Una STATISTICA D'ORDINE I-esima e' l'I elemento piu' piccolo di un insieme n

#esempio    -Statistica_ordine[i] con i = 1 ------> min(Array)
#           -Statistica_ordine[i] con i = len(Array) ------> max(Array)
#           -Statistica_ordine[i] con i = (len(Array)+1)/2 ------> mediana (superiore o inferiore, dipende)

#PROBLEMA DELLA SELEZIONE: 
    #Input: Array A lungo n, intero    1 <=i<= n
    #                          Output: l' i-esima statistica d'ordine

    #Soluzione banale: 1)Ordina A
    #                  2)Si restituisca l' elemento A[i]
    #Complessita' O(n*log(n))
    #   sortiamo con merge/heapsort e dopo semplicemente prendiamo l' elemento di A
    
#PROBLEMA DEL MASSIMO E MINIMO:
#Quante comparazioni sono necessarie per determinare il minimo di un set di n elementi?
    #Upperbound complessita' O(n-1), E' il meglio che possiamo fare
    #    Minimum(A):
    #        min=A[1]
    #        for i = 2 to A.length:
    #            if min > A[i]:
    #                min = A[i]
    #        return min
    
    #posso pure calcolare insieme massimo e minimo per un costo al massimo di 3(n/2) comparisons 


#PROBLEMA DELLA SELEZIONE IN TEMPO LINEARE
#esegue una sorta di quicksort ma senza sortare
#Il caso medio e' O(n), il caso peggiore e' O(n^2)

#in pratica io devo trovare l' elemento i-esimo in un array, quindi scelgo un pivot e partizionando l' array a quel pivot 
#quindi controllo la lunghezza del subarray che mi si e' venuto a creare partizionando e se la lunghezza e' uguale al mio i-target (che e' un indice) allora ho trovato il target



#RANDOMIZED-SELECT(A,p,r,i):
#    if p == r:
#        return A[p]
#        
#    q = RANDOMIZED-PARTITION(A,p,r) #partiziono con q pivot
#    k = q - p + 1    #k e' il numero di elementi nel subarray che sto studiando
#    if i == k:  #se il numero di elementi nel subarray e' esattamente i allora ho trovato il mio elemento(l' ultimo del subarray)
#        return A[q] 
#    elif i < k: #se invece il subarray e' piu grande dell' indice del mio target allor mi sposto a studiare la parte sinistra del subarray
#        return RANDOMIZED-SELECT(A,p,q-1,i)
#    else:
#        return RANDOMIZED-SELECT(A,q+1,r,i-k)










