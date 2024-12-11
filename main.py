from collections import deque

def fifo(array_list):
    
    process_dict = {}
    for i in range (len(array_list)):
        process_dict[i] = {'arrival': int(array_list[i][0]), 'exec': int(array_list[i][1]), 'wait': 0, 'time_left': int(array_list[i][1])}
    
    time_return = 0
    time_wait = 0
    turnaround = 0
    clock = 0
    quantity_process = len(process_dict.keys())
    in_progress = []
    in_wait = []

    while process_dict:
        for process in process_dict:
            if process_dict[process]['arrival'] == clock:
                if not in_progress:
                    in_progress.append(process)
                else:
                    in_wait.append(process)
        
        if in_progress:
            current_process = in_progress[0]
            process_dict[current_process]['time_left'] -= 1
        

        if in_wait:
            for element in in_wait:
                process_dict[element]['wait'] += 1

        if in_progress and process_dict[current_process]['time_left'] == 0:
            time_return += process_dict[current_process]['wait']
            time_wait += process_dict[current_process]['wait']
            turnaround += (process_dict[current_process]['exec'] + process_dict[current_process]['wait'])
            in_progress.pop()
            del process_dict[current_process]
            if in_wait:
                in_progress.append(in_wait[0])
                in_wait.pop(0)
        
        clock += 1
        
    array_result = [time_return / quantity_process, time_wait / quantity_process, turnaround / quantity_process]
    array_result = [f"{value:.3f}" for value in array_result]
    return array_result

def sjf(array_list):

    process_dict = {}
    for i in range (len(array_list)):
        process_dict[i] = {'arrival': int(array_list[i][0]), 'exec': int(array_list[i][1]), 'wait': 0, 'time_left': int(array_list[i][1])}
    
    time_return = 0
    time_wait = 0
    turnaround = 0
    clock = 0
    quantity_process = len(process_dict.keys())
    in_progress = []
    in_wait = []

    while process_dict:
        for process in process_dict:
            if process_dict[process]['arrival'] == clock:
                in_wait.append(process)
        
        if not in_progress and in_wait:
            menor = 100000
            p_choose = 0
            for p_waiting in in_wait:
                if process_dict[p_waiting]['exec'] < menor:
                    menor = process_dict[p_waiting]['exec']
                    p_choose = p_waiting
            in_progress.append(p_choose)
            in_wait.remove(p_choose)


        if in_progress:
            current_process = in_progress[0]
            process_dict[current_process]['time_left'] -= 1
        

        if in_wait:
            for element in in_wait:
                process_dict[element]['wait'] += 1

        if in_progress and process_dict[current_process]['time_left'] == 0:
            time_return += process_dict[current_process]['wait']
            time_wait += process_dict[current_process]['wait']
            turnaround += (process_dict[current_process]['exec'] + process_dict[current_process]['wait'])
            in_progress.pop()
            del process_dict[current_process]
                
        clock += 1
        
    array_result = [time_return / quantity_process, time_wait / quantity_process, turnaround / quantity_process]
    array_result = [f"{value:.3f}" for value in array_result]
    return array_result

def srt(array_list):

    process_dict = {}
    for i in range (len(array_list)):
        process_dict[i] = {'arrival': int(array_list[i][0]), 'exec': int(array_list[i][1]), 'wait': 0, 'time_left': int(array_list[i][1]), 'time_return': 0}
    
    time_return = 0
    time_wait = 0
    turnaround = 0
    clock = 0
    quantity_process = len(process_dict.keys())
    in_progress = []
    in_wait = []

    while process_dict:
        for process in process_dict:
            if process_dict[process]['arrival'] == clock:
                if in_progress and process_dict[in_progress[0]]['time_left'] > process_dict[process]['time_left']:
                    in_wait.append(in_progress[0])
                    in_progress.pop()
                    in_progress.append(process)
                else:
                    in_wait.append(process)
        
        if not in_progress and in_wait:
            menor = 100000
            p_choose = 0
            for p_waiting in in_wait:
                if process_dict[p_waiting]['time_left'] < menor:
                    menor = process_dict[p_waiting]['time_left']
                    p_choose = p_waiting
            in_progress.append(p_choose)
            in_wait.remove(p_choose)
           
        if in_progress:
            current_process = in_progress[0]

            if process_dict[current_process]['time_left'] == process_dict[current_process]['exec']:
                process_dict[current_process]['time_return'] = process_dict[current_process]['wait']
            
            process_dict[current_process]['time_left'] -= 1
        

        if in_wait:
            for element in in_wait:
                process_dict[element]['wait'] += 1

        if in_progress and process_dict[current_process]['time_left'] == 0:
            time_return += process_dict[current_process]['time_return']
            time_wait += process_dict[current_process]['wait']
            turnaround += (process_dict[current_process]['exec'] + process_dict[current_process]['wait'])
            in_progress.pop()
            del process_dict[current_process]
                
        clock += 1
        
    array_result = [time_return / quantity_process, time_wait / quantity_process, turnaround / quantity_process]
    array_result = [f"{value:.3f}" for value in array_result]
    return array_result

