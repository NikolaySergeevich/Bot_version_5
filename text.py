def get_list_whis_title_on_english():
    text = ['extrovert', 'introvert', 'ability_to_work_monotonously', 'mentoring', 'analytical_skills', 'empathy',
        'curiosity', 'oratory', 'organizational_skills', 'critical_thinking', 'multitasking', 'creativity',
        'stress_resistance', 'time_control', 'working_with_a_large_amount_of_information']
    return text
def get_list_whis_title_on_russian():
    text = ['Экстраверт', 'Интроверт', 'Способность\nк монотонной работе', 'Наставничество', 'Аналитические навыки', 'Эмпатия', 'Любопытство', 
         'Ораторское\nискусство', 'Организаторские\nспособности', 'Критическое мышление', 'Многозадачность', 'Креативность', 'Стрессоустойчивость',
        'Контроль времени', 'Работа с большим\nобъёмом информации']
    return text
def get_way_of_img(user_id):
    return 'D:/Учёба в GB/Дипломный проект/Работа/Бот 5/result_img/' + str(user_id) +'_result_test.png'
def get_way_of_img_compare(user_id, specific):
    return 'D:/Учёба в GB/Дипломный проект/Работа/Бот 5/result_img/' + str(user_id) + '_compare_'+ specific +'_result_test.png'
def get_way_of_finish_img(user_id):
    return 'D:/Учёба в GB/Дипломный проект/Работа/Бот 5/result_img/' + str(user_id) +'_finish.png'

name_specific = ["developer", "tester", "analist", "project", "prodact"]
name_compsre_specific = ["sum_bals_compare_with_developer", "sum_bals_compare_with_tester", "sum_bals_compare_with_analist", "sum_bals_compare_with_project", "sum_bals_compare_with_prodact"]
name_specific_rus = ["Программист", "Тестировщик", "Аналитик", "Проджект-\nменеджер", "Продакт-\nменеджер", " "]
defolt_resulr_passing_grade = {"Программист":"20", "Тестировщик":"15", "Аналитик":"20", "Проджект-\nменеджер":"25", "Продакт-\nменеджер":"25"}

color_for_analist = ["#f1dcc9","#ffb793","#9f4636","#6c2d2c","#42313a"] 
color_for_tester = ["#e2c499","#e8a735","#ff7606","#c8000a","#8c0004"] 
color_for_developer = ["#755248","#f79b77","#086488","#4b4345","#fcdbcd"] 
color_for_prodact = ["#323030","#cdbea7","#ba5536","#882426","#c29545"] 
color_for_project = ["#444c5c","#ff734d","#ce5a57","#78a5a3","#e1b16a"] 
color_for_person = ["#505160","#6a71","#68829e","#aebd38","#598234"] 
color_for_finish_img = ["#fb7819","#fc0fc0","#f5ee00","#28e4f3","#9d22f2", "#ffffff"]

hello_text = 'Привет, {name}, я бот и я предлагаю тебе пройти тест \n<b>"Колесо компетенций"</b> от <b>GeekBrains.</b>\n\
            После прохождения теста ты сможешь взглянуть на свой портрет, а так же сравнить его с портретами для \nIT-специальностей, таких как\n\
            👉 Программист\n\
            👉 Тестировщик\n\
            👉 Аналитик\n\
            👉 Проджект-менеджер\n\
            👉 Продакт-менеджер\n\
            \n\
            Для каждой из IT-специальностей уже составлены портреты и вы можете посмотреть на них.\n\
            Или начать проходить тест.\n\
            Для этого выберете в меню бота подходящую команду.'

text_for_question_1 = '🔴<b>Приступим к прохождению теста!</b>🔴\n\
            <b>Экстроверт</b> - человек, который любит общаться с людьми и быть в центре внимания. Получает энергию в социуме.\n\
            <b>0</b> - я не люблю быть в центре внимания\n\
            <b>1</b> - я готов общаться с людьми, если это необходимо\n\
            <b>2</b> - я умею общаться и часто делаю это\n\
            <b>3</b> - мне интересно общаться с людьми\n\
            <b>4</b> - мне нравится знакомиться и общаться\n\
            <b>5</b> - я легко иду на контакт с другими людьми'
