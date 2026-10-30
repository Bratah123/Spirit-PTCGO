from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, flip_damage


card = PokemonCardDef(
    guid="ca9c54d3-828d-5423-97dc-d25b0939e27e",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="NEO1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="Beat Up",
            game_text="Flip a coin for each of your Pok\u00e9mon in play (including this one). This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, coins_from=count_in_play("mine")),
        ),
    ],
)
