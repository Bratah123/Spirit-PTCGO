from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing


card = PokemonCardDef(
    guid="1410099d-4862-53de-a87f-dd134ca04340",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysShellder.Name",
    display_name="Misty's Shellder",
    searchable_by=["Misty's Shellder", "Basic", "MistysShellder"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=90,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Clamp",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(then=condition_attack(SpecialConditions.PARALYZED)),
        ),
    ],
)