text_for_question_2 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Интроверт</b> - человек, который сфокусирован на своём внутреннем мире. Получает энергию вне социума.\n\
            <b>0</b> - мне нужна тишина, чтобы сосредоточиться\n\
            <b>1</b> - Я предпочитаю сидеть дома\n\
            <b>2</b> - мне проще написать человеку, чем поговорить лично\n\
            <b>3</b> - я избегаю диалогов, если они не связаны с тем, что мне интересно\n\
            <b>4</b> - мне проще общаться с компьютером, чем с людьми\n\
            <b>5</b> - я не люблю общаться с людьми'
text_for_question_3 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Способность к монотонной работе</b> - умение сосредоточиться на выполнении рутинных однообразных задач.\n\
            <b>0</b> - не могу долго работать над однообразными задачами\n\
            <b>1</b> - я могу делать монотонную работу, но утаю от нее\n\
            <b>2</b> - мне не сложно делать одну и ту же работу постоянно\n\
            <b>3</b> - я делаю рутинные задачи на автомате\n\
            <b>4</b> - мне интересно даже там, где другим работа кажется скучной\n\
            <b>5</b> - я люблю делать хорошо знакомую мне работу'
text_for_question_4 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Наставничество</b> - способность и желание передавать свои навыки другим людям.\n\
            <b>0</b> - мне проще самому сделать, чем объяснить кому-то\n\
            <b>1</b> - если человек готов учиться, то я помогу ему\n\
            <b>2</b> - могу объяснить человеку все что угодно, если это необходимо\n\
            <b>3</b> - я охотно рассказываю о своих знаниях и умениях\n\
            <b>4</b> - мне нравиться делиться опытом\n\
            <b>5</b> - люблю учить людей тому, что умею'
text_for_question_5 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Аналитические навыки</b> - способность раскладывать информацию "по полочкам" и находить в ней закономерности.\n\
            <b>0</b> - я не люблю копаться в цифрах и отчетах\n\
            <b>1</b> - я готов анализировать информацию, если это необходимо\n\
            <b>2</b> - я умею структурировать и анализировать данные\n\
            <b>3</b> - мне инетерчно анализировать информацию\n\
            <b>4</b> - мне нравиться сранивать информациб\n\
            <b>5</b> - я люблю находить закономерности в большом массиве данных'
text_for_question_6 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Эмпатия</b> - способность понимать чувства других людей и сопереживать им.\n\
            <b>0</b> - мне не важно, что чувствуют дрйгие люди\n\
            <b>1</b> - я понимаю чувства дрцгих, когда это необходимо\n\
            <b>2</b> - я умею чувствовать других людей\n\
            <b>3</b> - мне интересно узнавать, что чувствуют другие люди\n\
            <b>4</b> - мне нравится ощущать, что чувствуют окружающие меня люди\n\
            <b>5</b> - я люблю понимать, что чувствуют окружающие меня люди'
text_for_question_7 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Любопытство</b> - способность и желание интересоваться чем-то новым.\n\
            <b>0</b> - я не интерексуюсь ием, что выходит за рамки моей профессии\n\
            <b>1</b> - я готов интересоваться новым, если это необходимо\n\
            <b>2</b> - я часто открываю для себя новую информацию\n\
            <b>3</b> - мне интересно искать новую информацию\n\
            <b>4</b> - мне нравиться исследовать новое\n\
            <b>5</b> - я люблю изучать информацию, даже не связанную с моей специальностью'
text_for_question_8 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Ораторское искусство</b> - умение логично и красиво излогать свои мысли.\n\
            <b>0</b> - я не люблю говорить на публике\n\
            <b>1</b> - я готов высказываться, если это необходимо\n\
            <b>2</b> - я умею выступать публично и делать это\n\
            <b>3</b> - мне интересно выступать перед людьми\n\
            <b>4</b> - мне нравитьсяговорить на аудиторию\n\
            <b>5</b> - я могу убдеить кого угодно в чем угодно'
