<h1>Важное примечание</h1>

К сожалению, без предустановленного пакета **graphviz** невозможно запустить программу. 

Установка модуля **graphviz** из репозитория **PYPI** недостаточное условие для запуска программы. 

Необходим скомпилированный бинарный файл библиотеки.

<h2> Windows </h2>

Для запуска на **Windows** 
необходимо скачать EXE-файл **graphviz** с [официального сайта](https://graphviz.org/download/#windows).

Или можно установить с помощью менеджера пакета **winget** (обычно предустановлена вместе с Windows):
```powershell
winget install graphviz
```
При необходимости **перезагрузите** компьютер.

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
