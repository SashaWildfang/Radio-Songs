# Radio Songs

The song library for the [Radio](https://github.com/SashaWildfang/Radio) plugin: note block songs (`.nbs`), one folder per genre.

**Built by Sasha Wildfang for Fractal Network.**

Servers running Radio stay in sync with this repository on every startup (or `/radio download`):

- songs added or changed here are downloaded
- songs removed here are removed from servers
- songs an admin added to a server by hand are never touched

## Adding or removing songs

1. Put `.nbs` files in a genre folder, e.g. `Electronic/`. A new folder becomes a new genre in the menu.
2. Name each file `Artist - Title.nbs`. That's exactly what players see.
3. Keep songs between **1m 30s and 4m 30s** (servers can change the limits in `config.yml`), and use vanilla note block instruments. Songs built mostly on custom instruments are skipped.
4. Rebuild the index, then commit and push:

```bash
python update_index.py
```

Servers pick up the changes on their next restart or `/radio download`.

## Credits

Songs from [Note Block World](https://noteblock.world) are credited in [`CREDITS.md`](CREDITS.md) and shared under their CC BY-SA 4.0 license.
