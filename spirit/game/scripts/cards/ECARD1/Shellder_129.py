from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="b6f4c8d9-2e2f-5ccb-89e8-87e395aed60f",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    display_name="Shellder",
    searchable_by=["Shellder", "Basic", "Shellder"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=90,
    abilities=[
        Attack(
            title="Irongrip",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
