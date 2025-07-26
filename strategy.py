def crossover_strategy(df, fast=9, slow=21):
    df['fast_ma'] = df['close'].rolling(window=fast).mean()
    df['slow_ma'] = df['close'].rolling(window=slow).mean()

    last_fast = df['fast_ma'].iloc[-2:]
    last_slow = df['slow_ma'].iloc[-2:]

    if last_fast.iloc[0] < last_slow.iloc[0] and last_fast.iloc[1] > last_slow.iloc[1]:
        return 'buy'
    elif last_fast.iloc[0] > last_slow.iloc[0] and last_fast.iloc[1] < last_slow.iloc[1]:
        return 'sell'
    return None
