# Instagram Reel Boilerplate

The aim is to provide a simple way to showcase horizontal video on vertical forward platforms like instagram reels. The following python code, with the help of [Moviepy](https://github.com/Zulko/moviepy) and [ImageMagick](https://www.imagemagick.org/script/index.php), enables conversion of horizontal videos to vertical videos with title text and sub text with individually given timestamps.

## Prerequisites

To deploy this project you will need:
- Python 3 (preferably 3.10 or higher)
- The [Moviepy](https://github.com/Zulko/moviepy) module
- [ImageMagick](https://www.imagemagick.org/script/index.php) Image Manipulation Software



1. Ensure Python is installed on your system and then run the following command to install Moviepy
    ```bash
    pip install moviepy
    ```

2. Install the ImageMagick tool ensuring that you note down the installation path

### For Windows Only
3. Go to your python installation Folder and point moviepy to Imagemagick
    1. Find your moviepy install location. The following is the default location
        ```
        %AppData%/Local/Programs/Python/Python311/Lib/site-packages/moviepy
        ```
    2. Open the `config_defaults.py`
    3. Comment out the `IMAGEMAGICK_BINARY` line and specify your ImageMagick path as follows
        ```bash
        #IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
        IMAGEMAGICK_BINARY = "C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe
        ```

## Usage

Ensure that there is a `config.json` file present in the current directory. This json structure provides the config to give the tool the necessary information for the conversion:

```json
{
    "videoPath" : <Video Path for the horizontal video>,
    "titleText" : <Title text with support for new lines (\n)>,
    "outputFilename": <Output Filename>,
    "captions" : [ <Match caption with the video clip. Any number acceptable>
        {"caption": Title text with support for new lines (\n)>, "time": <integer value of when to show text in seconds>},
        {"caption": Title text with support for new lines (\n)>, "time": <integer value of when to show text in seconds>},
        {"caption": Title text with support for new lines (\n)>, "time": <integer value of when to show text in seconds>}
    ]
}
```

> To see an example look at the `config.json` present in the repository

To run the tool run the following command:
```bash
python main.py
```

## Example
> TODO 

## Caveats
For this to work you need to provide **1** video which is a combination of the videos that you want to showcase. This can be easily and freely done via many different video editing programs. The ones I recommend are:

Windows:
- [Microsoft ClipChamp](https://clipchamp.com/en/windows-video-editor/)

MacOS:
- [iMovie](https://apps.apple.com/us/app/imovie/id408981434?mt=12)

Multi-Platform:
- [Openshot](https://www.openshot.org/download/)

## TODO
- Add more template styles to the boilerplate
- Create a docker container so setting up can be trivial on any system