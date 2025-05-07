<h1>Важное примечание</h1>

К сожалению, без предустановленного пакета **graphviz** невозможно гарантировать корректность работы программы.

Необходим скомпилированный бинарный файл библиотеки.

<h2> Windows </h2>

Для запуска на **Windows** 
необходимо скачать EXE-файл **graphviz** с [официального сайта](https://graphviz.org/download/#windows).

Или можно установить с помощью менеджера пакета **winget** (обычно предустановлен вместе с Windows):
```powershell
winget install -i graphviz
```
При необходимости **перезагрузите** компьютер.
Проверьте, что исполняемый файл Graphviz добавлен в переменную PATH.

Был добавлен ```prepare.ps1```, просто запустите его.
```powershell
./prepare.ps1
```

<h2> Linux </h2>

Для **Linux** необходимо также установить доп. пакет. 

Команды для установки находятся на [официальном сайте](https://graphviz.org/download/#linux).
Команда для установки на **Debian/Ubuntu**
```shell
sudo apt install graphviz
```
Команда для установки на **Fedora/Rocky Linux/Redhat Enterprise Linux/CentOS**
```shell
sudo dnf install graphviz
```
Скомпилированные сборки под **Linux** и **Windows** можно также найти на [Gitlab](https://gitlab.com/graphviz/graphviz/-/releases).

Был добавлен ```compare.sh```, просто запустите его.
```shell
./prepare.sh
```
Для Linux всё равно необходимо установить зависимость Graphviz с помощью команд выше.
