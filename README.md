# Profitable App Profiles for the App Store and Google Play Markets
  Esse projeto é um refactoring do projeto "Guided Project: Profitable App Profiles for the App Store and Google Play Markets"(https://github.com/dataquestio/solutions/blob/master/Mission350Solutions.ipynb)
  da plataforma [dataquest](https://app.dataquest.io/). O obejtivo desse refactoring é aplicar o paradigma de programação orientada a objetos. Vale salientar que esse refactoring não é uma generalização, ele resolve apenas o problema prosposto inicialmente aplicando os conceitos de POO.
  
  # Como usar
  
  ```python
   from Apps import Apps
   ```
   
   # Métodos Disponíveis
   - init(dataset): Construtor da classe Apps, recebe como parâmetro o nome do dataset
   - explore_data(start, end, rows_and_columns=True): retorna as linhas do dataset no intervalo especificado pelos pârametros "start" e "end". Quando row_and_columns = True, o número de linha e colunas do dataset é exibido
   - delete_row(index): deleta a linha no índice espeficado
   - remove_duplicate(show_numbers_duplicate_removed=True): remove aplicativos duplicados no dataset, quando o parâmetro padrão é "True" o número de aplicativos removidos é exibido
   - clean_english(index): remove aplicativos que não estão em inglês do dataset
   - remove_free_apps(index): remove aplicativos "free" do dataset
   - freq_table(index): Gera uma tabela de frequência
   - display_table(index): Exibe a tabela de frequência

 # Exemplo de uso:
  Utilizando a solução inicial como base para demonstração de uso da biblioteca: 
