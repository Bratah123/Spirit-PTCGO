from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37838b6c-0707-590a-8c81-287f73cfafc4",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Flame Burst",
            game_text="Does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)