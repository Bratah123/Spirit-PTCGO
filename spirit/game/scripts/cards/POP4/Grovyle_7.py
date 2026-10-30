from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import blot_heal


card = PokemonCardDef(
    guid="51ad8e8e-c313-5eb9-b38d-8c0f597cef7d",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name="Grovyle",
    searchable_by=["Grovyle", "Stage 1", "Grovyle"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="POP4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=253,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
        Attack(
            title="Blot",
            game_text="Remove 2 damage counters from Grovyle.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=blot_heal(2),
        ),
    ],
)
