from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_hand, place_counters
from spirit.game.card_effects.ex import magic_evens_passive


card = PokemonCardDef(
    guid="21270245-4c40-5358-a24e-35f580a0624a",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeex.Name",
    display_name="Mr. Mime ex",
    searchable_by=["Mr. Mime ex", "Basic", "ex", "MrMimeex"],
    subtypes=["Basic", "ex"],
    collector_number=111,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Evens",
            game_text="If Mr. Mime ex would be damaged by an attack, prevent that attack's damage done to Mr. Mime ex if that damage is 20, 40, 60, 80, 100, 120, 140, 160, or 180.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=magic_evens_passive(),
        ),
        Attack(
            title="Breakdown",
            game_text="Count the number of cards in your opponent's hand. Put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(count_hand('opponent')),
        ),
    ],
)