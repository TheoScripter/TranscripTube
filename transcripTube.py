from youtube_transcript_api import YouTubeTranscriptApi


def transcribe_youtube_video(url, language, output_filename):
    try:
        video_id = url.split("v=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=language)

        text = " ".join([entry['text'] for entry in transcript])

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"Transcription saved to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    url = input("Enter the YouTube video URL: ")
    language = input("Enter the text language of the YouTube video (fr, en): "),
    output_filename = input("Enter the output file name (output.txt): ")

    transcribe_youtube_video(url, language, output_filename)


if __name__ == "__main__":
    main()
