from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="405e7be5-a208-59db-b327-f0a9cfbd566b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianAvalugg.Name",
    display_name="Hisuian Avalugg",
    searchable_by=["Hisuian Avalugg", "Stage 1", "HisuianAvalugg"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Ability(
            title="Massive Ice",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Mountain Gale",
            game_text="If a Stadium is in play, this attack does 120 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)