-- SpiritPTCGO player database schema (MariaDB / MySQL).

-- Manually maintained deployment schema; update alongside spirit.database.models.

-- Create/select an empty database first; this script contains no player data.

SET NAMES utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE accounts (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	username VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	password_hash VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	screen_name VARCHAR(255) COLLATE utf8mb4_bin, 
	is_admin BOOL NOT NULL, 
	settings_json LONGTEXT NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (id), 
	UNIQUE (account_id), 
	UNIQUE (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE async_tournaments (
	tournament_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	definition_json LONGTEXT NOT NULL, 
	enabled BOOL NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (tournament_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE daily_login_progress (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	last_claim_date DATE, 
	streak INTEGER NOT NULL, 
	activations INTEGER NOT NULL, 
	PRIMARY KEY (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE dynamic_pages (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	page_type VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	sort_order INTEGER NOT NULL, 
	content_json LONGTEXT NOT NULL, 
	enabled BOOL NOT NULL, 
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE redemption_codes (
	code_string VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	reward_json LONGTEXT NOT NULL, 
	max_uses INTEGER NOT NULL, 
	current_uses INTEGER NOT NULL, 
	enabled BOOL NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (code_string)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE shop_items (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	product_guid VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	display_name VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	currency INTEGER NOT NULL, 
	price INTEGER NOT NULL, 
	enabled BOOL NOT NULL, 
	featured BOOL NOT NULL, 
	top_selling BOOL NOT NULL, 
	sort_order INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (product_guid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE tournament_leaderboard_claims (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	tournament_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	`rank` INTEGER NOT NULL, 
	claimed_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (id), 
	UNIQUE (tournament_id, account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE trade_offers (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	offer_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	sender_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	recipient_id VARCHAR(255) COLLATE utf8mb4_bin, 
	offering_json LONGTEXT NOT NULL, 
	requesting_json LONGTEXT NOT NULL, 
	status VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	accepted_by VARCHAR(255) COLLATE utf8mb4_bin, 
	created_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (id), 
	UNIQUE (offer_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE INDEX ix_trade_offers_recipient_id ON trade_offers (recipient_id);

CREATE INDEX ix_trade_offers_sender_id ON trade_offers (sender_id);

CREATE INDEX ix_trade_offers_status_created ON trade_offers (status, created_at);

CREATE INDEX ix_trade_offers_status_recipient ON trade_offers (status, recipient_id);

CREATE INDEX ix_trade_offers_status_sender ON trade_offers (status, sender_id);

CREATE TABLE versus_progress (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	season_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	points INTEGER NOT NULL, 
	all_time_points INTEGER NOT NULL, 
	granted_json LONGTEXT NOT NULL, 
	PRIMARY KEY (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE archetype_flags (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	archetype_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	wanted INTEGER NOT NULL, 
	for_trade INTEGER NOT NULL, 
	review INTEGER NOT NULL, 
	PRIMARY KEY (account_id, archetype_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE code_redemption_entries (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	code_string VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	redeemed_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (id), 
	UNIQUE (code_string, account_id), 
	FOREIGN KEY(code_string) REFERENCES redemption_codes (code_string)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE collection (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	archetype_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	tradable_count INTEGER NOT NULL, 
	nontradable_count INTEGER NOT NULL, 
	PRIMARY KEY (account_id, archetype_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE daily_quests (
	quest_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	offered_date DATE NOT NULL, 
	status VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	definition LONGTEXT NOT NULL, 
	activations INTEGER NOT NULL, 
	accepted_at FLOAT, 
	PRIMARY KEY (quest_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE INDEX ix_daily_quests_account_id ON daily_quests (account_id);

CREATE TABLE decks (
	id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	name VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	deck_data LONGTEXT NOT NULL, 
	is_avatar BOOL NOT NULL, 
	overall_wins INTEGER NOT NULL, 
	overall_played INTEGER NOT NULL, 
	wins_since_last_edit INTEGER NOT NULL, 
	played_since_last_edit INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE INDEX ix_decks_account_id ON decks (account_id);

CREATE TABLE friends (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	friend_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	status INTEGER NOT NULL, 
	PRIMARY KEY (account_id, friend_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id), 
	FOREIGN KEY(friend_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE INDEX ix_friends_friend_id ON friends (friend_id);

CREATE TABLE quest_accounts (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	enabled BOOL NOT NULL, 
	selected_date DATE, 
	affinity_xp LONGTEXT NOT NULL, 
	PRIMARY KEY (account_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE quest_match_credits (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	game_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	PRIMARY KEY (account_id, game_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE tournament_entries (
	entry_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	tournament_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	deck_json LONGTEXT NOT NULL, 
	wins INTEGER NOT NULL, 
	losses INTEGER NOT NULL, 
	tiebreakers INTEGER NOT NULL, 
	status VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	rewards_claimed BOOL NOT NULL, 
	history_json LONGTEXT NOT NULL, 
	last_update BIGINT NOT NULL, 
	created_at DATETIME NOT NULL DEFAULT now(), 
	PRIMARY KEY (entry_id), 
	FOREIGN KEY(tournament_id) REFERENCES async_tournaments (tournament_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE INDEX ix_tournament_entries_account_id ON tournament_entries (account_id);

CREATE INDEX ix_tournament_entries_tournament_id ON tournament_entries (tournament_id);

CREATE TABLE wallets (
	account_id VARCHAR(255) COLLATE utf8mb4_bin NOT NULL, 
	coins INTEGER NOT NULL, 
	gems INTEGER NOT NULL, 
	tickets INTEGER NOT NULL, 
	PRIMARY KEY (account_id), 
	FOREIGN KEY(account_id) REFERENCES accounts (account_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
