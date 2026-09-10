# GPT-6 Astra Computer Use Starter

**Build AI agents that control your computer like a human would.**

This is a starter kit for building computer use agents inspired by OpenAI's GPT-6 Astra capabilities. Learn how to create agents that interact with GUIs, automate workflows, and execute complex tasks through mouse and keyboard actions.

## 🎯 What You'll Build

A working agent that can:
- Take screenshots of your desktop
- Analyze UI elements using vision models
- Predict and execute mouse clicks, keyboard inputs, and scrolling
- Complete multi-step tasks like "open Excel and create a pivot table"
- Learn from success/failure feedback loops

## 🚀 Quick Start

```bash
# Clone this repo
git clone https://github.com/Varritech/gpt6-computer-use-starter.git
cd gpt6-computer-use-starter

# Install dependencies
pip install -r requirements.txt

# Set up your API keys
export OPENAI_API_KEY="your-key-here"

# Run the demo
python main.py --task "open calculator and calculate 123 * 456"
```

## 📚 The Guide

Read **[GUIDE.md](./GUIDE.md)** for the complete deep dive covering:
- How GPT-6 Astra's computer use actually works
- The looped transformer architecture explained
- Building your own training harness
- Reinforcement Learning with Verifiable Rewards (RLVR) for GUI tasks
- Cost analysis: API vs self-hosted inference
- Production deployment patterns

## 🏗️ Architecture Overview

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Prompt    │────▶│ Vision Model │────▶│  Action     │
│  + Screenshot│     │  (Analysis)  │     │  Predictor  │
└─────────────┘     └──────────────┘     └──────┬──────┘
                                                │
                                                ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Success/   │◀────│   Execute    │◀────│ Mouse/Keybd │
│  Failure    │     │   Action     │     │  Controller │
└─────────────┘     └──────────────┘     └─────────────┘
```

## 📁 Project Structure

```
.
├── README.md           # This file
├── GUIDE.md            # Complete technical guide (800-1500 words)
├── requirements.txt    # Python dependencies
├── main.py            # Entry point with CLI
├── agent/
│   ├── screenshot.py   # Screen capture utilities
│   ├── vision.py       # UI analysis with CLIP/GPT-4V
│   ├── actions.py      # Mouse/keyboard execution
│   └── trainer.py      # RLVR training loop
└── examples/
    ├── basic_task.py   # Simple automation example
    └── excel_pivot.py  # Complex multi-step workflow
```

## 🔥 Why This Matters

GPT-6 Astra achieved **99.9% on ARC-AGI-3** and dominates computer use benchmarks. But you don't need GPT-6 to build production agents today. This guide shows you how to:

1. **Replicate the workflow** using available models (GPT-4V, Claude 3.5 Sonnet, LLaVA)
2. **Train custom policies** for your specific apps (Excel, Figma, VS Code)
3. **Deploy at scale** with proper error handling and observability
4. **Cut costs 90%** vs naive API usage through smart caching and local inference

## 🛠️ Tech Stack

- **Python 3.10+** - Core language
- **OpenAI API / Anthropic API** - Vision + reasoning models
- **PyAutoGUI** - Cross-platform mouse/keyboard control
- **Pillow + mss** - Fast screenshot capture
- **Stable Baselines3** - RL training (optional advanced section)
- **Docker** - Production deployment

## 📊 Benchmarks to Track

When building your agent, measure:
- **Task Success Rate** (% of tasks completed without human intervention)
- **Steps per Task** (fewer = more efficient agent)
- **Latency** (time from prompt to action execution)
- **Cost per Task** (API calls × token usage)

## 🚨 Common Pitfalls

1. **Screenshot frequency** - Don't capture every action (expensive). Use change detection.
2. **Action space explosion** - Limit possible actions. Start with click/type/scroll only.
3. **No verification** - Always verify actions succeeded before proceeding.
4. **Ignoring accessibility APIs** - Use OS-level accessibility when available (faster + more reliable than pure vision).

## 📈 Next Steps

1. Run the basic example (`examples/basic_task.py`)
2. Read [GUIDE.md](./GUIDE.md) for architecture deep dive
3. Customize `agent/actions.py` for your target application
4. Set up RLVR training loop for domain-specific optimization
5. Deploy to production with monitoring (see GUIDE.md Section 7)

## 🤝 Contributing

Found a better pattern? Submit a PR. Building something cool with this? Open an issue to share.

## 📄 License

MIT License - see [LICENSE](./LICENSE)

## 👨‍💻 Author

**Varritech** | christian@varritech.com

*Bold ideas wait for no one.*

---

**Fork this repo** and start building. The future of agentic computing is here.
