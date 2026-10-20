from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="632c7790-0845-5d87-82f6-d3a720207b55",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    display_name="Shroomish",
    searchable_by=["Shroomish", "Basic", "Shroomish"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=285,
    abilities=[
        Attack(
            title="Worry Seed",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)