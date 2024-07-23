# 🔗 Comfyui : Bjornulf_custom_nodes v0.2 🔗

# Dependencies

- `pip install ollama` (you can also install ollama if you want :  https://ollama.com/download) - You don't need to really install it if you don't want to use my ollama node. (BUT you need to run `pip install ollama`)

# 📝 Changelog

## v0.2
- **Ollama**: Improve ollama node with system prompt + model selection.

# 📝 Nodes descriptions

## 1/2 - 👁 + ✒ Show/Write Text 
![Show Text](screenshots/write+show_text.png)

**Description:**  
Two simple nodes to write and show text.
Write node is a textarea where you can write your text.  
The show text node will only display the text. (That's why I made it a different color : green, uneditable, display only.)

## 3 - 🔗 Combine Texts
![Combine Texts](screenshots/combine_texts.png)

**Description:**  
Combine multiple text inputs into a single output. (can have separation with : comma, space, new line.)

## 4 - 🎲 Random Text
![Random Text](screenshots/random_text.png)

**Description:**  
Generate and display random text from a predefined list. Great for creating random prompts.

## 5 - ♻ Loop
![Loop](screenshots/loop.png)

**Description:**  
General-purpose loop node.

## 6 - ♻ Loop Texts
![Loop Texts](screenshots/loop_texts.png)

**Description:**  
Cycle through a list of text inputs. Great for creating dynamic text-based presentations.

## 7 - ♻ Loop Integer
![Loop Integer](screenshots/loop_integer.png)
![Loop Int + Show Text](screenshots/loop_int+show_text.png)

**Description:**  
Iterate through a range of integer values, good for `steps` in ksampler, etc...

❗ Don't forget that you can convert ksampler widgets to input by right-clicking the ksampler node :
![Widget to Input](screenshots/widget-to-input.png)

## 8 - ♻ Loop Float
![Loop Float](screenshots/loop_float.png)
![Loop Float + Show Text](screenshots/loop_float+show_text.png)

**Description:**  
Loop through a range of floating-point numbers, good for `cfg`, `denoise`, etc...

## 10 - ♻ Loop All Samplers
![Loop All Samplers](screenshots/loop_all_samplers.png)

**Description:**  
Iterate over all available samplers to apply them sequentially. Ideal for testing.

## 11 - ♻ Loop All Schedulers
![Loop All Schedulers](screenshots/loop_all_schedulers.png)

**Description:**  
Iterate over all available schedulers to apply them sequentially. Ideal for testing.

## 12 - ♻ Loop Combos
![Loop Combos](screenshots/loop_combos.png)

**Description:**  
Generate a loop from a list of my own custom combinations (scheduler+sampler), or select one combo manually.  
Good for testing.

## 13/14 - 📏 + 🖼 Resize and Save Exact name ⚠️💣
![Resize and Save Exact](screenshots/resize_save_exact.png)

**Description:**  
Resize an image to exact dimensions. The other node will save the image to the exact path.  
⚠️💣 Warning : The image will be overwritten if it already exists.

## 15 - 💾 Save Text
![Save Text](screenshots/save_text.png)

**Description:**  
Save the given text input to a file. Useful for logging and storing text data.

## 16 - 🖼 Save image for API (❗For my custom [lobe-chat](https://github.com/justUmen/lobe-chat)❗)
![Save API](screenshots/save_api.png)

**Description:**  
It will save the image with the name of `api_next_image.txt`, which will be incremented each time you run the node.  
The name will start at `api_00001.png`, then `api_00002.png`, etc...  
❓ I made that for my custom lobe-chat to send+receive images from Comfyui API : [lobe-chat](https://github.com/justUmen/lobe-chat)

## 17 - 🖼 Save image as `tmp_api.png` Temporary API ⚠️💣
![Save Temporary API](screenshots/save_tmp_api.png)

**Description:**  
Save image for short-term use : ./output/tmp_api.png ⚠️💣

## 18 - 🦙 Ollama
![Show Text](screenshots/ollama.png)

**Description:**  
Will generate detailed text based of what you give it.  
I recommend using `mistral-nemo` if you can run it, but it's up to you. (Might have to tweak the system prompt a bit)  
⚠️ Warning : Having an ollama node that will run for each generation might be a bit heavy on your VRAM. Think about if you really need it or not.

**Description:**  
Straight forward node to write and show text.

## 18 - 📹 Video Ping Pong
![Video Ping Pong](screenshots/video_pingpong.png)

**Description:**  
Create a ping-pong effect from a list of images (from a video) by reversing the playback direction when reaching the last frame. Good for an "infinity loop" effect.

## 19 - 📹 Images to Video
![Images to Video](screenshots/imgs2video.png)

**Description:**  
Combine a sequence of images into a video file.  
❓ I made this node because it supports transparency with webm format. (Good for rembg)