### Key Features:

1. **Telethon Authorization**:
   - Uses official Telegram API with session persistence
   - Automatically creates `session_name.session` file

2. **Image Handling**:
   - Filters only photo messages
   - Generates filenames using message date + ID (e.g., `20230814_153045_12345.jpg`)
   - Skips existing files

3. **Progress Tracking**:
   - Uses `tqdm` for progress bars
   - Shows download count statistics

4. **Error Handling**:
   - Comprehensive error logging to `error.log`
   - Skips failed downloads gracefully
   - Handles invalid channel names

5. **Command Line Arguments**:
   ```bash
   python telegram_image_downloader.py \
     --api-id YOUR_API_ID \
     --api-hash YOUR_API_HASH \
     --channel "t.me/channel_name" \
     --output "./custom_folder/" \
     --limit 500
   ```

### Setup Instructions:

1. **Install requirements**:
   ```bash
   pip install telethon tqdm
   ```

2. **Get API Credentials**:
   - Visit [my.telegram.org](https://my.telegram.org/)
   - Create application to get `api_id` and `api_hash`

3. **Run the script**:
   ```bash
   python telegram_image_downloader.py \
     --api-id 123456 \
     --api-hash a1b2c3d4e5f6g7h8i9j0 \
     --channel "t.me/interesting_pics" \
     --limit 1000
   ```

### Notes:

1. The first run will prompt for your phone number and login code
2. Session data is saved in `session_name.session` for future use
3. Images are saved with date-formatted names (YYYYMMDD_HHMMSS_MSGD.jpg)
4. Public channel requirement: Script won't work with private channels
5. For channels with >10k messages, use `--limit` parameter

### Output Structure:
```
downloads/
├── 20230814_120045_1234.jpg
├── 20230814_121530_1235.jpg
└── ...
error.log
```

