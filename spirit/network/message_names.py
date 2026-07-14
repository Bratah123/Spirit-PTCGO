from enum import Enum

class InboundMsg(str, Enum):
    """Packets sent from the Client to the Server."""
    
    # ---------------------------------------------------------
    # System & Handshake (Phase 1)
    # ---------------------------------------------------------
    # Source: dwd.core.networking.wargServer.messages.RequestConnectionServiceWithVersion
    REQ_CONNECTION_SERVICE_VERSION = "RequestConnectionServiceWithVersion"
    
    # Source: dwd.core.wargServer.messages.RequestSession
    REQ_SESSION = "RequestSession"
    
    # Source: dwd.core.wargServer.messages.RequestLogin
    REQ_LOGIN = "RequestLogin"
    
    # ---------------------------------------------------------
    # Authentication (Phase 2 - GAS)
    # ---------------------------------------------------------
    # Source: dwd.core.wargServer.messages.Outgoing.StartAuthentication
    START_AUTH = "StartAuthentication"
    
    # Source: dwd.core.networking.wargServer.authentication.gas.messages.outgoing.AuthenticateGASAuthToken
    AUTH_GAS_TOKEN = "AuthenticateGASAuthToken"
    
    # Source: dwd.core.networking.wargServer.authentication.gas.messages.outgoing.AuthenticateGASGuest
    AUTH_GAS_GUEST = "AuthenticateGASGuest"
    
    # Source: dwd.core.networking.wargServer.authentication.gas.messages.outgoing.AuthenticateGASMobile
    AUTH_GAS_MOBILE = "AuthenticateGASMobile"

    # Source: i.f.2.AuthenticateCASTicket
    AUTHENTICATE_CAS_TICKET = "AuthenticateCASTicket"

    # ---------------------------------------------------------
    # Data & Synchronization
    # ---------------------------------------------------------
    # Source: U.k.GetSetData
    GET_SET_DATA = "GetSetData"

    # Source: dwd.core.localization.service.messages.outgoing.GetAllLocalizationReleases
    GET_ALL_LOCALIZATION_RELEASES = "GetAllLocalizationReleases"

    # Source: dwd.core.commerce.messages.outgoing.GetWallet
    GET_WALLET = "GetWallet"

    # Source: GetDeckList
    GET_DECK_LIST = "GetDeckList"

    # Source: GetAvatarDeckList
    GET_AVATAR_DECK_LIST = "GetAvatarDeckList"

    # Source: dwd.Protobuf.Progression.GetProtobufScenarios
    GET_PROTOBUF_SCENARIOS = "GetProtobufScenarios"

    # Source: GetNotifications
    GET_NOTIFICATIONS = "GetNotifications"

    # Source: dwd.core.asynctournament.commands.GetActiveAsyncTournaments
    GET_ACTIVE_ASYNC_TOURNAMENTS = "GetActiveAsyncTournaments"

    # Legacy/Alternate name used by client
    GET_ACTIVE_TOURNAMENTS = "GetActiveTournaments"

    # Legacy Events-scene tournament channel (pie J.f / TournamentManager)
    # Outbound wire names are PLURAL "Tournaments" (decoded accessors aJD/aJd)
    SUBSCRIBE_TO_TOURNAMENTS_CHANNEL = "SubscribeToTournamentsChannel"
    UNSUBSCRIBE_TO_TOURNAMENTS_CHANNEL = "UnSubscribeToTournamentsChannel"

    # Legacy live bracket tournaments (pie J.f command builders)
    JOIN_TOURNAMENT = "JoinTournament"
    LEAVE_TOURNAMENT_QUEUE = "LeaveTournamentQueue"
    LEAVE_ACTIVE_TOURNAMENT = "LeaveActiveTournament"
    GET_PLAYERS_IN_QUEUE = "GetPlayersInQueue"
    GET_TOURNAMENT_IN_PROGRESS = "GetTournamentInProgress"

    # Source: dwd.core.asynctournament.commands.* (async tournament system)
    JOIN_ASYNC_TOURNAMENT = "JoinAsyncTournament"
    START_ASYNC_TOURNAMENT_GAME = "StartAsyncTournamentGame"
    RESIGN_TOURNAMENT_RUN = "ResignTournamentRun"
    CLAIM_ASYNC_TOURNAMENT_REWARD = "ClaimAsyncTournamentReward"
    CLAIM_ASYNC_TOURNAMENT_LEADERBOARD_REWARD = "ClaimAsyncTournamentLeaderboardReward"
    GET_NUMBER_OF_PLAYER_RUNS = "GetNumberOfPlayerRuns"
    GET_ASYNC_TOURNAMENT_GAME_HISTORY = "GetAsyncTournamentGameHistory"
    GET_ASYNC_TOURNAMENT_STANDINGS = "GetAsyncTournamentStandings"
    GET_TOP_RANKED_STANDINGS = "GetTopRankedStandings"
    GET_PLAYER_RANK_AND_SURROUNDING_STANDINGS = "GetPlayerRankAndSurroundingStandings"
    GET_CAN_CLAIM_LEADERBOARD_REWARDS_FOR_TOURNAMENT = "GetCanClaimLeaderboardRewardsForTournament"
    HAS_CLAIMED_ASYNC_TOURNAMENT_LEADERBOARD_REWARD = "HasClaimedAsyncTournamentLeaderboardReward"
    GET_UNACKNOWLEDGED_PACKS = "GetUnacknowledgedPacks"
    ACKNOWLEDGE_PACK = "AcknowledgePack"
    GET_LEAGUE_TIEBREAKERS_REMAINING = "GetLeagueTiebreakersRemaining"

    # Source: GetArchetypeListKeys
    GET_ARCHETYPE_LIST_KEYS = "GetArchetypeListKeys"

    # Source: GetArchetypeIDsByFamily
    GET_ARCHETYPE_IDS_BY_FAMILY = "GetArchetypeIDsByFamily"

    # Source: GetFormatLegalityForArchetypes
    GET_FORMAT_LEGALITY_FOR_ARCHETYPES = "GetFormatLegalityForArchetypes"

    # Source: GetProtobufAllAvatarArchetypesList
    GET_PROTOBUF_ALL_AVATAR_ARCHETYPES_LIST = "GetProtobufAllAvatarArchetypesList"

    # Source: GetProtobufArchetypesList
    GET_PROTOBUF_ARCHETYPES_LIST = "GetProtobufArchetypesList"

    # Source: GetCollectionCount
    GET_COLLECTION_COUNT = "GetCollectionCount"

    # Source: dwd.core.account.messages.outgoing.SetAccountSettings ({settings: {int:int}})
    SET_ACCOUNT_SETTINGS = "SetAccountSettings"

    # Source: dwd.core.switchboard.messages.GetFeatureStatuses_v2
    GET_FEATURE_STATUSES_V2 = "GetFeatureStatuses_v2"

    # Source: GetArchetypeFlags
    GET_ARCHETYPE_FLAGS = "GetArchetypeFlags"

    # Source: IsUserInActiveTournament
    IS_USER_IN_ACTIVE_TOURNAMENT = "IsUserInActiveTournament"
    GET_ACTIVE_TOURNAMENT = "GetActiveTournament"

    # Source: GetDynamicPages
    GET_DYNAMIC_PAGES = "GetDynamicPages"

    # Source: GetDynamicVersions
    GET_DYNAMIC_VERSIONS = "GetDynamicVersions"

    # Source: GetAllBannedCardsByFormats
    GET_ALL_BANNED_CARDS_BY_FORMATS = "GetAllBannedCardsByFormats"

    # Source: ViewMyLots
    VIEW_MY_LOTS = "ViewMyLots"

    # Source: GetTimeLockedArchetypes
    GET_TIME_LOCKED_ARCHETYPES = "GetTimeLockedArchetypes"

    # Chat (lobby room wire names decoded from s.f: JoinRoom/LeaveRoom/Chat)
    PRIVATE_CHAT = "PrivateChat"
    JOIN_ROOM = "JoinRoom"
    LEAVE_ROOM = "LeaveRoom"
    CHAT = "Chat"

    # Source: GetMotd
    GET_MOTD = "GetMotd"

    # Source: PublicRooms
    PUBLIC_ROOMS = "PublicRooms"

    # Source: GetFriendRoster
    GET_FRIEND_ROSTER = "GetFriendRoster"

    # Social Actions
    CREATE_FRIEND_INVITATION = "CreateFriendInvitation"
    ACCEPT_FRIEND_INVITATION = "AcceptFriendInvitation"
    DECLINE_FRIEND_INVITATION = "DeclineFriendInvitation"
    REMOVE_FRIEND = "RemoveFriend"
    SET_CURRENT_PRESENCE = "SetCurrentPresence"


    QUESTS_ENABLED = "QuestsEnabled"
    GET_ARCHETYPE_CORRECTIONS = "GetArchetypeCorrections"
    SET_ARCHETYPE_REVIEW = "SetArchetypeReview"
    CAKE_REQUEST_WEEKLY_LEADERBOARD_REWARDS = "CakeRequestWeeklyLeaderboardRewards"
    CAKE_SAVE_DECK = "CakeSaveDeck"
    CAKE_DELETE_DECK = "CakeDeleteDeck"
    VALIDATE_DECKS = "ValidateDecks"
    VALIDATE_ALL_DECKS = "ValidateAllDecks"
    GET_ACHIEVEMENTS = "GetAchievements"

    # Source: GetQuests
    GET_QUESTS = "GetQuests"

    # Source: GetPokemonFamilyMap
    GET_POKEMON_FAMILY_MAP = "GetPokemonFamilyMap"

    # Source: SetClientSetting
    SET_CLIENT_SETTING = "SetClientSetting"

    # Source: GetGuidOverride
    GET_GUID_OVERRIDE = "GetGuidOverride"

    # Shop / Commerce
    GET_AVAILABLE_PRODUCTS = "GetAvailableProducts"
    GET_FEATURED_PRODUCTS = "GetFeaturedProducts"
    GET_TOP_SELLING_PRODUCTS = "GetTopSellingProducts"
    GET_THEME_DECK_CONTENTS = "GetThemeDeckContents"
    PURCHASE_AND_OPEN_PRODUCTS = "PurchaseAndOpenProducts"
    OPEN_PRODUCTS_BY_ARCHETYPE_ID = "OpenProductsByArchetypeID"
    PURCHASE_ARCHETYPES = "PurchaseArchetypes"
    PURCHASE_CATALOG_PRODUCTS = "PurchaseCatalogProducts"

    # Code Redemption (source: n.z ValidateCode/RedeemCodes, decoded from pie-src string blob)
    VALIDATE_CODE = "ValidateCode"
    REDEEM_CODES = "RedeemCodes"

    # Trading (source: B.M command factory, decoded from pie-src string blob)
    # Each trade tab does a count-first handshake: it sends a payload-less *Count
    # request, then only asks for the page once it has the count (used as limit).
    VIEW_MY_LOTS_COUNT = "ViewMyLotsCount"
    VIEW_MY_LOTS_WITH_PAGINATION = "ViewMyLotsWithPagination"
    VIEW_ALL_PRIVATE_TRADES_COUNT = "ViewAllPrivateTradesCount"
    VIEW_ALL_PRIVATE_TRADES_WITH_PAGINATION = "ViewAllPrivateTradesWithPagination"
    VIEW_ALL_PUBLIC_TRADES_COUNT = "ViewAllPublicTradesCount"
    VIEW_ALL_PUBLIC_TRADES_WITH_PAGINATION = "ViewAllPublicTradesWithPagination"
    SEARCH_FOR_LOTS = "SearchForLots"
    ACCEPT_TRADE = "AcceptTrade"
    REMOVE_LOT = "RemoveLot"
    CREATE_LOT_WITH_ARCHETYPES = "CreateLotWithArchetypes"
    VIEW_TRADE_HISTORY = "ViewTradeHistory"
    VIEW_TRADE_HISTORY_2_COUNT = "ViewTradeHistory2Count"
    VIEW_TRADE_HISTORY_2 = "ViewTradeHistory2"
    SET_ARCHETYPE_FOR_TRADE_COUNT = "SetArchetypeForTradeCount"
    GET_CREATE_LOT_PRICES = "GetCreateLotPrices"

    # Notifications
    ACKNOWLEDGE_NOTIFICATION = "AcknowledgeNotification"
    USER_HAS_VISITED_SCENE = "UserHasVisitedScene"

    # Source: dwd.core.networking.wargServer.messages.outgoing.LogClientError
    LOG_CLIENT_ERROR = "LogClientError"
    
    # Matchmaking
    REQUEST_QUEUE_MATCH = "RequestQueueMatch"
    REQUEST_SINGLE_PLAYER_MATCH = "RequestSinglePlayerMatch"
    CANCEL_MATCH_REQUEST = "CancelMatchRequest"
    READY_FOR_MATCH_CONFIRMATION = "ReadyForMatchConfirmation"

    # Friend challenges (dwd.core.data.matchmaking.messages)
    REQUEST_MATCH_WITH_SPECIFIC_CLIENT = "RequestMatchWithSpecificClient"
    ACCEPT_MATCH_WITH_SPECIFIC_CLIENT = "AcceptMatchWithSpecificClient"
    REJECT_MATCH_WITH_SPECIFIC_CLIENT = "RejectMatchWithSpecificClient"
    CANCEL_MATCH_REQUEST_WITH_SPECIFIC_CLIENT = "CancelMatchRequestWithSpecificClient"
    
    # Gameplay
    PLAYER_READY = "PlayerReady"
    GAME_CUSTOM_CHOICE = "GameCustomChoice"
    GAME_MULLIGAN_CHOICE = "GameMulliganChoice"
    RECONNECT_TO_GAME = "ReconnectToGame"
    RESIGN_GAME = "ResignGame"
    GAME_CHAT = "GameChat"
    UPDATE_USER_TIMEOUT_STATUS = "UpdateUserTimeoutStatus"
    # Reply to SelectionWithTargetsAndActionsRequired (general in-game plays).
    # value = {gameID, selection: [[entityID, actionID], [targetResponses]] | null, counter}
    SELECTION_WITH_TARGETS_AND_ACTIONS = "SelectionWithTargetsAndActions"
    # Reply to SelectionWithTargetsRequired (setup placement, knockout replace).
    # value = {gameID, selection: {entityID, targetResponses} | null, counter}
    SELECTION_WITH_TARGETS = "SelectionWithTargets"

    # Source: WargSocket.cs
    PING = "Ping"

    def __str__(self):
        return self.value


