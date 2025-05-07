🚀 Reinforcement Learning with LunarLander-v2: My First RL Project
This project marks my first hands-on journey into Reinforcement Learning (RL) using OpenAI Gym’s classic LunarLander-v2 environment. I designed a Deep Q-Network (DQN) model from scratch and trained it using a custom dataset of state-action transitions, rewards, and terminal flags.

🧠 Project Objectives
✅ Learn how Reinforcement Learning works

✅ Build a Deep Q-Network (DQN) in PyTorch

✅ Train using offline data (state, action, reward, next_state, done)

✅ Visualize Q-values, actions, and lander behavior

✅ Understand how intelligent agents learn from reward feedback

📦 Dataset Used
Dataset extracted from:

Environment: LunarLander-v2 (OpenAI Gym)

Files:

LunarLanderv2_Obs.csv: Observation and action data

LunarLander-v2_Reward.csv: Episode rewards

📊 Key Steps
1. Data Preprocessing
Merged state, action, reward, next_state, done for each episode

Handled and removed NaN and inf values

Normalized features using StandardScaler

Clipped reward values for stability

2. DQN Model Architecture
Input size: 8 (state features)

Output size: 4 (actions)

Hidden layers: 2 fully connected (128 neurons each)

Activation: ReLU

Framework: PyTorch

python
Copy
Edit
nn.Sequential(
  nn.Linear(input_dim, 128),
  nn.ReLU(),
  nn.Linear(128, 128),
  nn.ReLU(),
  nn.Linear(128, output_dim)
)
3. Training the Agent
Trained using Q-learning update:

less
Copy
Edit
Q(s, a) ← r + γ max Q(s', a')
Loss: Mean Squared Error (MSE)

Used target network for stability

10 training epochs with loss decreasing steadily

4. Evaluation & Visualization
Visualized:

Reward distribution

Action frequency

Trajectory of lander (Episode 1)

Q-values across states

Used PCA for 2D projection of Q-values and action space

📈 Results
Loss decreased from ~2800 to ~1800 over 10 epochs

Balanced exploration across all 4 actions

Agent trajectory followed expected descent path

PCA projections highlighted clear Q-value clusters by action

🎓 Key Learnings
Understanding the RL data format (state, action, reward, next_state, done)

Importance of preprocessing for stable RL training

Training DQNs offline with replay-style data

Visualizing RL policies and behaviors

Handling training issues (NaNs, scaling, clipping, etc.)

📌 Technologies Used
Python 3

Pandas, NumPy, scikit-learn

PyTorch

Matplotlib & Seaborn

OpenAI Gym (offline data)

💡 Future Work
Use live environment simulation for training

Explore Double DQN, Dueling DQN, and Prioritized Experience Replay

Implement epsilon-greedy policy for exploration

Extend to other Gym environments (CartPole, MountainCar)

🤝 Let's Connect
If you're also learning RL or working on OpenAI Gym projects, let’s share knowledge and grow together!

“Learning to learn is the most powerful skill in the AI world.”


https://www.kaggle.com/code/dilrabonu/openai-gym

![image](https://github.com/user-attachments/assets/6d952a13-02ed-4dca-96ec-5168786120f8)

