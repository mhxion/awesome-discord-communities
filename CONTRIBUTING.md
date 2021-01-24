<!-- omit in toc -->
# Contribution Guidelines

By participating in this project you agree to follow the [contributor code of conduct](CODE_OF_CONDUCT.md). From here on, the word _server_ and _community_ will be used interchangeably and will mean the same thing.

- [Add Community](#add-community)
- [Format WebP](#format-webp)
- [Issues](#issues)
- [Review Policy](#review-policy)

## Add Community

To include a community to the list, fork this project and add your server under a section or subsection, or you can include a new section if need be,
then [create a pull request](https://github.com/sindresorhus/awesome/blob/main/contributing.md#adding-something-to-an-awesome-list).
Make sure your proposal meets these requirements below, if you've Python installed you can take advantage of this [script](./main.py).

✅ Each community follows this template

```html
<img align="left" height="94px" width="94px" alt="Server Icon" src="<static url of the image>"/>

[__Community Name__](url of invite link) [<img height="16px" width="16px" alt="Official Badge" src="images/badges/official.webp">](badges.md#official-identification-badge) [<img height="16px" width="16px" alt="Reddit Badge" src="images/badges/reddit.webp">](badges.md#reddit-badge) [<img height="16px" width="16px" alt="Homepage URL" src="images/badges/homepage.webp">](url of server homepage) [<img height="16px" width="16px" alt="Git Repository" src="images/badges/git.webp">](url of server git repository) \
Notable Channels: `#most-important-channel-1`, `#most-important-channel-2`, `#most-important-channel-3`, `#most-important-channel-4`, `#most-important-channel-5`, `#least-important-channel` \
Language: English, Deutsch, 日本語
```

![Render Screenshot](images/screenshots/screenshot_00.png)

✅ Community icon is optimized with [WebP](#format-webp), with 75% lossy quality, and at least `128x128` pixel in resolution with moderate PPI

✅ Community name does not contain any emoji (discouraged)

✅ Invite link is permanent, generated from Discord platform itself, not a third-party domain

✅ [Badges](badges.md) are properly placed and aligned

✅ `Notable Channels` contains the most important channels, no off-topic channels, and does not necessarily take up too much space

✅ `Language` only contains spoken languages that the community has to offer

✅ Moderation team is regularly active

✅ Community is active on a daily or semiweekly basis

✅ All public channels follow Discord [community guidelines](https://discord.com/guidelines)
and [ToS](https://discord.com/terms)

## Format WebP

Awesome Discord Communities list [hosts](images/server_icons) the server icon images in its own repository. This allows reduced time to cache and faster rendition by the browser. Discord hosts the icon files as `png` which can take quite a lot of space and make the README page a lot heavier. Thus, `webp` was [adopted](https://github.com/mhxion/awesome-discord-communities/pull/25). You can convert your `png/jpg` icon in the
any of the following ways:

__Easy WebP Conversion:__ Drop or paste your `png/jpg` icon on [Sqoosh](https://squoosh.app/). Squoosh is [open-source](https://github.com/GoogleChromeLabs/squoosh/) and does image compression on the client-side. Once loaded, by default, the original image preview is on the left side of the draggable vertical bar, and the compressed image preview is on the right. From the right _'Compress'_ sidebar select _'WebP'_, and drag the _'Quality'_ slider to 75. You can now download the image.

![Web Conversion](images/screenshots/screenshot_02.png)

__CLI WebP Conversion:__ If you prefer command line WebP conversion, you can use
native [`cwebp` by Google](https://developers.google.com/speed/webp/docs/using#using_cwebp_to_convert_images_to_the_webp_format). It does require installing the library to your system. Use `-q` option with value `75`.

## Issues

If you've found an issue with an existing server or have a suggestion to make to improve this list, feel free to file an
issue [here](https://github.com/mhxion/awesome-discord-communities/issues/new/choose).

## Review Policy

Review policy is meant for reviewers, not necessarily for contributors. There is no real metric provided by Discord that can be used by anyone to evaluate a server. However, a maintainer will manually review the community for a period of time (1-4 days) before it can be accepted.

As an initial requirement, only technical or technology-related communities are considered. A community that is meant for people to hang out with no real active support channel will not be considered as technical. There are certain categories a technical community can be attributed to. **Generic**, **Niche**, and **Project**. There are a few distinct requirements for each of them.

[Generic servers](./README.md#programming-in-general) try to address multiple-technical-domains-in-one instead of a single specific domain, i.e., a server that offers support for all programming languages vs. a server that offers Java only. These communities are most likely to attract a lot of people in a short period, and more likely to be short-lived as it gets more and more difficult to maintain over time. For this reason, a stricter requirement, a generic server needs to be at least a year old with active moderation and messaging activity on a daily basis (excluding the off-topic channels). This specific precondition affects generic servers only.

Niche servers are the opposite of Generics, they're geared toward a smaller domain. The required minimum age is six months. Communities related to cryptocurrencies are often prone to the risk of getting hacked, for this reason, for now, only open-source owned official cryptocurrency servers will be allowed.

Project servers are part of associated communities of open-source projects or content creators (e.g., Twitch streamers, YouTube creators). Since the activity and growth of the server depend on the creators' contents, they can be accepted as soon as there is daily or semiweekly activity. If you maintain an open-source project you might also be interested in [Discord's own open-source recognition](https://discord.com/open-source).

<!-- omit in toc -->
## Attribution

Icon mockup is made by [Darius Dan](https://www.flaticon.com/authors/darius-dan).
