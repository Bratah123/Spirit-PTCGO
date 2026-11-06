from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="a5fef12c-a145-529d-90c9-82ed517d67e2",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasGloom.Name",
    display_name="Erika's Gloom",
    searchable_by=["Erika's Gloom", "Stage 1", "ErikasGloom"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Dream Dance",
            game_text="Both the Defending Pok\u00e9mon and Erika's Gloom are now Asleep (after doing damage).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
        Attack(
            title="Vile Smell",
            game_text="Both the Defending Pok\u00e9mon and Erika's Gloom are now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)