def rr(array_list, quantum):
    
    process_dict = {}
    for i in range (len(array_list)):
        process_dict[i] = {'arrival': int(array_list[i][0]), 'exec': int(array_list[i][1]), 'wait': 0, 'time_left': int(array_list[i][1]), 'time_return': 0}
    
    time_return = 0
    time_wait = 0
    turnaround = 0
    clock = 0
    quantum = quantum
    quantum_temp = quantum
    quantity_process = len(process_dict.keys())
    fila = deque()

    while process_dict:

        for process in process_dict:
            if process_dict[process]['arrival'] == clock:
                fila.append(process)
        

        if fila:
            current_process = fila[0]
            if process_dict[current_process]['time_left'] == process_dict[current_process]['exec']:
                process_dict[current_process]['time_return'] = process_dict[current_process]['wait']
            
            if process_dict[current_process]['time_left'] != 0:
                process_dict[current_process]['time_left'] -= 1
                quantum_temp -= 1
                if len(fila) > 1:
                    temp = fila.popleft()
                    for process in fila:
                        process_dict[process]['wait'] += 1
                    fila.appendleft(temp)

            if process_dict[current_process]['time_left'] == 0:
                time_return += process_dict[current_process]['time_return']
                time_wait += process_dict[current_process]['wait']
                turnaround += (process_dict[current_process]['exec'] + process_dict[current_process]['wait'])
                del process_dict[fila.popleft()]
                process_exit = True
                if quantum_temp != 0:
                    quantum_temp = quantum
        
            
            if quantum_temp == 0:
                if fila and not process_exit:
                    last_process = fila.popleft()
                    fila.append(last_process)
                quantum_temp = quantum
        
        process_exit = False      
        clock += 1
        
    array_result = [time_return / quantity_process, time_wait / quantity_process, turnaround / quantity_process]
    array_result = [f"{value:.3f}" for value in array_result]
    print(array_result)
    return array_result

def scaling_dict(array_list):
    quantum = int(array_list[0][0])
    del array_list[0]
    fifo_result = fifo(array_list)
    sjf_result = sjf(array_list)
    srt_result = srt(array_list)
    rr_result = rr(array_list, quantum)
    array_all = []
    array_all.append(fifo_result)
    array_all.append(sjf_result)
    array_all.append(srt_result)
    array_all.append(rr_result)
    return array_all



def text_generator(read_file, write_file):
    with open(read_file, 'r') as read_file, open(write_file, 'w') as write_file:
        write_file.write('Nome: ' + username + '\n')
        write_file.write('Convertido de: ' + str(read_file.name).replace(caminho_arquivo, '') + '\n')
        write_file.write('Resultado: ' + '\n' + '\n')
        #Colocar instruções no array_list
        array_list = []
        for line in read_file:
            array_temp = []
            line = line.strip().replace(',', '').replace('(',' ').replace(')',' ')
            if line != '':
                for element in line.split():
                    array_temp.append(element)
                array_list.append(array_temp)
        
        #Colocar instruções no txt de resultado
        for line in scaling_dict(array_list):
            line = str(line).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace('.', ',')
            write_file.write(line + '\n')


#Mude a quantidade de arquivos
n_arquivos = 3
#Coloque o caminho exato do arquivo, ex: pc/documentos/testes/
caminho_arquivo = ""
for i in range(0, n_arquivos):
    username = 'Pedro Sanzio'
    if i + 1 < 10:
        read_file = f'{caminho_arquivo}TESTE-0{i+1}.txt'
    else:
        read_file = f'{caminho_arquivo}TESTE-{i+1}.txt'
    filename = read_file.replace('.txt','-RESULTADO')
    write_file = str(filename) + '.txt'
    text_generator(read_file, write_file)