.. test documentation master file, created by
   sphinx-quickstart on Wed Jul 23 17:54:55 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

md文档语法
==================
方法1：使用纯文本字符（最简单）
进度: [=====>     ] 50%

.. code-block:: text

    0% [                    ]
    25% [=====>             ]
    50% [===========>       ]
    75% [===============>   ]
    100%[===================]


方法2：使用表格模拟进度条（更精确）

.. list-table:: 任务进度
   :widths: 10 90
   :header-rows: 0
   
   * - 25%
     - | [█████.................]
   * - 50%
     - | [██████████............]
   * - 75%
     - | [███████████████.......]
   * - 100%
     - | [██████████████████████]



方法3：嵌入Python动态生成（需Sphinx支持）
.. raw:: html

   <div id="progress-bar" style="width:100%; background:#ddd; border-radius:5px">
     <div id="progress-fill" style="width:0%; height:20px; background:#4CAF50; border-radius:5px"></div>
   </div>
   <script type="text/javascript">
     // 动态更新进度条
     let progress = 0;
     const interval = setInterval(() => {
       progress += 5;
       document.getElementById('progress-fill').style.width = `${progress}%`;
       if(progress >= 100) clearInterval(interval);
     }, 200);
   </script>




方法4：使用Unicode块字符（最佳视觉效果）
处理中: | ████████████████████░░░░░ | 75%

.. code-block:: none

   0%   ░░░░░░░░░░░░░░░░░░░░
   25%  ████░░░░░░░░░░░░░░░░
   50%  ██████████░░░░░░░░░░
   100% ████████████████████




下载进度: :progress-bar:`██████████░░░░░░░░░░ 50%`

.. raw:: html

   <script>
       document.getElementById('show-message').addEventListener('click', function() {
           var messageContainer = document.getElementById('message-container');
           var message = "这是要显示的消息。";
           messageContainer.innerHTML = message;
       });
   </script>