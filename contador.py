from operator import itemgetter
import numpy as np

def ContarTxt(nombre_archivo):
    matriz=[]
    for i in range(89):
        matriz.append([0]*2)

    document_text = open(nombre_archivo,'r')
    text_string = document_text.read().lower()

    #definiendo la matriz
    def asignarycalcular(i,caracter):
        matriz[i][0]=caracter
        ocurrencias= text_string.count(caracter)
        if caracter=='a':
            ocurrencias = ocurrencias-(2*matriz[39][1])-(matriz[40][1])-(matriz[41][1])-(matriz[44][1])-(matriz[54][1])-(matriz[55][1])
        if caracter=='b':
            ocurrencias = ocurrencias-(matriz[39][1])-(matriz[40][1])
        if caracter=='c':
            ocurrencias = ocurrencias-(2*matriz[39][1])-(2*matriz[41][1])-(matriz[42][1])-(matriz[43][1])-(matriz[56][1])
        if caracter=='d':
            ocurrencias = ocurrencias-(matriz[43][1])-(matriz[48][1])-(matriz[53][1])-(matriz[55][1])
        if caracter=='e':
            ocurrencias = ocurrencias-(2*matriz[39][1])-(matriz[40][1])-(matriz[41][1])-(matriz[42][1])-(matriz[43][1])-(matriz[44][1])-(2*matriz[45][1])-(matriz[46][1])-(matriz[47][1])-(matriz[48][1])-(matriz[49][1])-(matriz[50][1])-(3*matriz[51][1])-(2*matriz[52][1])-(2*matriz[53][1])-(2*matriz[54][1])-(2*matriz[55][1])-(matriz[56][1])
        if caracter=='f':
            ocurrencias = ocurrencias-(matriz[45][1])-(matriz[49][1])-(matriz[50][1])  
        if caracter=='g':
            ocurrencias = ocurrencias-(matriz[46][1])-(matriz[54][1])-(matriz[55][1])
        if caracter=='h':
            ocurrencias = ocurrencias-(matriz[46][1])-(matriz[49][1])-(matriz[50][1])-(matriz[52][1]) 
        if caracter=='i':
            ocurrencias = ocurrencias-(matriz[46][1])-(matriz[49][1])-(matriz[50][1])
        if caracter=='k':
            ocurrencias = ocurrencias-(2*matriz[39][1])-(matriz[40][1])-(2*matriz[41][1])-(2*matriz[42][1])-(matriz[43][1])-(matriz[44][1])-(matriz[45][1])-(matriz[46][1])-(matriz[47][1])-(matriz[48][1])-(matriz[49][1])-(matriz[50][1])-(matriz[51][1])-(matriz[52][1])-(matriz[53][1])-(matriz[54][1])-(matriz[55][1])-(2*matriz[56][1])
        if caracter=='l':
            ocurrencias = ocurrencias-(matriz[41][1])-(matriz[42][1])-(matriz[44][1])-(matriz[45][1])-(matriz[50][1])-(matriz[56][1])
        if caracter=='m':
            ocurrencias = ocurrencias-(matriz[43][1])-(matriz[52][1])-(matriz[56][1])
        if caracter=='n':
            ocurrencias = ocurrencias-(matriz[48][1])-(matriz[51][1])-(matriz[53][1])-(matriz[55][1])-(matriz[56][1])
        if caracter=='o':
            ocurrencias = ocurrencias-(matriz[41][1])-(matriz[48][1])-(matriz[52][1])-(matriz[55][1])-(matriz[56][1])
        if caracter=='p':
            ocurrencias = ocurrencias-(matriz[39][1])-(matriz[41][1])-(matriz[47][1])-(2*matriz[54][1])-(matriz[55][1])
        if caracter=='r':
            ocurrencias = ocurrencias-(matriz[42][1])-(matriz[46][1])-(matriz[49][1])-(matriz[51][1])-(matriz[55][1])
        if caracter=='s':
            ocurrencias = ocurrencias-(matriz[39][1])-(matriz[41][1])-(matriz[49][1])-(matriz[50][1])
        if caracter=='t':
            ocurrencias = ocurrencias-(matriz[40][1])-(matriz[42][1])-(matriz[44][1])-(matriz[45][1])-(matriz[46][1])-(matriz[49][1])-(matriz[50][1])-(matriz[51][1])   
        if caracter=='u':
            ocurrencias = ocurrencias-(matriz[47][1])-(matriz[54][1])
        if caracter=='w':
            ocurrencias = ocurrencias-(matriz[48][1])-(matriz[55][1])
        if caracter=='y':
            ocurrencias = ocurrencias-(matriz[39][1])-(matriz[40][1])-(matriz[41][1])-(matriz[42][1])-(matriz[43][1])-(matriz[44][1])-(matriz[45][1])-(matriz[46][1])-(matriz[47][1])-(matriz[48][1])-(matriz[49][1])-(matriz[50][1])-(matriz[51][1])-(matriz[52][1])-(matriz[53][1])-(matriz[54][1])-(matriz[55][1])-(matriz[56][1])
        if caracter=='.':
            ocurrencias = ocurrencias-(matriz[39][1])-(matriz[40][1])-(matriz[41][1])-(matriz[42][1])-(matriz[43][1])-(matriz[44][1])-(matriz[45][1])-(matriz[46][1])-(matriz[47][1])-(matriz[48][1])-(matriz[49][1])-(matriz[50][1])-(matriz[51][1])-(matriz[52][1])-(matriz[53][1])-(matriz[54][1])-(matriz[55][1])-(matriz[56][1])    
        if caracter=='_':
            ocurrencias = ocurrencias-(matriz[41][1])-(matriz[49][1])-(matriz[50][1])-(matriz[54][1])-(matriz[55][1])-(matriz[56][1])
        matriz[i][1]=ocurrencias

    #Poblando la matriz
    asignarycalcular(39,'key.backspace')
    asignarycalcular(40,'key.tab')
    asignarycalcular(41,'key.caps_lock')
    asignarycalcular(42,'key.ctrl')
    asignarycalcular(43,'key.cmd')
    asignarycalcular(44,'key.alt')
    asignarycalcular(45,'key.left')
    asignarycalcular(46,'key.right')
    asignarycalcular(47,'key.up')
    asignarycalcular(48,'key.down')
    asignarycalcular(49,'key.shift_r')
    asignarycalcular(50,'key.shift_l')
    asignarycalcular(51,'key.enter')
    asignarycalcular(52,'key.home')
    asignarycalcular(53,'key.end')
    asignarycalcular(54,'key.page_up')
    asignarycalcular(55,'key.page_down')
    asignarycalcular(56,'key.num_lock')
    asignarycalcular(0,'a')
    asignarycalcular(1,'b')
    asignarycalcular(3,'c')
    asignarycalcular(4,'d')
    asignarycalcular(5,'e')
    asignarycalcular(6,'f')
    asignarycalcular(7,'g')
    asignarycalcular(8,'h')
    asignarycalcular(9,'i')
    asignarycalcular(10,'j')
    asignarycalcular(11,'k')
    asignarycalcular(12,'l')
    asignarycalcular(13,'m')
    asignarycalcular(14,'n')
    asignarycalcular(15,'ñ')
    asignarycalcular(16,'o')
    asignarycalcular(17,'p')
    asignarycalcular(18,'q')
    asignarycalcular(19,'r')
    asignarycalcular(20,'s')
    asignarycalcular(21,'t')
    asignarycalcular(22,'u')
    asignarycalcular(23,'v')
    asignarycalcular(24,'w')
    asignarycalcular(25,'x')
    asignarycalcular(26,'y')
    asignarycalcular(27,'z')
    asignarycalcular(28,'1')
    asignarycalcular(29,'2')
    asignarycalcular(30,'3')
    asignarycalcular(31,'4')
    asignarycalcular(32,'5')
    asignarycalcular(33,'6')
    asignarycalcular(34,'7')
    asignarycalcular(35,'8')
    asignarycalcular(36,'9')
    asignarycalcular(37,'0')
    asignarycalcular(38,' ')
    asignarycalcular(57,'*')
    asignarycalcular(58,'-')
    asignarycalcular(59,'+')
    asignarycalcular(60,'/')
    asignarycalcular(61,'=')
    asignarycalcular(62,'.')
    asignarycalcular(63,':')
    asignarycalcular(64,'_')
    asignarycalcular(65,',')
    asignarycalcular(66,';')
    asignarycalcular(67,'<')
    asignarycalcular(68,'>')
    asignarycalcular(69,"'")
    asignarycalcular(70,'¿')
    asignarycalcular(71,'?')
    asignarycalcular(72,'|')
    asignarycalcular(73,'°')
    asignarycalcular(74,'¬')
    asignarycalcular(75,'!')
    asignarycalcular(76,'¡')
    asignarycalcular(77,'}')
    asignarycalcular(78,'{')
    asignarycalcular(79,'[')
    asignarycalcular(80,']')
    asignarycalcular(81,'"')
    asignarycalcular(82,'#')
    asignarycalcular(83,'$')
    asignarycalcular(84,'%')
    asignarycalcular(85,'&')
    asignarycalcular(86,'(')
    asignarycalcular(87,')')
    asignarycalcular(88,'@')
    #ordenando la matriz desde el mas usado al menor
    matriz=sorted(matriz, key=itemgetter(1),reverse=True)
    #creando el archivo
    encabezado='Caracter    Repeticion'
    np.savetxt('temp.txt',matriz, delimiter="               ",header=encabezado, fmt='%s')
