from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43fbeca6-bc0a-5b20-a625-73a59d22ef16",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name",
    display_name="Mamoswine",
    searchable_by=["Mamoswine", "Stage 2", "Mamoswine"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Frost Stone",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Continuous Headbutt",
            game_text="Flip a coin until you get tails. This attack does 90 damage times the number of heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)