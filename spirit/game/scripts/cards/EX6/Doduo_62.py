from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import random_peck, run_around

card = PokemonCardDef(
    guid="fffeb57b-2f74-5fb0-8a6e-2a796f6f9d8d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    display_name="Doduo",
    searchable_by=["Doduo", "Basic", "Doduo"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=84,
    abilities=[
        Attack(
            title="Run Around",
            game_text="Switch Doduo with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=run_around(),
        ),
        Attack(
            title="Random Peck",
            game_text="Flip 2 coins. This attack does 10 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=random_peck(10, 10, 2),
        ),
    ],
)