class OutboundMsg(str, Enum):
    """Packets sent from the Server to the Client."""

    # ---------------------------------------------------------
    # System & Handshake (Phase 1)
    # ---------------------------------------------------------
    # Source: ConnectionService.cs
    CONNECTION_SERVICE = "ConnectionService"
    
    # Source: GrantedSession.cs
    GRANTED_SESSION = "GrantedSession"
    
    # Source: RequestedAuthType.cs
    REQ_AUTH_TYPE = "RequestedAuthType"
    
    # Source: Motd.cs
    MOTD = "Motd"
    
    # ---------------------------------------------------------
    # Authentication (Phase 2 - GAS)
    # ---------------------------------------------------------
    # Source: dwd.core.wargServer.authentication.platform.incoming.RequestAuthToken
    REQ_AUTH_TOKEN = "RequestAuthToken"
    
    # Source: dwd.core.account.messages.AuthenticationSuccessful
    AUTH_SUCCESS = "AuthenticationSuccessful"
    
    # Source: AuthenticationFailed.cs
    AUTH_FAILED = "AuthenticationFailed"
    
    # Source: AuthenticationError.cs
    AUTH_ERROR = "AuthenticationError"

    # ---------------------------------------------------------
    # Data & Synchronization
    # ---------------------------------------------------------
    # Source: SetDataList.cs
    SET_DATA_LIST = "SetDataList"

    # Source: dwd.core.cacheableMessages.messages.incoming.ChecksumDiff
    CHECKSUM_DIFF = "ChecksumDiff"

    # Source: dwd.core.localization.service.messages.incoming.AllLocalizationReleases
    ALL_LOCALIZATION_RELEASES = "AllLocalizationReleases"

    # Source: dwd.core.commerce.messages.incoming.CurrentWallet
    CURRENT_WALLET = "CurrentWallet"

    # Source: pie-core AccountUpdated.cs (ReplaceWith swaps ALL account attributes)
    ACCOUNT_UPDATED = "AccountUpdated"

    # Source: Decks.cs -> OnlineDecksFound
    DECK_LIST = "OnlineDecksFound"

    # Source: AvatarDeckList -> OnlineAvatarDecksFound
    AVATAR_DECK_LIST = "OnlineAvatarDecksFound"

    # Source: AllScenarios
    ALL_SCENARIOS = "AllScenarios"

    # Source: dwd.core.notifications.messages.incoming.NotificationsRequested
    NOTIFICATIONS_REQUESTED = "NotificationsRequested"

    # Source: ActiveAsyncTournaments.cs
    ACTIVE_ASYNC_TOURNAMENTS = "ActiveAsyncTournaments"

    # Legacy Events-scene tournament list (pie J\G.cs models)
    AVAILABLE_TOURNAMENT_LIST = "AvailableTournamentList"
    SUBSCRIBE_TO_TOURNAMENT_CHANNEL_SUCCESSFUL = "SubscribeToTournamentChannelSuccessful"

    # Legacy live bracket tournament pushes (pie TournamentManager dispatcher)
    TOURNAMENT_QUEUE_JOINED = "TournamentQueueJoined"
    TOURNAMENT_QUEUE_STATUS = "TournamentQueueStatus"
    USERS_IN_TOURNAMENT_QUEUE = "UsersInTournamentQueue"
    TOURNAMENT_QUEUE_LEFT = "TournamentQueueLeft"
    TOURNAMENT_QUEUE_LEFT_FAILED = "TournamentQueueLeftFailed"
    JOIN_TOURNAMENT_FAILED = "JoinTournamentFailed"
    TOURNAMENT_STARTED = "TournamentStarted"
    TOURNAMENT_ROUND_UPDATED = "TournamentRoundUpdated"
    TOURNAMENT_NEXT_ROUND_STARTING = "TournamentNextRoundStarting"
    TOURNAMENT_CANCELLED = "TournamentCancelled"
    TOURNAMENT_LEFT = "TournamentLeft"
    TOURNAMENTS_IN_PROGRESS_DATA = "TournamentsInProgressData"
    TOURNAMENT_COMPLETED = "TournamentCompleted"

    # Source: dwd.core.asynctournament.messages.* + coredll root (async tournaments)
    ASYNC_TOURNAMENT_JOINED = "AsyncTournamentJoined"
    ASYNC_TOURNAMENT_PROGRESS_UPDATED = "AsyncTournamentProgressUpdated"
    ASYNC_TOURNAMENT_DECK_UPDATED = "AsyncTournamentDeckUpdated"
    ASYNC_TOURNAMENT_REWARDS = "AsyncTournamentRewards"
    ASYNC_TOURNAMENT_STANDINGS = "AsyncTournamentStandings"
    ASYNC_TOURNAMENT_NUMBER_OF_PLAYER_RUNS = "AsyncTournamentNumberOfPlayerRuns"
    ASYNC_TOURNAMENT_GAME_HISTORY_LIST = "AsyncTournamentGameHistoryList"
    ASYNC_TOURNAMENT_LEADERBOARD_TOP_RANKED_STANDINGS = "AsyncTournamentLeaderboardTopRankedStandings"
    ASYNC_TOURNAMENT_LEADERBOARD_PLAYER_RANK_AND_SURROUNDING_STANDINGS = "AsyncTournamentLeaderboardPlayerRankAndSurroundingStandings"
    ASYNC_TOURNAMENT_LEADERBOARD_REWARDS = "AsyncTournamentLeaderboardRewards"
    ASYNC_TOURNAMENT_HAS_CLAIMED_LEADERBOARD_REWARD = "AsyncTournamentHasClaimedLeaderboardReward"
    CAN_CLAIM_LEADERBOARD_REWARDS_FOR_TOURNAMENT = "CanClaimLeaderboardRewardsForTournament"
    ASYNC_TOURNAMENT_UNACKNOWLEDGED_PACKS = "AsyncTournamentUnacknowledgedPacks"
    PACK_ACKNOWLEDGED = "PackAcknowledged"
    LEAGUE_TIEBREAKERS_REMAINING = "LeagueTiebreakersRemaining"
    JOIN_ASYNC_TOURNAMENT_ERROR = "JoinAsyncTournamentError"
    START_ASYNC_TOURNAMENT_GAME_ERROR = "StartAsyncTournamentGameError"
    CLAIM_ASYNC_TOURNAMENT_REWARD_ERROR = "ClaimAsyncTournamentRewardError"

    # Source: ArchetypeKeys.cs
    ARCHETYPE_KEYS = "ArchetypeKeys"

    # Source: ArchetypeIDsByFamily
    ARCHETYPE_IDS_BY_FAMILY = "ArchetypeIDsByFamily"

    # Source: FormatLegalityForArchetypes
    FORMAT_LEGALITY_FOR_ARCHETYPES = "FormatLegalityForArchetypes"

    # Source: AllAvatarArchetypesChecksumMatch.cs
    ALL_AVATAR_ARCHETYPES_CHECKSUM_MATCH = "AllAvatarArchetypesChecksumMatch"

    # Source: dwd.Protobuf.cake.item.AllAvatarArchetypesFound
    ALL_AVATAR_ARCHETYPES_FOUND = "AllAvatarArchetypesFound"

    # Source: dwd.Protobuf.Collection.ArchetypesFound
    ARCHETYPES_FOUND = "ArchetypesFound"

    # Source: CollectionCountFound.cs
    COLLECTION_COUNT_FOUND = "CollectionCountFound"

    # Source: AllFeatureStatuses_v2.cs
    ALL_FEATURE_STATUSES_V2 = "AllFeatureStatuses_v2"

    # Source: ArchetypeFlagsSet.cs
    ARCHETYPE_FLAGS_SET = "ArchetypeFlagsSet"
    ARCHETYPE_FLAGS_FOR_TRADE_SET = "ArchetypeFlagsForTradeSet"
    ARCHETYPE_FOR_TRADE_SET = "ArchetypeForTradeSet"
    ARCHETYPE_REVIEW_SET = "ArchetypeReviewSet"

    # Source: UserInActiveTournament.cs
    USER_IN_ACTIVE_TOURNAMENT = "UserInActiveTournament"

    # Source: DynamicLandingPages.cs
    DYNAMIC_LANDING_PAGES = "DynamicLandingPages"

    # Source: DynamicVersions.cs
    DYNAMIC_VERSIONS = "DynamicVersions"

    # Source: MyLotsRetrieved.cs
    MY_LOTS_RETRIEVED = "MyLotsRetrieved"

    # Source: MyLotsRetrievedCount.cs
    MY_LOTS_RETRIEVED_COUNT = "MyLotsRetrievedCount"

    # Source: TimeLockedArchetypesFound
    TIME_LOCKED_ARCHETYPES = "TimeLockedArchetypes"

    # Source: PokemonFamilyMap.cs
    POKEMON_FAMILY_MAP = "PokemonFamilyMap"

    # Code Redemption responses (CodeIsValid.cs / InvalidCode.cs / CodeSuccessfullyRedeemed.cs / CodeRedemptionFailure.cs)
    CODE_IS_VALID = "CodeIsValid"
    INVALID_CODE = "InvalidCode"
    CODE_SUCCESSFULLY_REDEEMED = "CodeSuccessfullyRedeemed"
    CODE_REDEMPTION_FAILURE = "CodeRedemptionFailure"

    # Trading responses (LotsRetrieved.cs / MyLotsRetrieved.cs / PrivateLotsRetrieved.cs / LotCreated.cs / ...)
    CREATE_LOT_PRICES = "CreateLotPrices"
    LOTS_RETRIEVED = "LotsRetrieved"
    LOTS_RETRIEVED_COUNT = "LotsRetrievedCount"
    PRIVATE_LOTS_RETRIEVED = "PrivateLotsRetrieved"
    PRIVATE_LOTS_RETRIEVED_COUNT = "PrivateLotsRetrievedCount"
    TRADE_HISTORY_RETRIEVED = "TradeHistoryRetrieved"
    TRADE_HISTORY_RETRIEVED_COUNT = "TradeHistoryRetrievedCount"
    LOT_CREATED = "LotCreated"
    LOT_REMOVED = "LotRemoved"
    LOT_SOLD = "LotSold"
    ERROR_CREATING_LOT = "ErrorCreatingLot"
    ERROR_PURCHASING_LOT = "ErrorPurchasingLot"
    ERROR_REMOVING_LOT = "ErrorRemovingLot"

    # Source: AllBannedCardsByFormat.cs (Note: client request is plural, response is singular)
    ALL_BANNED_CARDS_BY_FORMAT = "AllBannedCardsByFormat"

    # Source: NoGuidOverride.cs
    NO_GUID_OVERRIDE = "NoGuidOverride"

    # Source: ClientSettingSet.cs (Guessed based on naming convention)
    CLIENT_SETTING_SET = "ClientSettingSet"
    
    # Source: ArchetypeCorrections.cs (Guessed)
    ARCHETYPE_CORRECTIONS = "ArchetypeCorrections"

    # Source: CakeWeeklyLeaderboardRewards.cs (Guessed)
    CAKE_WEEKLY_LEADERBOARD_REWARDS = "CakeWeeklyLeaderboardRewards"
    DECK_SAVED = "DeckSaved"
    DECK_DELETED = "DeckDeleted"
    DECKS_VALIDATED = "DecksValidated"
    LIST_ACHIEVEMENTS = "ListAchievements"

    # ---------------------------------------------------------
    # Extended Login Sequence
    # ---------------------------------------------------------
    # Source: EulaSuccessful.cs
    EULA_SUCCESSFUL = "EulaSuccessful"

    # Source: CohortsForAccount.cs
    COHORTS_FOR_ACCOUNT = "CohortsForAccount"

    # Source: PlayerNotInGame.cs
    PLAYER_NOT_IN_GAME = "PlayerNotInGame"

    # Source: PlayerStillInGame.cs (drives PlayerStillInGameObserver -> ReconnectToGame at login)
    PLAYER_STILL_IN_GAME = "PlayerStillInGame"

    # In-match opponent-disconnect indicator (client cmd m.q): shows the no-button
    # "opponent disconnected, waiting Ns" dialog and stops the chess clock.
    # {accountID: <dropped player>, waitTime: <ms>}. PlayerReconnected (m.r)
    # dismisses it and restarts the clock. {accountID: <returned player>}.
    PLAYER_DISCONNECTED = "PlayerDisconnected"
    PLAYER_RECONNECTED = "PlayerReconnected"

    # Source: NetworkStatusIndicatorConfiguration.cs
    NETWORK_STATUS_INDICATOR_CONFIGURATION = "NetworkStatusIndicatorConfiguration"

    # Source: DefaultTrainerChallengeDeckMessage.cs
    DEFAULT_TRAINER_CHALLENGE_DECK_MESSAGE = "DefaultTrainerChallengeDeckMessage"

    # Source: CurrentVersusSeason.cs
    CURRENT_VERSUS_SEASON = "CurrentVersusSeason"

    # Source: CurrentDailyRewardTrack.cs
    CURRENT_DAILY_REWARD_TRACK = "CurrentDailyRewardTrack"

    # Source: QuestConfigurationUpdated.cs
    QUEST_CONFIGURATION_UPDATED = "QuestConfigurationUpdated"

    # Source: DailyLogin.cs
    DAILY_LOGIN = "DailyLogin"

    # Source: AccountPropertiesUpdated.cs
    ACCOUNT_PROPERTIES_UPDATED = "AccountPropertiesUpdated"

    # ---------------------------------------------------------
    # Commerce
    # ---------------------------------------------------------
    # Source: AvailableProducts.cs
    AVAILABLE_PRODUCTS = "AvailableProducts"
    
    # Source: FeaturedProducts.cs
    FEATURED_PRODUCTS = "FeaturedProducts"
    
    # Source: TopSellingProducts.cs
    TOP_SELLING_PRODUCTS = "TopSellingProducts"
    
    # Source: ThemeDeckContentsMap.cs
    THEME_DECK_CONTENTS_MAP = "ThemeDeckContentsMap"

    # Source: dwd.core.commerce.messages.incoming.ProductsOpened
    PRODUCTS_OPENED = "ProductsOpened"

    # Source: dwd.core.commerce.messages.incoming.ProductsPurchased
    PRODUCTS_PURCHASED = "ProductsPurchased"

    # Source: dwd.core.commerce.messages.incoming.ArchetypesPurchased
    ARCHETYPES_PURCHASED = "ArchetypesPurchased"

    # ---------------------------------------------------------
    # Social & Other
    # ---------------------------------------------------------
    # Source: FriendRoster.cs
    FRIEND_ROSTER = "FriendRoster"

    # Source: pie.socialv2.messages.AvailableRooms (handler s.w auto-joins a
    # random RoomType.Lobby room from the list via JoinRoom).
    AVAILABLE_ROOMS = "AvailableRooms"
    # Source: pie.socialv2.messages.* — lobby room membership + room chat.
    CHAT_CONNECTED = "ChatConnected"
    CHAT_DISCONNECTED = "ChatDisconnected"
    NOTIFY_CHAT = "NotifyChat"
    NOTIFY_JOIN = "NotifyJoin"
    NOTIFY_LEAVE = "NotifyLeave"

    # Source: Quests.cs (Guessed)
    QUESTS = "Quests"

    # Social Notifications
    NOTIFICATION = "Notification"
    NOTIFY_PRIVATE_CHAT = "NotifyPrivateChat"
    FRIEND_INVITATION = "FriendInvitation"
    FRIEND_ADDED = "FriendAdded"
    FRIEND_REMOVED = "FriendRemoved"
    FRIEND_ERROR = "FriendError"
    FRIEND_PRESENCE = "FriendPresence"

    # Matchmaking
    MATCH_QUEUE_ENTERED = "MatchQueueEntered"
    MATCH_QUEUE_LEFT = "MatchQueueLeft"
    CONFIRM_READY_FOR_MATCH = "ConfirmReadyForMatch"
    MATCH_FOUND = "MatchFound"
    SERIALIZED_GAME_STATE = "SerializedGameState"

    # Friend challenges (dwd.core.matchmaking.messages.incoming)
    MATCH_REQUESTED = "MatchRequested"
    MATCH_REQUEST_SENT = "MatchRequestSent"
    MATCH_REQUEST_REJECTED = "MatchRequestRejected"
    MATCH_REQUEST_CANCELLED = "MatchRequestCancelled"
    MATCH_REQUEST_WITH_SPECIFIC_CLIENT_FAILED = "MatchRequestWithSpecificClientFailed"
    
    # Gameplay
    COIN_FLIP_CHOICE_REQUIRED = "CoinFlipChoiceRequired"
    MULTIPLE_COIN_FLIP_EFFECT = "MultipleCoinFlipEffect"
    MULTIPLE_COIN_FLIP_WITH_CONTEXT_EFFECT = "MultipleCoinFlipWithContextEffect"
    GO_FIRST_CHOICE_REQUIRED = "GoFirstChoiceRequired"
    FORCE_SELECTION_FINISHED = "ForceSelectionFinished"
    START_SEQUENCE = "StartSequence"
    SEQUENCE_MESSAGE = "SequenceMessage"
    STOP_SEQUENCE = "StopSequence"
    ACTIVE_PLAYER_SET = "ActivePlayerSet"
    OBSERVER_CUSTOM_CHOICE_OFFER_MESSAGE = "ObserverCustomChoiceOfferMessage"
    CUSTOM_CHOICE_OFFER_MESSAGE = "CustomChoiceOfferMessage"
    # Generic button-choice prompt (renders via the default R.y dialog when
    # sortType/kind is unmapped); replied with GameCustomChoice.
    CUSTOM_CHOICE_REQUIRED = "CustomChoiceRequired"
    NOTIFY_GAME_CHAT = "NotifyGameChat"

    # Setup phase (post coin flip): entity movement + reveal + mulligan
    ENTITY_MOVED = "EntityMoved"
    ENTITY_INTRODUCED = "EntityIntroduced"
    # Re-hides a revealed card (client L.U -> EntityComponent.ResetAttributes):
    # restores the face-down back after a "look at your Prizes" reveal.
    ATTRIBUTES_RESET = "AttributesReset"
    # Presents a card large center-screen to viewers who don't own it (m.u);
    # Return=true tucks it back afterwards, Return=false leaves it in the
    # multiPresentArea for a following attach move (l.a) to consume.
    REVEAL_CARD_TO_ALL_EFFECT = "RevealCardToAllEffect"
    MULLIGAN_CHOICE_REQUIRED = "MulliganChoiceRequired"
    SHUFFLED = "Shuffled"
    # Deck-lift animation trigger (S.I); required in HandShuffledAndMovedToDeck.
    PLACE_ON_BOTTOM = "PlaceOnBottom"
    # Full-screen carousel revealing a player's mulliganed hand(s) to the opponent.
    MULLIGAN_REVEAL_CARDS_EFFECT = "MulliganRevealCardsEffect"
    # Center-screen prompt override (m.l): shows `prompt` and hides the Next
    # button while up. doPause=false leaves it until ClosePauseOnPromptEffect.
    PAUSE_ON_PROMPT_EFFECT = "PauseOnPromptEffect"
    # Clears the PauseOnPromptEffect override (d.C; no side effects).
    CLOSE_PAUSE_ON_PROMPT_EFFECT = "ClosePauseOnPromptEffect"
    # Entity-selection prompt with per-entity action trees (general in-game
    # plays; NOT setup placement -- its drop path stalls on the ActionsNode).
    SELECTION_WITH_TARGETS_AND_ACTIONS_REQUIRED = "SelectionWithTargetsAndActionsRequired"
    # Single-level entity-selection prompt (setup active/bench placement,
    # knockout replacement): pick one entity, no action tree.
    SELECTION_WITH_TARGETS_REQUIRED = "SelectionWithTargetsRequired"

    # Attack choreography (inside an "Attack" sequence bracket, in order):
    # ability-begin marker (L.o), damage popup + lunge trigger (m.m),
    # HP attribute update, ability-finished marker (k.U).
    ABILITY_PLAYED_EFFECT = "AbilityPlayedEffect"
    CAKE_ATTACK_EFFECT = "CakeAttackEffect"
    # Raw damage-counter placement (Poison/Burn checkup ticks, Confusion self-hit):
    # no W/R, no passive pipeline -- damage counters, not attack damage.
    PLACE_DAMAGE_EFFECT = "PlaceDamageEffect"
    # Heal FX + green fly-text (command L.y): {source, targets, amount}.
    CREATURE_HEAL_WITH_CONTEXT_EVENT = "CreatureHealWithContextEvent"
    # Replaces one attribute on an introduced entity (AttributeModifiedCommand).
    ATTRIBUTE_MODIFIED = "AttributeModified"
    ABILITY_FINISHED_EFFECT = "AbilityFinishedEffect"
    # Named entity parameter for a bracket executor (e.g. Evolve needs "From"/"Into").
    ENTITY_ID_DATA_EFFECT = "EntityIDDataEffect"
    # Orb-of-light targets: the Attack executor injects the r.u projectile group
    # from the playmat's attack-source entity to these targets.
    NON_DAMAGING_TARGETS_EFFECT = "NonDamagingTargetsEffect"
    # Flips the acting player's playmat VSTAR marker face-down (handler P.Y
    # matches "user" against the player account IDs). One-way until sudden death.
    VSTAR_POWER_USED_EFFECT = "VSTARPowerUsedEffect"
    # GX equivalent of the VSTAR marker flip (handler b.M).
    GX_ATTACK_USED_EFFECT = "GXAttackUsedEffect"
    # End-of-game dialog (handler D.Z): winner/loser account IDs + reward info.
    GAME_COMPLETED_MESSAGE = "GameCompletedMessage"

    def __str__(self):
        return self.value
