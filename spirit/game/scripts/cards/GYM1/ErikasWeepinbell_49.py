from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="faa1c98c-3670-5338-b5e4-f8662d04ecb8",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    display_name="Erika's Weepinbell",
    searchable_by=["Erika's Weepinbell", "Stage 1", "ErikasWeepinbell"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Sleep Poison",
            game_text="The Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
