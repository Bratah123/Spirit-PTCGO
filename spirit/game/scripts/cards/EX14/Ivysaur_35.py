from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import stretch_vine_bench
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="369e86af-9985-541e-b038-5fecee7387d7",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur", "Stage 1", "Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=1,
    abilities=[
        Attack(
            title="Stretch Vine",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
                        effect=stretch_vine_bench(30),
        ),
        Attack(
            title="Sharp Leaf",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)