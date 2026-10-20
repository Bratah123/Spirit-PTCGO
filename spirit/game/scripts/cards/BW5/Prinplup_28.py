from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="4aeb62ac-2f5b-50d5-bc5b-c8e13953dcfb",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=["Prinplup", "Stage 1", "Prinplup"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)