import os
import yt_dlp

def download_video(url, output_path='downloads'):
    """
    Laster ned video i høyere kvalitet (opp til 1080p) for bedre ansiktsdeteksjon.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        # ENDRING: Vi tillater nå opp til 1080p for skarpere ansikter
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio/best[height<=1080][ext=mp4]',
        'outtmpl': f'{output_path}/%(id)s.%(ext)s',
        'match_filter': yt_dlp.utils.match_filter_func("duration <= 600"),
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info)
            
            ydl.download([url])
            
            if os.path.exists(filename):
                return filename
            else:
                return None
                
    except Exception as e:
        # Fallback hvis 1080p feiler (f.eks. pga manglende ffmpeg), prøv enklere format
        print(f"Høy kvalitet feilet, prøver standard 720p... Feil: {e}")
        try:
            ydl_opts['format'] = 'best[height<=720]'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                return ydl.prepare_filename(info)
        except:
            return None

def delete_video(file_path):
    if file_path and os.path.exists(file_path):
        os.remove(file_path)