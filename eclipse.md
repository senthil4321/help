# Usefule Eclipse shortcut
## TODO
1. How to run one testcase in eclipse junit?
---
## Eclipse shortcut
### Maximise eclipse view
```
ctrl+M
```
### Static import eclipse java
```
control shift m
```
### Eclipse goto Implentation
#### Custom shortcut
```
ALt + x - to open implementation
Alt + y - Open method definition like F3
```
### Open Interface implementation view
```
ctrl + t
```
### goto error
```
ctrl + . next error
ctrl + , previous error
ctrl + 1 solution suggesion
ctrl + f7
```
---
## How to generate test class and test method from eclipse wizard

New&nbsp;>&nbsp;JUnit Test Case&nbsp;>&nbsp;Class under test&nbsp; > &nbsp; Available methods

## edit shortcut
```
alt+UP/DOWN move line
alt+ctrl+DOWN. Copy lines.
shift+↵ Insert line below current line.
alt+ctrl+UP. Duplicate lines.
ctrl+DEL. Delete next word.
shift+ctrl+DEL. Delete to end of line.
shift+ctrl+↵ Insert line above current line.
shift+ctrl+X. To upper case.
```
## quick access commands
```
ctrl+ 3
```
## How to bind Ctrl + Tab in eclipse for navigating between editor windows?
> Bind key and unbind old keys.
1. https://stackoverflow.com/questions/2332330/eclipse-hotkey-how-to-switch-between-tabs
--- 
## Eclipse plugin

### Code Quality and Static Code Analysis
#### code style and formatting
* https://marketplace.eclipse.org/content/checkstyle-plug

#### fix quality issues as you write code
* https://marketplace.eclipse.org/content/sonarlint
* https://marketplace.eclipse.org/content/quick-bookmarks-plugin

#### static code analyser - detects possible bugs
* https://marketplace.eclipse.org/content/spotbugs-eclipse-plugin

#### Markdown plugin
* https://marketplace.eclipse.org/content/markdown-text-editor

#### TODO PMD plugin 



#### Other TODO
https://blog.codota.com/14-free-plugins-for-eclipse-ide/

#### Python IDE support
* https://marketplace.eclipse.org/content/pydev-python-ide-eclipse

#### Jansi plugin This plugin enables color in log output used with log4j2
  > This plugin gives an option in the console window to enable/disable ansi\
  > Use below option in log4j to enable ansi
  ```xml
  	<Console name="ConsoleMsgOnly" target="SYSTEM_OUT">
			<PatternLayout disableAnsi="false">
				<Pattern>%highlight{%msg%n}
				</Pattern>
			</PatternLayout>
		</Console>
  ```
  
#### JAutodoc	
   > Enables automatic java documentation generation
   Shortcut to auto generate documentation
   ```
   ctrl + alt + j
   ```
#### Terminal plugin
#### Copypath
#### Jenkins file viewer
#### anyedit
* https://marketplace.eclipse.org/content/anyedit-tools
---
## Productivity
### Eclipse Line Copy without select
#### What is it?
1. Press Ctrl-C to copy or Ctrl-X to cut the whole line in an editor if you select nothing. (It works as usual if you select some text.)
2. Put the caret on any line on any position.
3. Press Ctrl-V to paste the line above. (You will not lose the caret position.)
#### Installation
Download into your dropins folder and restart Eclipse.
#### Ref
 * https://github.com/fabioz/copycutcurrentline 
 * https://code.google.com/archive/p/copycutcurrentline/
 * https://github.com/fabioz/copycutcurrentline/blob/master/updatesite/plugins/copycutcurrentline_1.0.1.201505020939.jar
---
## Check Style, Code formatter, Content assistant, Template, Type filter
### Check Style
* http://google.github.io/styleguide/javaguide.html
* google_checks.xml
* https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml

```
Then enable the formatter for your workspace: Windows > Preferences > Java > Code Style > Formatter. Select formatter: "eclipse-cs [project name]".
```
### Code Formatter
* https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml
* https://stackoverflow.com/questions/984778/how-to-generate-an-eclipse-formatter-configuration-from-a-checkstyle-configurati

### Content assistant and Template
> In eclipse it is possible to expand code with shortcut.eg. typing `syso` and pressing `ctrl + space` expands to `Sysout.out.println();`
> Similarly it is possible to create custom code expansion. It can be done with code `Template` section of eclipse preference. 
Also refer Idea

#### `info` expansion for apache log4j2
```java 
logger.info(${word_selection}${});${cursor}
```
---

## How to uninstall or disable plugin in eclipse?
1. https://wiki.eclipse.org/FAQ_How_do_I_remove_a_plug-in%3F
## Ref.

 1. https://stackoverflow.com/questions/25980588/eclipse-hotkey-to-toggle-tab-maximize-minimize/25980723 
 1. http://www.eclipseonetips.com/2010/02/15/the-fastest-ways-to-navigate-views-in-eclipse-using-the-keyboard/
 1. https://marketplace.eclipse.org/content/quick-bookmarks-plugin
 1. https://stackoverflow.com/questions/5354068/shortcut-how-to-get-eclipse-to-go-to-the-only-implementation-of-an-interfaces


## Eclipse maven source code download
It is possivle to download maven artifact source code automatically using the maven option.
Use the below option to download the source

```xml
 <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-eclipse-plugin</artifactId>
                <configuration>
                    <downloadSources>true</downloadSources>
                    <downloadJavadocs>true</downloadJavadocs>
                </configuration>
            </plugin>
        </plugins>
    </build>
```
* https://stackoverflow.com/questions/2059431/get-source-jars-from-maven-repository
* https://stackoverflow.com/questions/310720/get-source-jar-files-attached-to-eclipse-for-maven-managed-dependencies
---

### Eclipse download plugin source and attach

So far there is no easy wasy to download and attach eclipse plugin source automatically.
Easy working solution is to download the source manually and attaching it. (CTRL + Click or F3) and attach source folder.
## Manage import ❤️
* http://www.eclipseonetips.com/2014/01/14/essential-tools-to-manage-import-statements-in-eclipse/
---
### Not Useful
#### ~~~ AI based code completion - does not work ~~~
 ~~~ https://marketplace.eclipse.org/content/codota ~~~
#### ~~~Markdown plugin~~~
* Not good
 ~~https://marketplace.eclipse.org/content/markdown-text-editor~~
 ~~https://marketplace.eclipse.org/content/liclipsetext~~
 ~~FluentMarkEditor~~
