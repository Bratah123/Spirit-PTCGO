from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import gentle_song


card = PokemonCardDef(
    guid="e4cf8192-a562-546b-971f-79dfff355ee0",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Gentle Song",
            game_text="If Lapras has any damage counters on it, remove 2 of them from it (1 if it only has 1). If the Defending Pok\u00e9mon has any damage counters on it, remove 2 of them from it (1 if it only has 1). The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gentle_song,
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
