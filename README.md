# linkedin-roast (a Claude Code skill)

Five Claudes roast your LinkedIn profile, each one alone: a recruiter, a hiring manager, a founder, an expert in your field and a peer at your level. Then the skill fixes the profile: a new headline, an About section with the keywords people search for, every experience entry rewritten, a banner file and a headshot prompt.

It is a free alternative to paying someone on Fiverr to review your profile. Free, MIT, no signup, no API key. It is not made by Anthropic or LinkedIn.

Made by **Alex Chen** ([@nocodealex](https://instagram.com/nocodealex)), an AI creator who builds free Claude Code skills. Full guide: [chen.media](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill).

## Install

Paste this into Claude Code:

```
https://github.com/alexyc9381/linkedin-roast-skill
Install this skill, then confirm /linkedin-roast works.
```

Or as a plugin:

```
/plugin marketplace add alexyc9381/linkedin-roast-skill
/plugin install linkedin-roast-skill@linkedin-roast-skill
```

Or copy the folder into your skills folder yourself (`cp -r skills/linkedin-roast ~/.claude/skills/`). Open a new Claude Code session afterwards so it picks the skill up.

## Run it

Save your profile as a PDF first. On LinkedIn (desktop only): Me, View profile, More or Resources, Save to PDF. Put the file in the folder you opened Claude Code in, then:

```
/linkedin-roast my-profile.pdf
```

You can also paste your profile text or give it a screenshot.

## What you get

Everything goes into one folder, `linkedin-roast-output/`, in the folder where you ran it:

- `roasts.md`: the five roasts and what all five agree on.
- `new-profile.md`: the new headline (with two alternates), the new About with the keywords it chose and why, and every experience entry before and after.
- `banner.png` (and `banner.svg`): a plain banner at LinkedIn's size, 1584 x 396.
- `headshot-prompt.md`: a prompt to paste into the image tool of your choice, with your own photo attached.

It ends with a five-line checklist of what to paste into LinkedIn. See `examples/jordan-sample/` for a made-up profile and what the skill did with it.

## How it works

1. It reads your profile and strips out email, phone and address.
2. It starts five sub-agents at the same time. Each gets only your profile and one role. None sees the others' answers, so nobody goes easy on you.
3. It prints the roasts and the problems at least three of the five agree on.
4. It rewrites the headline (220 characters or fewer), the About (2,600 or fewer) and every experience entry. The bullets follow what Harvard College's Mignone Center for Career Success teaches in its resume guide: start with an action verb, say specifically what you did and end on a result with a number. Harvard does not publish this as a named formula, so the skill describes it as the guide's advice.
5. It makes the banner with code, and writes the headshot prompt (or uses an image tool if you already have one connected).

## Honest limits

- It never invents anything. Where a bullet needs a number it does not have, it leaves `[ADD YOUR NUMBER: ...]` for you to fill in. You should be able to defend every line.
- The five readers are one model playing five roles. They are a structured second opinion, not five real people, and not career advice.
- It cannot post to LinkedIn for you. You paste everything in yourself.
- LinkedIn does not publish how it ranks profiles. Keywords make your profile match what recruiters type; they do not promise a rank, interviews or connection requests.
- Claude cannot make or edit images by itself. The banner is a file made with code. For the headshot you need your own image tool; the skill only uses one that is already connected, and never claims it edited your face unless a tool did.
- Your profile goes to Claude like anything else you share. Leave out what you would not paste into a chat.
- One run starts five sub-agents and counts toward your Claude plan's usage.

## Sources

- Harvard College Guide to Creating a Strong Resume (Mignone Center for Career Success): https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/
- LinkedIn Help, Save a profile as a PDF: https://www.linkedin.com/help/linkedin/answer/a541960
- LinkedIn Help, background photo: https://www.linkedin.com/help/linkedin/answer/a568217/add-or-change-the-background-photo-on-your-profile
- LinkedIn Help, photo won't upload (profile photo and background specs): https://www.linkedin.com/help/linkedin/answer/a549049
- LinkedIn Help, profile photo guidelines: https://www.linkedin.com/help/billing/answer/430
- LinkedIn Talent Blog, About section limit: https://www.linkedin.com/business/talent/blog/product-tips/linkedin-profile-summaries-that-we-love-and-how-to-boost-your-own
- LinkedIn Recruiter Help, keyword search: https://www.linkedin.com/help/recruiter/answer/a415295


## Making a video or post about this?

Go ahead. Credit it like this, in your caption or description:

```text
/linkedin-roast skill by Alex Chen (@nocodealex): github.com/alexyc9381/linkedin-roast-skill
```

Tag [@nocodealex](https://instagram.com/nocodealex) so I can see it. Writing about it or citing it in a paper? Use **Cite this repository** in the sidebar on GitHub.

Run the tests with `python3 -m unittest discover -s tests`.
