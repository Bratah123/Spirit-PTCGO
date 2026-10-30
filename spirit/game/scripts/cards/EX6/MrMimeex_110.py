from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_hand, place_counters
from spirit.game.card_effects.ex import magic_odds_passive


card = PokemonCardDef(
    guid="529a6440-f191-552b-adf0-22b115ce174d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeex.Name",
    display_name="Mr. Mime ex",
    searchable_by=["Mr. Mime ex", "Basic", "ex", "MrMimeex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Odds",
            game_text="If Mr. Mime ex would be damaged by an attack, prevent that attack's damage done to Mr. Mime ex if that damage is 10, 30, 50, 70, 90, 110, 130, 150, or 170.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=magic_odds_passive(),
        ),
        Attack(
            title="Breakdown",
            game_text="Count the number of cards in your opponent's hand. Put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(count_hand('opponent')),
        ),
    ],
)