text_for_question_9 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Организаторские способности</b> - умение выстраивать работу других людей для решения определенной задачи.\n\
            <b>0</b> - я предпочитаю делать все самомстоятельно\n\
            <b>1</b> - я готов организовать других, если это необходимо\n\
            <b>2</b> - я умею организовать людей\n\
            <b>3</b> - мне инетесно выстраивать работу других\n\
            <b>4</b> - мне нравиться руководить людьми\n\
            <b>5</b> - я люблю организовывать людей вокруг себя'
text_for_question_10 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Критическое мышление</b> - способность анализировать информацию, ставить ее под сомнение и давать фактам собственную оценку.\n\
            <b>0</b> - я не люблю перепроверять факты\n\
            <b>1</b> - я готов проверять информацию, ечли это необходимо\n\
            <b>2</b> - я умею проверять информацию и часто делаю это\n\
            <b>3</b> - мне интересно анализировать информацию\n\
            <b>4</b> - мне нравиться самостоятельно оценивать факты\n\
            <b>5</b> - я люблю ставить все под сомнение'
text_for_question_11 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Многозадачность</b> - способность эффектно работать, постоянно переключаясь между разными задачами.\n\
            <b>0</b> - мне проще сконцентрироваться на одной задаче\n\
            <b>1</b> - я готов делать несколько задач, если это необходимо\n\
            <b>2</b> - я умею переключаться между задачами\n\
            <b>3</b> - мне интересно работать над несколькими проектами\n\
            <b>4</b> - мне нравиться рабоать над несколькими задачами сразу\n\
            <b>5</b> - я люблю переключаться с одной задачи на другую'
text_for_question_12 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Креативность</b> - способность творчески подходить к задачам и придумывать новые пути для их решения.\n\
            <b>0</b> - я люблю делать все по готовому шаблону\n\
            <b>1</b> - я готов придумывать новое, если это необходимо\n\
            <b>2</b> - я умею придумывать новые решения задач и делаю это\n\
            <b>3</b> - мне интересно решать задачи по-своему\n\
            <b>4</b> - мне нравиться придумывать нестандартный подход к решению задач\n\
            <b>5</b> - я люблю придумывать что-то новое в своей работе'
text_for_question_13 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Стрессоустойчивость</b> - способность адаптироваться к стрессам, переносить их без негативных последствий.\n\
            <b>0</b> - я не могу работать в режиме аврала\n\
            <b>1</b> - я готов к авралам, если это необходимо\n\
            <b>2</b> - я умею работать в авральном режиме\n\
            <b>3</b> - мне становиться интересно, когда "горят сроки"\n\
            <b>4</b> - мне нравиться напряженная атмосфера на работе\n\
            <b>5</b> - стресс стимулирует меня работать лучше'
text_for_question_14 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Контроль времени</b> - способность соблюдать дедлайны и контролировать время выполнения задач.\n\
            <b>0</b> - я постоянно опаздываю и пропускаю дедлайны\n\
            <b>1</b> - я готов делать все вевремя, если это необходимо\n\
            <b>2</b> - я умею соблбдать дедлайны и делаю это\n\
            <b>3</b> - в моих интересах делать все заранее\n\
            <b>4</b> - мне нравиться, когда все сделано заранее\n\
            <b>5</b> - я всегда прихожу заранее и делаю все вовремя'
text_for_question_15 = '🔴<b>Ваш ответ принят. Идём дальше!</b>🔴\n\
            <b>Работа с большим объемом информации</b> - способность ориентироваться и чувствовать себя комфортно в большом потоке данных.\n\
            <b>0</b> - я тераюсь, когда информации слишком много\n\
            <b>1</b> - я готов обрабатывать объемные данные, если это необходимо\n\
            <b>2</b> - я умею рабоать с большими данными и делаю это\n\
            <b>3</b> - мне интересно обрабатывать объемные массивы информации\n\
            <b>4</b> - мне нравиться работать с большим объемом информации\n\
            <b>5</b> - я люблю структурировать информацию ане зависимости от ее объема'
