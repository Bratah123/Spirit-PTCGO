from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import leech_seed


card = PokemonCardDef(
    guid="018909e5-0435-50fa-addd-5419c3c0108d",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="If this attack damages the Defending Pok\u00e9mon (after applying Weakness and Resistance), remove 1 damage counter from Venusaur, if it has any.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=leech_seed,
        ),
        Attack(
            title="Fury Strikes",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)
