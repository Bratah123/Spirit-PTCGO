from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand


card = PokemonCardDef(
    guid="ce64e555-aa4f-5dee-ba62-c9ab1d1f6cce",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Attack(
            title="Clear Search",
            game_text="Search your deck for any 3 cards and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(None, count=3, minimum=0, reveal=False,
                                  prompt='Choose any 3 cards to put into your hand.'),
        ),
        Attack(
            title="Water Pulse",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)