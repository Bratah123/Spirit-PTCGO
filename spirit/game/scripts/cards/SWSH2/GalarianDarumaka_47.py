from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="730727b9-ab87-50c2-9d94-5a24297fd44f",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianDarumaka.Name",
    display_name="Galarian Darumaka",
    searchable_by=["Galarian Darumaka", "Basic", "GalarianDarumaka"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=554,
    abilities=[
        Attack(
            title="Ice Punch",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)